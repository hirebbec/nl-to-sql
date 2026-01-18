from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.db import DBRepository


class DBProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def provide_repository(
        self,
        session: AsyncSession,
    ) -> DBRepository:
        return DBRepository(session)

    @provide
    def provide_db_service(
        self,
        repository: DBRepository,
    ) -> DBService:
        return DBService(repository)
