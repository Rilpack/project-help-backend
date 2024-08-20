from fastapi import APIRouter

from .users.views import router as users_router
from .auth.views import router as auth_router
from .organizations.views import router as organizations_router

router = APIRouter()
router.include_router(router=auth_router, prefix="/auth")
router.include_router(router=users_router, prefix="/users")
router.include_router(router=organizations_router, prefix="/organizations")
