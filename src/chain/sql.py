from langchain_core.messages import HumanMessage
from core.llm import llm
from core.promts import system_prompt

def generate_sql(question: str):
    return llm.invoke([
        system_prompt,
        HumanMessage(content=question)
    ])