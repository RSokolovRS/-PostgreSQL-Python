# pip install psycopg2-binary	- Установка библиотеки.
# createdb -U postgres CustomersDB - создание БД через терминал.
# пароль от postgres.
# psql -U postgres -d CustomersDB - подключение к БД через терминал.
# import psycopg2 
import psycopg2 
def create_connection(nameDB, userDB, passwordDB):
    connection = None
    try: # Обработка ошибок в виде исключений.
        connection = psycopg2.connect(
            database=nameDB, 
            user=userDB,
            password=passwordDB)
        print(f'Удачное подключение к {nameDB}')
    except ConnectionError as CE:
        print(f'Ошибка подключения {CE}')
    return connection

connect = create_connection('CustomersDB', 'postgres', '05121978')

#2. Функция, позволяющая добавить нового клиента.
# def add_customer(connect,  name_1: str, name_2: str)->int: # специальный объект typing.Any, принимает разные значения:
#     with connect.cursor() as cur:
#         try:
#             cur.execute("""INSERT INTO Customers(first_name, last_name) VALUES
#             (%s, %s);""", (name_1, name_2,))
#             connect.commit()
#             print('Данные успешно добавлены!')
#         except:
#             print('Ошибка')
#         finally:
#             connect.commit()
# add_cust = add_customer(connect, 'Andry','Name')

# Функция удаления данных.
# def delete_data(connect, name1: str, name2: str)->int:
#     with connect.cursor() as cur:
#         try:
#             cur.execute("""DELETE FROM customers 
#                         WHERE customer_id in (select customer_id from customers 
#                         WHERE first_name  LIKE %s 
#                         AND last_name LIKE %s );""",(name1, name2))
#             print('Данные успешно удалены!')
#         except:
#             print('Ошибка')
#         finally:
#             connect.commit()
# delete_data(connect, 'Roman', 'Sokolov')

# 3. Функция, позволяющая добавить телефон для существующего клиента.
# def insert_table(connect,  name_1, name_2, phon_num ): 
#     with connect.cursor() as cur:
#         cur.execute("""SELECT customer_id FROM customers c 
#                         WHERE customer_id IN (SELECT customer_id FROM customers 
#                         WHERE first_name LIKE %s AND last_name  LIKE %s);""",
#                         (name_1, name_2, ))
#         res = cur.fetchall()
#         for id in res:
#             for i in id:
#                 with connect.cursor() as cur:
#                     cur.execute(""" INSERT INTO phone_numbers(number, customer_id)
#                                         VALUES (%s, %s);""", ( phon_num, i,))
#                     print('Успешно')
#                     connect.commit()

# insert = insert_table(connect, 'Roman','Sokolov', +79208855989)

# 4. Функция, позволяющая изменить данные о клиенте.
def update(connect, )
    with connect.cursor() as cur:
        cur.execute()
   
