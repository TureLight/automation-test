import pymongo
import redis

from loguru import logger

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

from motor.motor_asyncio import AsyncIOMotorClient


engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

redis_pool = redis.ConnectionPool(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT,
                                  password=settings.REDIS_PASSWORD,
                                  decode_responses=True
                                  )


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.client


async def connect_to_mongo():
    logger.info("连接数据库中...")
    db.client = AsyncIOMotorClient(str(settings.MONGODB_URL),
                                   maxPoolSize=settings.MAX_CONNECTIONS_COUNT,
                                   minPoolSize=settings.MIN_CONNECTIONS_COUNT
                                   )
    logger.info("连接数据库成功！")


async def close_mongo_connection():
    logger.info("关闭数据库连接...")
    db.client.close()
    logger.info("数据库连接关闭！")


class AsyncMongoLink:

    def __init__(self):
        self.client = AsyncIOMotorClient(str(settings.MONGODB_URL),
                                         maxPoolSize=settings.MAX_CONNECTIONS_COUNT,
                                         minPoolSize=settings.MIN_CONNECTIONS_COUNT
                                         )

    @property
    def automation(self):
        return self.client[settings.MONGO_DB_B]

    @property
    def user(self):
        return self.automation['user_info']

    @property
    def task(self):
        return self.automation['task_info']

    @property
    def test_manage(self):
        return self.automation['test_manage_data']


class MongoLink:

    def __init__(self):
        self.client = pymongo.MongoClient(host=settings.MONGO_HOST,
                                          port=settings.MONGO_PORT,
                                          username=settings.MONGO_USER,
                                          password=settings.MONGO_PWD,
                                          # authSource='admin',
                                          authMechanism=settings.MONGO_authMECHANISM
                                          )

    @property
    def automation(self):
        return self.client[settings.MONGO_DB_B]

    @property
    def user(self):
        return self.automation['user_info']

    @property
    def task(self):
        return self.automation['task_info']

    @property
    def test_manage(self):
        return self.automation['test_manage_data']


globals_link = MongoLink()


def mongo_l():
    return globals_link
