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
    total: int


class UpdateCaseStatus(BaseModel):
    id: int
    status: str


class SuiteQuery(BaseModel):
    page: int
    limit: int
    suite_name: str = None
    tester: str = None
    sort: str


class SuiteUpdate(BaseModel):
    p_key: str
    id: int
    suite_name: str
    tester: str
    version: str
    update_time: str
    total: int = None


class SuiteCreate(BaseModel):
    id: int
    suite_name: str
    tester: str
    version: str
    update_time: str
    total: int = None


class InsertSuiteItems(BaseModel):
    p_key: str
    case_keys: list


class QueryNINPool(BaseModel):
    nin_list: list = None


