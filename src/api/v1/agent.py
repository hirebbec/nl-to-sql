import uuid

from fastapi import APIRouter, Depends, status
from agents import sql_agent
from agents.sql_agent import create_sql_agent
from promts.sql import SYSTEM_PROMPT

router = APIRouter(prefix="/agent", tags=["Agent"])


@router.post("/", status_code=status.HTTP_200_OK)
async def generate_sql(prompt: str) -> dict[str, str]:
    agent = create_sql_agent()

    result = await agent.ainvoke(
        {
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ]
        },
        config={"configurable": {"thread_id": uuid.uuid4().hex}},
    )

    print(result)

    return result
