from typing import Any

from fastapi import APIRouter, Depends
from db.session import mongo_l
import crud
import schemas


router = APIRouter()


@router.post("/suite_list")
async def query_suite_list(data: schemas.SuiteQuery, db=Depends(mongo_l)) -> Any:
    res = await crud.test_manage.query_suite(db, data)
    if not res:
        return {'code': 40004, 'message': '获取测试计划失败!'}
    return {'code': 20000, 'message': 'ok', 'data': {'list': res[0], 'total': res[1]}}


@router.post("/create_suite")
async def _create(data: schemas.SuiteCreate, db=Depends(mongo_l)) -> Any:
    res = await crud.test_manage.create_suite(db, data)
    if not res:
        return {'code': 40004, 'message': '创建测试计划失败!'}
    return {'code': 20000, 'message': 'ok'}


@router.post("/update_suite")
async def _update(data: schemas.SuiteUpdate, db=Depends(mongo_l)) -> Any:
    res = await crud.test_manage.update_suite(db, data)
    if not res:
        return {'code': 40004, 'message': '更新测试计划失败!'}
    return {'code': 20000, 'message': 'ok'}


@router.post("/insert_suite_items")
async def _insert_items(data: schemas.InsertSuiteItems, db=Depends(mongo_l)) -> Any:
    res = await crud.test_manage.insert_suite_items(db, data)
    if not res:
        return {'code': 40004, 'message': '配置测试集合失败!'}
    return {'code': 20000, 'message': 'ok'}


@router.get("/get_items")
async def _get_items(p_key: str, db=Depends(mongo_l)) -> Any:
    res = await crud.test_manage.get_suite_items(db, p_key)
    if not res:
        return {'code': 40004, 'message': '测试集合未配置或者存在过期用例!'}
    return {'code': 20000, 'message': 'ok', 'data': res}


@router.get("/get_diff_items")
async def _get_d_items(p_key: str, db=Depends(mongo_l)) -> Any:
    res = await crud.test_manage.get_diff_items(db, p_key)
    if not res:
        return {'code': 40004, 'message': '测试集合未配置或者存在过期用例!'}
    return {'code': 20000, 'message': 'ok', 'data': res}


@router.post("/get_pool")
async def _get_poll(data: schemas.QueryNINPool, db=Depends(mongo_l)) -> Any:
    res = await crud.test_manage.get_case_items_for_insert(db, data)
    if not res:
        return {'code': 40004, 'message': '获取用例池失败!'}
    return {'code': 20000, 'message': 'ok', 'data': res}


@router.delete("/delete_suite")
async def _delete(p_key: str, db=Depends(mongo_l)) -> Any:
    res = await crud.test_manage.delete_suite(db, p_key)
    if not res:
        return {'code': 40004, 'message': '删除测试计划失败!'}
    return {'code': 20000, 'message': 'ok'}
