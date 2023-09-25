from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    category = Column(String())
    description = Column(String())
    spice_level = Column(Integer())
    price = Column(Float())

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.category}, {self.description}, {self.price})"
    
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    phone_number = Column(String())
    #One-to-many relationship with order, reviews, and history tables
    order = relationship("Order", backref="customers") 
    reviews = relationship("Review", backref="customers")
    history = relationship("History", backref="customers")

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.phone_number} {self.order})"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer(), primary_key=True)
    items = Column(String())
    total_price = Column(Float())
    customer_id = Column(Integer(), ForeignKey("customers.id"))

    def __repr__(self):
        return f"({self.id}, {self.items}, {self.total_price}, {self.customer_id})"

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer(), primary_key=True)
    rating = Column(Integer())
    comment = Column(String())
    customer_id = Column(Integer(), ForeignKey("customers.id"))

    def __repr__(self):
        return f"{self.id}, {self.rating}, {self.comment}, {self.customer_id}"
    
class History(Base):
    __tablename__ = "histories"

    id = Column(Integer(), primary_key=True)
    order_items = Column(String())
    total = Column(Float())
    customer_id = Column(Integer(), ForeignKey("customers.id"))

    def __repr__(self):
        return f"{self.id}, {self.order_items}, {self.total}, {self.customer_id}"
