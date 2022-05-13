import psycopg2
import config

try:

    connection = psycopg2.connect(user=config.user,
                                password=config.password,
                                host=config.host,
                                port=config.port,
                                database=config.database)
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(config.imp)
    cursor.execute(config.export)





except Exception as error:
    print("Ошибка при работе с PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")