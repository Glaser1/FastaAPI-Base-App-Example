from typing import Sequence

from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from models.models import User
from models.db_helper import db_helper
from api.api_v1.schemas import UserRead, UserCreate

router = APIRouter(prefix=settings.api.v1.users, tags=["Users"])


@router.get("/", response_model=list[UserRead])
async def get_users(session: AsyncSession = Depends(db_helper.get_db)) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await session.scalars(stmt)
    return result.all()


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_post(user_create: UserCreate, session: AsyncSession = Depends(db_helper.get_db)) -> User:
    user = User(**user_create.model_dump())
    session.add(user)
    await session.commit()
    return user
