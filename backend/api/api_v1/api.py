from fastapi import APIRouter, Depends, Header, HTTPException

from api.api_v1.endpoints import login, dashboard, test_management
from db.session import mongo_l, get_database
from api.deps import get_current_user
api_router = APIRouter()


async def check_token(X_Token: str = Header(...), db=Depends(get_database)):
    check_res = await get_current_user(db, X_Token)
    if not check_res:
        raise HTTPException(status_code=400, detail="令牌过期!")

api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(dashboard.router,
                          prefix="/dashboard",
                          tags=["dashboard"],
                          dependencies=[Depends(check_token)]
                          )
api_router.include_router(test_management.router,
                          prefix="/test_management",
                          tags=["utils"],
                          dependencies=[Depends(check_token)]
                          )


# api_router.include_router(items.router, prefix="/items", tags=["items"])
