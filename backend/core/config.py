import secrets
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    # SECRET_KEY: str = secrets.token_urlsafe(32)
    SECRET_KEY = 'N9sbUevTrCkfIWC50PDdyIwJoqHYLq7+duQ9rRdBogTgA/T/9TeDglzDBRrHExROgzvIe4WFPMajNyOn2iEBBA=='
    ALGORITHM = 'HS256'
    # 60 minutes * 24 hours * 7 days = 7 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 1
    SERVER_NAME: str = 'automation-server'
    SERVER_HOST: AnyHttpUrl = 'http://0.0.0.0:8888'
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    # BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ['*']

    PROJECT_NAME: str = 'automationPlat'

    MAX_CONNECTIONS_COUNT = 50
    MIN_CONNECTIONS_COUNT = 10
    MONGO_USER = 'root'
    MONGO_PWD = '123456'
    MONGO_HOST = '192.168.1.6'
    MONGO_PORT = 27017
    MONGO_DB = 'admin'
    MONGO_DB_B = 'automation-data'
    MONGO_DB_T = 'test-data'
    MONGO_authMECHANISM = 'DEFAULT'
    MONGODB_URL = f"mongodb://{MONGO_USER}:{MONGO_PWD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"


settings = Settings()

