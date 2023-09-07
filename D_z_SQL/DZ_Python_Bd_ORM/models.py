import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()
class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)




class Book(Base):#класс регистрирует созданные обьекты, потом их можно будет создать
    __tablename__ = "book"
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.Text, nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False) #ссылка на внешний ключ
    publisher = relationship("Publisher", backref="book")  # связи таблиц


class Shop(Base):
    __tablename__ = "shop"
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

class Stock(Base):
    __tablename__ = "stock"
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer)

class Sale(Base):
    __tablename__ = "sale"
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.String(length=40),nullable=False)
    date_sale = sq.Column(sq.DateTime,nullable=False)
    count = sq.Column(sq.Integer)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)


def create_tables(engine):
    #Base.metadata.drop_all(engine)# метод drop_all удалит все таблицы в базе данных
    Base.metadata.create_all(engine)#метод create_all создаст все таблицы в базе данных


