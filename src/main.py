from agent.sql import generate_sql

if __name__ == "__main__":
    question = input("Введите вопрос: ")
    print(generate_sql(question))
