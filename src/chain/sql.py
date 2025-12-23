from llm.llm import get_llm
from promt.sql import system_prompt


def generate_sql(question: str) -> str:
    llm = get_llm()

    response = llm.invoke([system_prompt, question])

    return response.content
