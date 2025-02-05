from fastapi import APIRouter

from config import settings
from api.api_v1.views import router as users_router

router = APIRouter(prefix=settings.api.v1.prefix)
router.include_router(users_router)
