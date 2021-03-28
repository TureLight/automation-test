from typing import List
from pydantic import BaseModel


class QueryTask(BaseModel):
    page: int
    limit: int
    task_name: str = None
    sort: str


class UpdateTask(BaseModel):
    id: int
    task_name: str
    suite_name: str
    operator: str
    version: str
    status: str


class OperatorTask(BaseModel):
    id: int
    status: str
