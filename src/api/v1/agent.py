import uuid

from fastapi import APIRouter, status
from agents.sql_agent import create_sql_agent
from core.container import container
from promts.sql import SYSTEM_PROMPT

router = APIRouter(prefix="/agent", tags=["Agent"])


@router.post("/", status_code=status.HTTP_200_OK)
async def generate_sql(prompt: str) -> dict[str, str]:
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
