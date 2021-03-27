from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
import time
import crud
import models
import schemas
from core import security
from core.config import settings
from db.session import AsyncIOMotorClient, SessionLocal

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def get_current_user(
    db: AsyncIOMotorClient, token: str = Depends(reusable_oauth2)
):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        if payload['exp'] - time.time() > 0:
            user = await crud.user.get_user_info(db, username=payload['sub'])
            if not user:
                raise HTTPException(status_code=400, detail="账号信息错误!")
            return user
        else:
            raise HTTPException(status_code=400, detail="令牌过期!")
    except (jwt.JWTError, ValidationError):
        raise HTTPException(status_code=400, detail="令牌过期!")


async def get_current_active_user(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not await crud.user.is_active(current_user):
        raise HTTPException(status_code=400, detail="账号被冻结!")
    return current_user


async def get_current_active_superuser(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not await crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="账号没有足够的权限!"
        )
    return current_user
