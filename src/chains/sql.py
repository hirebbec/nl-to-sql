from llms.giga_chat import get_llm
from promts.sql import system_prompt


def generate_sql(question: str) -> str:
    llm = get_llm()

    response = llm.invoke([system_prompt, question])

    return response.content
