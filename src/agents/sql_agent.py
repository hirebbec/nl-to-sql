from llms.giga_chat import get_llm
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

from tools.execute_sql import execute_sql
from tools.get_ddl import get_table_schemas
from tools.get_tables import get_tables


def create_sql_agent():
    return create_react_agent(
        model=get_llm(),
        tools=[get_tables, get_table_schemas, execute_sql],
        checkpointer=InMemorySaver(),
    )
