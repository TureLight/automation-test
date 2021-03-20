from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    code: str
    data: dict


class NormalResponse(BaseModel):
    code: int
    msg: str


class Register(BaseModel):
    code: int
    message: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None
