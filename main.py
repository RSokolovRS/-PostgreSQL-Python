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
# add_cust = add_customer(connect, 'Andry','Sokolov')

# Функция удаления данных из таблицы.
# def delete_data(connect, name1: str, name2: str)->int:
#     with connect.cursor() as cur:
#         try:
#             cur.execute("""DELETE FROM customers 
#                         WHERE customer_id IN (SELECT customer_id FROM customers 
#                         WHERE first_name  LIKE %s 
#                         AND last_name LIKE %s );""",(name1, name2))
#             connect.commit()
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
#         print(res)
#         for id in res:
#             for i in id:
#                 with connect.cursor() as cur:
#                     cur.execute(""" INSERT INTO phone_numbers(number, customer_id)
#                                         VALUES (%s, %s);""", ( phon_num, i,))
#                     print('Успешно')
#                     connect.commit()

# insert = insert_table(connect, 'Andry','Sokolov', 79208855989)

# 4. Функция, позволяющая изменить данные о клиенте.
# def update(connect, sql_query, old_name1, new_name1):
#     twoname = (old_name1, new_name1)
#     print(type(twoname)) # передовать в sql- запрос %s только кортеж.
#     with connect.cursor() as cur:
#         try:
#             cur.execute(sql_query,(twoname))
#             connect.commit()
#             print(f'Внесены изменения:{old_name1} на {new_name1}')
#         except:
#             print(f'Error')
       

# sql_query = ("""UPDATE customers SET first_name =%s WHERE first_name =%s;""")
# update(connect, sql_query, 'Andry', 'Roman')

# 5. Функция, позволяющая удалить телефон для существующего клиента.
# def delete(connect, sql_query_delete, f_name, l_name):
#     twoname = (f_name, l_name)
#     with connect.cursor() as cur:
#         try:
#             cur.execute(sql_query_delete,(twoname))
#             connect.commit()
#             print('Номер телефона удален успешно.')
#         except:
#             print('Error')

# sql_query_delete = """DELETE FROM phone_numbers pn WHERE pn.customer_id = (
#                 SELECT c.customer_id FROM customers c WHERE first_name 
#                 LIKE %s AND last_name LIKE %s);"""

# del_phone = delete(connect, sql_query_delete, 'Andry', 'Sokolov')

# 6. Функция, позволяющая удалить существующего клиента.
# def delete_cust(connect, sql_query_del_cust, fname, lname ):
#     two_names = fname, lname
#     with connect.cursor() as cur:
#         try:
#             cur.execute(sql_query_del_cust, (two_names))
#             connect.commit()
#             print(f'Клиент {two_names} удален!')
#         except:
#             print('Error')


# sql_query_del_cust = (""" DELETE FROM customers WHERE first_name LIKE %s
#                         AND last_name LIKE %s;""")

# delete_cust(connect, sql_query_del_cust, 'Andry', 'Sokolov')




        


   
