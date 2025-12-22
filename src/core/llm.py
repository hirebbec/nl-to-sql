from gigachat import GigaChat
from langchain. agents import create_agent
from config import settings
from tool.ddl import get_db_ddl

llm = create_agent(model=GigaChat(
    credentials=settings().API_KEY,
    temperature=settings().TEMPERATURE,
    max_tokens=settings().MAX_TOKENS,
    verify_ssl_certs=False,
), tools=[get_db_ddl])