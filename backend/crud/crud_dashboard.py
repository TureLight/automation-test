import redis
from bson import ObjectId, Int64
from typing import Any, Dict, Optional, Union
from datetime import datetime
from db.session import AsyncIOMotorClient
from db.session import redis_pool
from loguru import logger


class CrudDashboard:

    mdb = 'automation_data'
    collection = 'dashboard_data'

    async def get_dashboard_data(self, db: AsyncIOMotorClient, query_params: str):
        mongo_params = {'key_words': query_params}
        redis_c = redis.Redis(connection_pool=redis_pool)
        redis_query_key = redis_c.get(query_params)
        if redis_query_key:
            # logger.debug(redis_c.hgetall(redis_query_key))
            return redis_c.hgetall(redis_query_key)
        else:
            res = await db[self.mdb][self.collection].find_one(mongo_params)
            if not res:
                return None
            redis_c.set(query_params, str(res['_id']), 60)
            redis_c.delete(str(res['_id']))
            redis_c.hmset(name=str(res['_id']), mapping=res['data_body'])
            return res['data_body']

    async def get_dashboard_data_no_redis(self, db: AsyncIOMotorClient, query_params: str):
        mongo_params = {'key_words': query_params}
        res = await db[self.mdb][self.collection].find_one(mongo_params)
        if not res:
            return None
        return res['data_body']


dashboard = CrudDashboard()
