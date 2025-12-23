from langchain_gigachat import GigaChat
from config import settings

def get_llm():
    return GigaChat(
        credentials=settings().API_KEY,
        temperature=settings().TEMPERATURE,
        max_tokens=settings().MAX_TOKENS,
        verify_ssl_certs=False,
    )