import json
import psycopg2
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:____@localhost:5432/____'
engine = sqlalchemy.create_engine(DSN)# абстракция для подключения к базе данных

w = create_tables(engine)

Session = sessionmaker(bind=engine) # Создали как буд-то бы класс Session (sessionmaker)создание сессии для подключения, аналог курсор
session = Session()


def query_publisher_name(publisher_name):
        query = session.query(Publisher,Book,Stock,Sale).filter(Publisher.name == publisher_name).filter(Book.id_publisher == Publisher.id).filter(Stock.id_book == Book.id).filter(Stock.id_shop==Shop.id).filter(Sale.id_stock==Stock.id)
        records = query
        for publisher, book ,stock, sale in query:
            print(f'{book.title} | {stock.shop.name} | {sale.price} | {sale.date_sale}')


def query_publisher_id(publisher_id):
    query = session.query(Publisher, Book, Stock, Sale).filter(Publisher.id == publisher_id).filter(
        Book.id_publisher == Publisher.id).filter(Stock.id_book == Book.id).filter(Stock.id_shop == Shop.id).filter(
        Sale.id_stock == Stock.id)
    records = query
    for publisher, book, stock, sale in query:
        print(f'{book.title} | {stock.shop.name} | {sale.price} | {sale.date_sale}')


if __name__ == '__main__':
    #assert query_publisher_name('Пушкин') == query_publisher_id(5)
    publisher_name = input('Автор - ввод: ')
    query_publisher_name(publisher_name)
    publisher_id = int(input('ID - Автор - ввод: '))
    query_publisher_id(publisher_id)



    # with open('tests_data.json', 'r', encoding='utf-8') as fd:
    #     data = json.load(fd)
    # for record in data:
    #     model = {
    #         'publisher': Publisher,
    #         'shop': Shop,
    #         'book': Book,
    #         'stock': Stock,
    #         'sale': Sale,
    #      }[record.get('model')]
    #     session.add(model(id=record.get('pk'), **record.get('fields')))
    #     session.commit()

