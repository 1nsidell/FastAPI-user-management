from typing import Annotated

from fastapi import Depends

from app.repositories.sql.impls.users_repository import UsersSQLRepositoryImpl
from src.app.repositories import UsersSQLRepositoryProtocol


def get_users_sql_repository() -> UsersSQLRepositoryProtocol:
    return UsersSQLRepositoryImpl()


SQLRepository = Annotated[
    UsersSQLRepositoryProtocol, Depends(get_users_sql_repository)
]
