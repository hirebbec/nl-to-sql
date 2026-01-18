from dishka import Provider, Scope, provide
from gigachat import GigaChat

from core.config import settings


class LLLmProvider(Provider):
    scope = Scope.APP

    @provide
    def provide_llm(self) -> GigaChat:
        return GigaChat(
            credentials=settings().API_KEY,
            temperature=settings().TEMPERATURE,
            max_tokens=settings().MAX_TOKENS,
            verify_ssl_certs=False,
        )
