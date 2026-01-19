from dishka import make_async_container

from providers.service import DBProvider
from providers.session import DBSessionProvider

container = make_async_container(DBSessionProvider(), DBProvider())
