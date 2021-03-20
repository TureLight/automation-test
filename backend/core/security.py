import binascii

from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext

from core.config import settings

import base64
import hashlib
from Crypto.Cipher import AES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    """
    根据设定的时间生成令牌
    :param subject: 要加密的对象
    :param expires_delta: 令牌时限
    :return: 加密字符串
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证两组密码
    :param plain_password: 原始密码
    :param hashed_password: 哈希密码
    :return:
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    获取密码的哈希
    :param password: 密码
    :return:
    """
    return pwd_context.hash(password)


class DeAesCrypt:
    """
    AES-128-CBC解密
    """

    def __init__(self, data, key, pad):
        """
        :param data: 加密后的字符串
        :param key: 随机的16位字符
        :param pad: 填充方式
        """
        self.key = key
        self.data = data
        self.pad = pad.lower()

        hash_obj = hashlib.md5()  # 构造md5对象
        hash_obj.update(key.encode("utf-8"))  # 进行md5加密,md5只能对byte类型进行加密
        res_md5 = hash_obj.hexdigest()  # 获取加密后的字符串数据
        self.iv = res_md5[:16].encode("utf-8")

    @property
    def decrypt_aes(self):
        """AES-128-CBC解密"""
        try:
            real_data = base64.b64decode(self.data)
            my_aes = AES.new(self.key.encode("utf-8"), AES.MODE_CBC, self.iv)

            decrypt_data = my_aes.decrypt(real_data)
            return self.get_str(decrypt_data)
        except binascii.Error:
            return None

    def get_str(self, bd):
        """解密后的数据去除加密前添加的数据"""
        if self.pad == "zero":  # 去掉数据在转化前不足16位长度时添加的ASCII码为0编号的二进制字符
            return ''.join([chr(i) for i in bd if i != 0])

        elif self.pad == "pkcs7":  # 去掉pkcs7模式中添加后面的字符
            return ''.join([chr(i) for i in bd if i > 32])
        else:
            return "不存在此种数据填充方式"
