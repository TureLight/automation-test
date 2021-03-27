from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from db.session import mongo_l
import crud
import schemas


router = APIRouter()


@router.post("/case_list")
async def query_case_list_data(data: schemas.CaseQuery, db=Depends(mongo_l)) -> Any:
    res = await crud.test_manage.get_case_info_list(db, data)
    if not res:
        return {'code': 40004, 'message': '获取用例信息失败!'}
    return {'code': 20000, 'message': 'ok', 'data': {'list': res[0], 'total': res[1]}}


@router.post("/create_case_info")
async def create_info(data: schemas.UpdateCaseInfo, db=Depends(mongo_l)) -> Any:
    res = await crud.test_manage.create_case(db, data)
    if not res:
        return {'code': 40004, 'message': '创建用例信息失败!'}
    return {'code': 20000, 'message': 'ok'}


@router.post("/update_case_info")
async def update_info(data: schemas.UpdateCaseInfo, db=Depends(mongo_l)) -> Any:
    res = await crud.test_manage.update_case_info(db, data)
    if not res:
        return {'code': 40004, 'message': '更新用例信息失败!'}
    return {'code': 20000, 'message': 'ok'}


@router.post("/update_case_status")
async def update_status(data: schemas.UpdateCaseStatus, db=Depends(mongo_l)) -> Any:
    res = await crud.test_manage.update_case_status(db, data)
    if not res:
        return {'code': 40004, 'message': '更新用例状态失败!'}
    return {'code': 20000, 'message': 'ok'}


@router.delete("/delete_case_info")
async def delete_info(id: int, db=Depends(mongo_l)) -> Any:
    res = await crud.test_manage.delete_case_info(db, id)
    if not res:
        return {'code': 40004, 'message': '删除用例信息失败!'}
    return {'code': 20000, 'message': 'ok'}
