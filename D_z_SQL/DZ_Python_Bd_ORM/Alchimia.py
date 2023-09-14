import json
import psycopg2
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:....@localhost:.....'
engine = sqlalchemy.create_engine(DSN)# абстракция для подключения к базе данных

w = create_tables(engine)

Session = sessionmaker(bind=engine) # Создали как буд-то бы класс Session (sessionmaker)создание сессии для подключения, аналог курсор
session = Session()

def filling_tables(file):
    with open(file, 'r', encoding='utf-8') as fd:
        data = json.load(fd)
    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
         }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()

def query_publisher_name_id(name_id):
    query_tables = session.query(Publisher,Book,Stock,Sale).\
            join(Stock, Stock.id_book == Book.id).\
            join(Publisher).\
            join(Sale, Sale.id_stock == Stock.id)
            #filter(Publisher.name == "Пушкин").all()
    if name_id.isdigit():  # Проверяем переданные данные в функцию на то, что строка состоит только из чисел
        query_filter = query_tables.filter(Publisher.id == name_id).all()  # Обращаемся к запросу, который составили ранее, и применяем фильтрацию, где айди публициста равно переданным данным в функцию, и сохраняем в переменную
    else:
        query_filter = query_tables.filter(Publisher.name == name_id).all()
    for publisher, book ,stock, sale in query_filter:
        print(f'{book.title} | {stock.shop.name} | {sale.price} | {sale.date_sale}')


if __name__ == '__main__':
    filling_tables('tests_data.json')

    name_id = input('name or id: ')
    query_publisher_name_id(name_id)

    #assert query_publisher_name_id('Пушкин') == query_publisher_name_id('5')





