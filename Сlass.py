import psycopg2

def create_db(conn):
    conn
    print(f'Удачное подключение!')


def add_client(conn, cur, name, surname, email, customer_id, phones=None):
    query = ("""INSERT INTO Customers(first_name, last_name) VALUES
        (%s, %s); INSERT INTO email(email, customer_id) VALUES
        (%s, %s);""")
    paramas = (name, surname, email, customer_id,)
    cur.execute(query,paramas)
    conn.commit()
    print('Данные успешно добавлены!')
   

def add_phone(conn, cur, customer_id, number):
    query = ("""INSERT INTO phone_numbers(customer_id, number) VALUES
        (%s, %s);""")
    par = (customer_id, number,)
    cur.execute(query,par)
    conn.commit()
    print(f'Успешно!')

    

def change_client(conn, cur,  customer_id, name=None, surname=None, email=None, number=None):
    sql = ("""UPDATE customers SET first_name =%s, last_name = %s WHERE customer_id =%s;""")
    par = (name,surname,customer_id,)
    cur.execute(sql,par)
    conn.commit()
    print('Успешно!')


def delete_phone(conn, cur, name, surname, customer_id=None):
    sql = """DELETE FROM phone_numbers pn WHERE pn.customer_id = (
            SELECT c.customer_id FROM customers c WHERE first_name 
            LIKE %s AND last_name LIKE %s);"""
    par = (name, surname,)
    cur.execute(sql,par)
    conn.commit()
    print('Удачное удаление!')
    

def delete_client(conn, cur, name, surname, customer_id):
    sql = """DELETE FROM customers WHERE first_name LIKE %s AND last_name LIKE %s
            AND customer_id = %s ;"""
    par =  (name, surname, customer_id,)
    cur.execute(sql,par)
    conn.commit()
    print('Ok')


def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    pass


with psycopg2.connect(database="CustomersDB", user="postgres", password="05121978") as conn:
    create_db(conn)  # вызывайте функции здесь
    with conn.cursor() as cur:
        # add_client(conn, cur, 'Roman', 'Sokolov', 'r@mail.ru', 5)
        # add_phone(conn, cur, 5, 79205855989)
        # change_client(conn, cur,  1, 'Nic', 'Name')
        # delete_phone(conn, cur, 'Nic', 'Name')
        # delete_client(conn, cur, 'Nic', 'Name', 1)


conn.close()