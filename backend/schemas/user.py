from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    username: str


class UserInfo(UserBase):
    full_name: str


class GetUserInfo(BaseModel):
    token: str


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str
    verify_key: str
    full_name: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password_old: str
    password_new: str
    verify_key: str


# Properties to receive via API on update
class UserLogin(UserBase):
    password: str
    verify_key: str


# Additional properties stored in DB
class UserInDBBase(UserBase):
    hashed_password: str


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
    is_activate: bool
    is_superuser: bool
    create_time: str
    update_time: str

