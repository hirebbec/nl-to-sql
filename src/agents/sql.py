from llm.llm import get_llm
from langchain.agents import create_agent

from promt.sql import system_prompt
from tools.get_ddl import get_ddl


def create_sql_agent():
    return create_agent(
        model=get_llm(),
        tools=[get_ddl],
        system_prompt=system_prompt,
    )
