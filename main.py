# pip install psycopg2-binary	- Установка библиотеки.
# createdb -U postgres CustomersDB - создание БД через терминал.
# пароль от postgres.
# psql -U postgres -d CustomersDB - подключение к БД через терминал.
# import psycopg2 
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


