import redis
from datetime import datetime
from core.security import get_password_hash, verify_password, DeAesCrypt
from schemas.user import UserCreate, UserInDB, UserLogin
from db.session import AsyncIOMotorClient
from db.session import redis_pool


class CRUDUser:

    mdb = 'automation_data'
    collection = 'user_info'

    async def get_by_username(self, db: AsyncIOMotorClient, username: str):
        query_params = {'username': username}
        res = await db[self.mdb][self.collection].find_one(query_params)
        return res

    async def get_user_info(self, db: AsyncIOMotorClient, username: str):
        query_params = {'username': username}
        r_c = redis.Redis(connection_pool=redis_pool)
        redis_query_key = r_c.get(username)
        if redis_query_key:
            return r_c.hgetall(redis_query_key)
        else:
            res = await db[self.mdb][self.collection].find_one(query_params)
            if not res:
                return None
            clean_dict = {
                "_id": str(res['_id']),
                "username": res['username'],
                "password": res['password'],
                "full_name": res['full_name'],
                "is_activate": 1 if res['is_activate'] else 0,
                "is_superuser": 1 if res['is_superuser'] else 0
            }
            r_c.set(username, clean_dict['_id'], 43200)
            r_c.delete(clean_dict['_id'])
            r_c.hmset(name=clean_dict['_id'], mapping=clean_dict)
            return clean_dict

    async def create(self, db: AsyncIOMotorClient, obj_in: UserCreate):
        user_info = await db[self.mdb][self.collection].find_one({'username': obj_in.username})
        if user_info:
            return None
        else:
            set_params = {
                'username': obj_in.username,
                'password': get_password_hash(DeAesCrypt(obj_in.password, obj_in.verify_key, 'pkcs7').decrypt_aes),
                'full_name': obj_in.full_name,
                'create_time': datetime.today(),
                'update_time': datetime.today(),
                'roles': ['admin'],
                'is_activate': False,
                'is_superuser': False
            }
            insert_res = await db[self.mdb][self.collection].insert_one(set_params)
            return insert_res

    async def update(
        self, db: AsyncIOMotorClient, db_obj: dict, obj_in: dict
    ) -> UserInDB:
        return db[self.mdb][self.collection].update_one(db_obj, {'$set': obj_in})

    async def authenticate(self, db: AsyncIOMotorClient, login_data: UserLogin):
        md5_password = login_data.password
        password = DeAesCrypt(md5_password, login_data.verify_key, 'pkcs7').decrypt_aes
        if not password:
            return None
        user_info = await self.get_by_username(db, username=login_data.username)
        if not user_info:
            return None
        if not verify_password(password, user_info['password']):
            return None
        return user_info

    async def is_active(self, user_info):
        if user_info['is_activate'] or user_info['is_activate'] == 1:
            return True
        else:
            return False


user = CRUDUser()
