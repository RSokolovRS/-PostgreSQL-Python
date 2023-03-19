# pip install psycopg2-binary	- Установка библиотеки.
# createdb -U postgres CustomersDB - создание БД через терминал.
# пароль от postgres.
# psql -U postgres -d CustomersDB - подключение к БД через терминал.
# import psycopg2 
# conn = psycopg2.connect(database='CustomersDB' , user='postgres' , password='05121978')
# with conn.cursor() as cur:  
#         cur.execute("""CREATE TABLE IF NOT EXISTS Customers(
#         customer_id SERIAL PRIMARY KEY,
#         first_name VARCHAR(40) NOT NULL,
#         last_name VARCHAR(100) NOT NULL);""")
#         cur.execute("""CREATE TABLE IF NOT EXISTS Email(
# 	Email_id SERIAL PRIMARY KEY,
# 	Email VARCHAR(120) NOT NULL,
# 	customer_id INTEGER NOT NULL REFERENCES Customers(customer_id));""")
#         cur.execute("""CREATE TABLE IF NOT EXISTS Phone_numbers(
# 	number_id SERIAL PRIMARY KEY,
# 	number INTEGER NOT NULL UNIQUE,
# 	customer_id INTEGER NOT NULL REFERENCES Customers(customer_id));""")
# conn.commit() # применить все опрерации выше, зафиксировать БД.
# conn.close() # Закрыть соединение.

# conn = psycopg2.connect(database='CustomersDB' , user='postgres' , password='05121978')
# with conn.cursor() as cur:
#         cur.execute("""DROP TABLE Phone_numbers""") # Удаление таблицЫ.
# conn.commit() # применить все опрерации выше, зафиксировать БД.
# conn.close() # Закрыть соединение.

import psycopg2 
conn = psycopg2.connect(database='CustomersDB' , user='postgres' , password='05121978')
with conn.cursor() as cur:
        name1 = input('Введите Имя клиента.')
        name2 = input('Введите Фамилию клиента.')  
        def add_customer():
                cur.execute("""INSERT INTO Customers(first_name, last_name) VALUES
                (%s, %s), name1, name2);""")
        print(cur.fetchall())
conn.commit() 
conn.close()

