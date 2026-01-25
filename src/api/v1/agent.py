import uuid

from fastapi import APIRouter, status

from agents.sql.agent import create_sql_agent
from agents.sql.graph import create_sql_graph
from agents.sql.state import SQLAgentState
from core.container import container
from llms.giga_chat import get_llm
from promts.sql import SYSTEM_PROMPT

router = APIRouter(prefix="/agent", tags=["Agent"])


@router.post("/langgraph", status_code=status.HTTP_200_OK)
async def generate_sql_langgraph(prompt: str):
    async with container() as request_container:
        graph = create_sql_graph(request_container, get_llm())

        result = await graph.ainvoke(SQLAgentState(user_prompt=prompt))

        return {
            "sql": result["sql_query"],
            "result": result["sql_result"],
        }


@router.post("/langchain", status_code=status.HTTP_200_OK)
async def generate_sql_langchain(prompt: str) -> dict[str, str]:
    async with container() as request_container:
        agent = create_sql_agent(request_container)
        result = await agent.ainvoke(
            {
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ]
            },
            config={
                "configurable": {"thread_id": uuid.uuid4().hex},
                "recursion_limit": 10,
                "debug": True,
            },
        )
        print(result)

        final_message = result["messages"][-1]

        return {"result": final_message.content}
