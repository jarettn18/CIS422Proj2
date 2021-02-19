# ManDB
# This module manages database for ManEz


import datetime
from sqlalchemy import create_engine, Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


class MenuDB(Base):
    __tablename__ = 'menus'

    menu_name = Column(String(50), primary_key=True)

    def __repr__(self):
        return f"{self.menu_name}"


class SectionDB(Base):
    __tablename__ = 'sections'

    section_name = Column(String(50), primary_key=True)
    menu_id = Column(String, ForeignKey('menus.menu_name'))
    menu = relationship("MenuDB", back_populates="sections")

    def __repr__(self):
        return f"{self.section_name}"


class ItemDB(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    section_id = Column(String, ForeignKey('sections.section_name'))
    section = relationship("SectionDB", back_populates="items")
    item_name = Column(String(50))
    item_price = Column(Integer)

    def __repr__(self):
        return f"{self.item_name}: {self.item_price}"


<<<<<<< HEAD
MenuDB.sections = relationship("SectionDB", order_by=SectionDB.section_name, back_populates="menu")
SectionDB.items = relationship("ItemDB",order_by=ItemDB.item_name, back_populates="section")
Base.metadata.create_all(engine)
=======
datetime

sort

def report(date):
	
>>>>>>> 2bb77c8abe608f5f33ef2075af63cd3846833088
