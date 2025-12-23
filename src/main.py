from service.sql import nl_to_sql

if __name__ == "__main__":
    prompt = input("Введите вопрос: ")
    print(nl_to_sql(prompt))

