from dishka import AsyncContainer

from llms.giga_chat import get_llm
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

from tools.execute_sql import make_execute_sql_tool
from tools.get_table_schemas import make_get_table_schemas_tool
from tools.get_tables import make_get_tables_tool


def create_sql_agent(container: AsyncContainer):
    return create_react_agent(
        model=get_llm(),
        tools=[
            make_get_tables_tool(container),
            make_get_table_schemas_tool(container),
            make_execute_sql_tool(container),
        ],
        checkpointer=InMemorySaver(),
    )
