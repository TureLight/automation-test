from typing import Any

from fastapi import APIRouter, Depends
from db.session import mongo_l
import crud
import schemas


router = APIRouter()


@router.post("/task_list")
async def query_task_list(data: schemas.QueryTask, db=Depends(mongo_l)) -> Any:
    res = await crud.task_schedule.task_list(db, data)
    if not res:
        return {'code': 40004, 'message': '获取任务失败!'}
    return {'code': 20000, 'message': 'ok', 'data': {'list': res[0], 'total': res[1]}}


@router.post("/create_task")
async def _create(data: schemas.UpdateTask, db=Depends(mongo_l)) -> Any:
    res = await crud.task_schedule.create_task(db, data)
    if not res:
        return {'code': 40004, 'message': '创建任务失败!'}
    return {'code': 20000, 'message': 'ok'}


@router.post("/update_task")
async def _update(data: schemas.UpdateTask, db=Depends(mongo_l)) -> Any:
    res = await crud.task_schedule.update_task(db, data)
    if not res:
        return {'code': 40004, 'message': '更新任务失败!'}
    return {'code': 20000, 'message': 'ok'}


@router.post("/operator_task")
async def _operator(data: schemas.OperatorTask, db=Depends(mongo_l)) -> Any:
    res = await crud.task_schedule.operator_task(db, data)
    if not res:
        return {'code': 40004, 'message': '操作任务失败!'}
    return {'code': 20000, 'message': 'ok'}


@router.delete("/delete_task")
async def _delete(p_key: str, db=Depends(mongo_l)) -> Any:
    res = await crud.task_schedule.delete_task(db, p_key)
    if not res:
        return {'code': 40004, 'message': '删除测试任务失败!'}
    return {'code': 20000, 'message': 'ok'}


@router.get("/get_suite")
async def _get_suite(db=Depends(mongo_l)) -> Any:
    res = await crud.task_schedule.get_suite(db)
    if not res:
        return {'code': 40004, 'message': '删除测试任务失败!'}
    return {'code': 20000, 'message': 'ok', 'data': res}
