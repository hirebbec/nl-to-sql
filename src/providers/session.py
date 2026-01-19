from typing import AsyncIterator

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from db.session import get_session


class DBSessionProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def provide_session(self) -> AsyncIterator[AsyncSession]:
        async for session in get_session(settings().postgres_dsn):
            yield session
