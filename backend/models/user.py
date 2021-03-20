from pydantic import BaseModel
from bson.objectid import ObjectId


class User(BaseModel):

    _id: ObjectId
    user_name: str
    hashed_password: str
    is_activate: bool
    is_superuser: bool
    create_time: str
    update_time: str
