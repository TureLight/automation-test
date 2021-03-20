from datetime import timedelta
from typing import Any, List
from loguru import logger
from fastapi import APIRouter, Body, Depends, HTTPException, Header
# from bson.objectid import ObjectId
from fastapi.security import OAuth2PasswordRequestForm
from motor.motor_asyncio import AsyncIOMotorClient
import crud
import models
import schemas
from api import deps
from core import security
from core.config import settings
from core.security import get_password_hash
from utils import (
    generate_password_reset_token,
    send_reset_password_email,
    verify_password_reset_token,
)
from db.session import mongo_l, get_database

router = APIRouter()


@router.post("/login/access-token")
async def login_access_token(
    form_data: schemas.UserLogin, db: AsyncIOMotorClient = Depends(get_database)
) -> Any:
    """
    登录接口
    :param form_data:
    :param db:
    :return: {code: int, data: {'access_token':xxx, "name": xxx}, 'message':xxx}
    """
    user = await crud.user.authenticate(
        db, login_data=form_data
    )
    if not user:
        return {'code': 50000, 'message': '账号或者密码错误!'}
    elif not await crud.user.is_active(user):
        return {'code': 50004, 'message': '账号冻结,请联系管理员激活账号!'}
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "code": 20000,
        "data": {
            "access_token": security.create_access_token(
                user['username'], expires_delta=access_token_expires
            ),
            "name": user['full_name']
        },
        'message': '登陆成功!'
    }


@router.get("/login/user_info")
async def get_user_info(
    token: str, db: AsyncIOMotorClient = Depends(get_database)
) -> Any:
    """
    获取用户信息
    :param token:
    :param db:
    :return: {
                roles: ['admin'],
                introduction: 'I am a super administrator',
                avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
                name: 'Super Admin'
              }
    """
    user = await deps.get_current_user(db=db, token=token)
    logger.debug(user)
    if not user:
        return {'code': 50008, 'message': '账号信息过期或者存在异常,请重新登录!'}
    elif not await crud.user.is_active(user):
        return {'code': 50004, 'message': '账号冻结,请联系管理员激活账号!'}
    # access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "code": 20000,
        "data": {
            "roles": ['admin'],
            "name": user['full_name'],
            "uid": str(user['_id']),
            "avatar": 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            'introduction': '默认返回一个管理员权限',
        }
    }


@router.post("/login/logout", response_model=schemas.Register)
async def user_logout(x_token: List[str] = Header(None)) -> Any:
    print(x_token)
    # TODO 这里配置一个销毁方法,暂时把token放到临时表中,如果下次有这个token登录则阻拦
    return {'code': 20000, 'message': '退出成功!'}


@router.post("/login/register", response_model=schemas.Register)
async def user_register(
    form_data: schemas.UserCreate, db=Depends(get_database)
) -> Any:
    """
    用户注册
    """
    user = await crud.user.create(
        db, obj_in=form_data
    )
    logger.debug(f'注册接口 user: {user}')
    if not user:
        return {'code': 50000, 'message': '用户名已占用,注册失败!'}
    return {'code': 20000, 'message': '注册账号成功,请联系管理员激活账号!'}


@router.post("/password-recovery/{email}", response_model=schemas.Msg)
def recover_password(email: str, db: AsyncIOMotorClient = Depends(get_database)) -> Any:
    """
    Password Recovery
    """
    user = crud.user.get_by_email(db, email=email)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="用户不存在!",
        )
    password_reset_token = generate_password_reset_token(email=email)
    send_reset_password_email(
        email_to=user.email, email=email, token=password_reset_token
    )
    return {"msg": "确认邮件已发出!"}


@router.post("/reset-password/", response_model=schemas.Msg)
def reset_password(
    db: AsyncIOMotorClient = Depends(get_database),
    token: str = Body(...),
    new_password: str = Body(...),
) -> Any:
    """
    Reset password
    """
    email = verify_password_reset_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = crud.user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="用户不存在!",
        )
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    hashed_password = get_password_hash(new_password)
    user.hashed_password = hashed_password
    # TODO: 暂时没需求
    return {"msg": "密码更新成功!"}
