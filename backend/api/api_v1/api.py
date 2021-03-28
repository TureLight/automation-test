from fastapi import APIRouter, Depends, Header, HTTPException

from api.api_v1.endpoints import login, dashboard
from api.api_v1.endpoints.test_manage import test_management, test_suite
from api.api_v1.endpoints.task_manage import task_schedule
from db.session import get_database
from api.deps import get_current_user
api_router = APIRouter()


async def check_token(X_Token: str = Header(...), db=Depends(get_database)):
    check_res = await get_current_user(db, X_Token)
    if not check_res:
        raise HTTPException(status_code=400, detail="令牌过期!")

api_router.include_router(login.router, prefix="/login", tags=["登录相关"])
api_router.include_router(dashboard.router,
                          prefix="/dashboard",
                          tags=["首页"],
                          dependencies=[Depends(check_token)]
                          )
api_router.include_router(test_management.router,
                          prefix="/test_management",
                          tags=["测试用例"],
                          dependencies=[Depends(check_token)]
                          )
api_router.include_router(test_suite.router,
                          prefix="/test_project",
                          tags=["测试计划"],
                          dependencies=[Depends(check_token)]
                          )

api_router.include_router(task_schedule.router,
                          prefix="/task_schedule",
                          tags=["任务调度"],
                          dependencies=[Depends(check_token)]
                          )
