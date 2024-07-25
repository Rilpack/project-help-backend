from fastapi import APIRouter

from .organizatios.views import router as organizations_router

router = APIRouter()
router.include_router(router=organizations_router, prefix="/organizations")
