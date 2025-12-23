from chain.sql import generate_sql

def nl_to_sql(question: str) -> str:
    sql = generate_sql(question)
    return sql
