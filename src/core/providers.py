from dishka import Provider, provide, Scope
from langchain_gigachat import GigaChat
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from db.session import get_session
from services.db import DBService
from db.repositories.db import DBRepository

class DBProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def provide_session(self):
        async for session in get_session(settings().postgres_dsn):
            yield session

class AppProvider(Provider):
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

