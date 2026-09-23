from sqlalchemy import Column,Integer,String,Float,Date,ForeignKey
from .database import Base
class Customer(Base):
    __tablename__="customers"; id=Column(Integer,primary_key=True); name=Column(String); email=Column(String,unique=True); state=Column(String)
class Product(Base):
    __tablename__="products"; id=Column(Integer,primary_key=True); name=Column(String); category=Column(String); price=Column(Float)
class Order(Base):
    __tablename__="orders"; id=Column(Integer,primary_key=True); customer_id=Column(Integer,ForeignKey("customers.id")); product_id=Column(Integer,ForeignKey("products.id")); quantity=Column(Integer); order_date=Column(Date); revenue=Column(Float)
