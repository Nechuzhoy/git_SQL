import json
import psycopg2
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import datetime
from models import create_tables, Publisher, Book, Shop, Stock, Sale
from sqlalchemy import create_engine

DSN = 'postgresql://postgres'
engine = sqlalchemy.create_engine(DSN)# абстракция для подключения к базе данных

create_tables(engine)

Session = sessionmaker(bind=engine) # Создали как буд-то бы класс Session (sessionmaker)создание сессии для подключения, аналог курсор
session = Session()


if __name__ == '__main__':
    print(session.query(Publisher).filter(Publisher.name == 'Пушкин').all())




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

