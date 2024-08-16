from fastapi import APIRouter

from .questions.views import router as questions_router
from .choices.views import router as choices_router

router = APIRouter()
router.include_router(router=questions_router, prefix="/questions")
router.include_router(router=choices_router, prefix="/choices")
