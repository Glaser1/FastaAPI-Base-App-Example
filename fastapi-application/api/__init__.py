from fastapi import APIRouter

from config import settings
from api.api_v1 import router as api_v1_router

router = APIRouter(prefix=settings.api.prefix)
router.include_router(api_v1_router)
