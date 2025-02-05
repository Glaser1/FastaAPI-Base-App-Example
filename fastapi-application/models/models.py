from sqlalchemy.orm import declared_attr, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import MetaData

from config import settings
from models.mixins import IdIntPkMixin


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=settings.db.naming_convention)

    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"


class User(IdIntPkMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)
