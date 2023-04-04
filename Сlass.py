import psycopg2 

class CustomersDB:
    def __init__(self, nameDB, userDB, passwordDB, query):
        self.nameDB = nameDB
        self.userDB = userDB
        self.passwordDB = passwordDB
        self.query = query

    def connect_create(self):
        connection = None
        try: 
            connection = psycopg2.connect(
                database=self.nameDB, 
                user=self.userDB,
                password=self.passwordDB)
            print(f'Удачное подключение!')
        except ConnectionError as CE:
            print(f'Ошибка подключения {CE}')
        return connection

    def 


class 



connect = CustomersDB('CustomersDB', 'postgres', '05121978')
connect.connect_create()
