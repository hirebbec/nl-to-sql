from chain.sql import generate_sql


def run_agent(question: str):
    return generate_sql(question)
