from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException

import crud
import models
import schemas
from api import deps
from db.session import get_database


router = APIRouter()


@router.get("/read_panel_group_data", response_model=schemas.PanelGroupData)
async def read_dashboard_data(query_params: str, db=Depends(get_database)) -> Any:
    res = await crud.dashboard.get_dashboard_data(db, query_params)
    if not res:
        return {'code': 40000, 'message': "获取概览数据失败!"}
    return {'code': 20000, 'message': 'ok', 'data': res}


@router.get("/read_data")
async def read_dashboard_data(query_params: str, db=Depends(get_database)) -> Any:
    res = await crud.dashboard.get_dashboard_data_no_redis(db, query_params)
    if not res:
        return {'code': 40000, 'message': "获取概览数据失败!"}
    return {'code': 20000, 'message': 'ok', 'data': res}


# @router.get("/pie_chart_data", response_model=schemas.PieChartData)
# async def read_items(db=Depends(get_database)) -> Any:
#     res = await crud.dashboard.get_dashboard_data(db)
#     if not res:
#         raise HTTPException(status_code=404, detail="获取概览数据失败!")
#     return {'code': 20000, 'message': 'ok', 'data': res}


# @router.post("/", response_model=schemas.Item)
# def create_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     item_in: schemas.ItemCreate,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Create new item.
#     """
#     item = crud.item.create_with_owner(db=db, obj_in=item_in, owner_id=current_user.id)
#     return item
#
#
# @router.put("/{id}", response_model=schemas.Item)
# def update_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     item_in: schemas.ItemUpdate,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Update an item.
#     """
#     item = crud.item.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     item = crud.item.update(db=db, db_obj=item, obj_in=item_in)
#     return item
#
#
# @router.get("/{id}", response_model=schemas.Item)
# def read_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Get item by ID.
#     """
#     item = crud.item.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     return item
#
#
# @router.delete("/{id}", response_model=schemas.Item)
# def delete_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Delete an item.
#     """
#     item = crud.item.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     item = crud.item.remove(db=db, id=id)
#     return item
