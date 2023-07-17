import psycopg2
from psycopg2 import Error


class BdClient:

    def __init__(self, database, user, password):
        self.params_connection = {'database': database,
                                  'user': user,
                                  'password': password
                                  }

    def conn(self):
        return psycopg2.connect(**self.params_connection)

    def create_table(self, table_name):
        try:
            cursor = self.conn()
            with cursor.cursor() as cur_bd:
                cur_bd.execute(f'CREATE TABLE IF NOT exists {table_name}('
                               f'{table_name}_id SERIAL PRIMARY KEY,'
                               f' first_name VARCHAR(1478) NOT NULL,'
                               f' last_name VARCHAR(1612),'
                               f' email VARCHAR(320) NOT NULL,'
                               f' phones VARCHAR(20),'
                               f' UNIQUE(email)'
                               f');'

                               f'CREATE TABLE IF NOT exists phones('
                               f'phones_id SERIAL primary key,'
                               f'{table_name}_id INT REFERENCES {table_name}({table_name}_id),'
                               f'phones VARCHAR(20));'
                               )
                cursor.commit()
                return f'Таблица {table_name} создана'
        except (Exception, Error) as error:
            return f'Ошибка создания {table_name}', error

    def add_client(self, table_name, first_name, last_name, email, phones=None):
        try:
            cursor = self.conn()
            with cursor.cursor() as cur_bd:
                cur_bd.execute(f'INSERT INTO {table_name} (first_name, last_name, email, phones)'
                               f' VALUES (%s, %s, %s, %s)', [first_name, last_name, email, phones]
                               )

                cursor.commit()
                return 'Чел добавлен'
        except (Exception, Error) as error:
            return "Ошибка при создании чела))))", error

    def add_phones(self, table_name, client_id, phones):
        try:
            cursor = self.conn()
            with cursor.cursor() as cur_bd:
                cur_bd.execute(f'INSERT INTO phones ({table_name}_id, phones)'
                               f' VALUES (%s, %s)', [client_id, phones])
                cursor.commit()
                return 'Добавлен, теперь а связи'
        except (Exception, Error) as error:
            return "Ошибка подключения", error

    def change_client(self, table_name, what_change, on_what_change, client_id):
        try:
            cursor = self.conn()
            with cursor.cursor() as cur_bd:
                cur_bd.execute(
                    f'UPDATE {table_name} set {what_change} = {on_what_change} WHERE {table_name}_id = {client_id}')
                cursor.commit()
                return f' Изменил, теперь кто-то - {on_what_change}'
        except (Exception, Error) as error:
            return "Ошибка подключения", error

    def delete_phone(self, client_id, table_name, on_what_change='NULL', table_name_p='phones', what_change='phones'):
        try:
            cursor = self.conn()
            with cursor.cursor() as cur_bd:
                cur_bd.execute(
                    f'UPDATE {table_name_p} set {what_change} = {on_what_change} WHERE {table_name}_id = {client_id}')
                cursor.commit()
                return "Нет больше телефона"
        except (Exception, Error) as error:
            return "Ошибка подключения", error

    def delete_client(self, table_name, client_id):
        try:
            cursor = self.conn()
            with cursor.cursor() as cur_bd:
                cur_bd.execute(
                    f'DELETE FROM {table_name} WHERE {table_name}_id = {client_id}')
                cursor.commit()
                return "Убили запись"
        except (Exception, Error) as error:
            return "Ошибка подключения", error

    def find_client(self, table_name, where, whom):
        try:
            cursor = self.conn()
            with cursor.cursor() as cur_bd:
                cur_bd.execute(
                    f'SELECT c_id, first_name, last_name, phones FROM {table_name} WHERE {where} = {whom}')
                return cur_bd.fetchone()
        except (Exception, Error) as error:
            return "Ошибка подключения", error


if __name__ == '__main__':
    dict_choice = {1: '1 - Создать таблицу?', 2: '2 - Создать клиента?',
                   3: '3 - Добавить номер?', 4: '4 - Изменить имя',
                   5: '5 - Удалить телефон', 6: '6 - Удалить клиента', 7: '7 - Поиск'
                   }
    a = BdClient(database, user, password)
    r = int(input(
        f'Что изволите съделать??? :\n {dict_choice[1]} \n {dict_choice[2]} \n {dict_choice[3]} \n {dict_choice[4]} \n '
        f'{dict_choice[5]} \n {dict_choice[6]} \n {dict_choice[7]} \nВвод: '))

    if r == 1:
        table_name = input('Назвение таблицы1: ')
        print(a.create_table(table_name))
    elif r == 2:
        table_name = input('Назвение таблицы: ')
        first_name = input('Имя: ')
        last_name = input('Фамилия: ')
        email = input('Email: ')
        phones = input('№ Телефона')
        print(a.add_client(table_name, first_name, last_name, email))
    elif r == 3:
        table_name = input('Назвение таблицы: ')
        client_id = input('ID клиета: ')
        phones = input('Телефон клиета: ')
        print(a.add_phones(table_name, client_id, phones))
    elif r == 4:
        table_name = input('Назвение таблицы: ')
        what_change = 'first_name'
        on_what_change = input('Новое имя: ')
        client_id = input('ID клиета: ')
        print(a.change_client(table_name, what_change, f"'{on_what_change}'", client_id))
    elif r == 5:
        table_name = input('Назвение таблицы: ')
        client_id = input('ID клиета: ')
        print(a.delete_phone(client_id, table_name))
    elif r == 6:
        table_name = input('Назвение таблицы: ')
        client_id = input('ID клиета: ')
        print(a.delete_client(table_name, client_id))
    elif r == 7:
        table_name = input('Назвение таблицы: ')
        where = 'first_name'
        whom = input('Кого ищем: ')
        print(a.find_client(table_name, where, f"'{whom}'"))
