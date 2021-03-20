from typing import Any, Dict, Optional, Union
from fastapi import Depends, HTTPException, status
from datetime import datetime
from core.security import get_password_hash, verify_password, DeAesCrypt
from schemas.user import UserCreate, UserUpdate, UserInDB, UserBase, UserLogin
from db.session import AsyncIOMotorClient
from loguru import logger


class CRUDUser:

    db = 'automation-data'
    collection = 'user-info'

    async def get_by_username(self, db: AsyncIOMotorClient, username: str):
        query_params = {'username': username}
        res = await db[self.db][self.collection].find_one(query_params)
        return res

    async def create(self, db: AsyncIOMotorClient, obj_in: UserCreate):
        user_info = await db[self.db][self.collection].find_one({'username': obj_in.username})
        logger.debug(user_info)
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
            insert_res = await db[self.db][self.collection].insert_one(set_params)
            return insert_res

    async def update(
        self, db: AsyncIOMotorClient, db_obj: dict, obj_in: dict
    ) -> UserInDB:
        return db[self.db][self.collection].update_one(db_obj, {'$set': obj_in})

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
        # logger.debug(user_info)
        if not user_info['is_activate']:
            return None
        return user_info


user = CRUDUser()
