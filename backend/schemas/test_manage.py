from typing import List
from pydantic import BaseModel


class CaseQuery(BaseModel):
    page: int
    limit: int
    module_name: str = None
    file_name: str = None
    author: str = None
    status: str = None
    sort: str


class UpdateCaseInfo(BaseModel):
    id: int
    update_time: str
    module_name: str
    file_name: str
    file_path: str
    author: str
    version: str
    status: str


class UpdateCaseStatus(BaseModel):
    id: int
    status: str


