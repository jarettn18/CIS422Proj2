"""
*   Title:			 ManDB.py
*   Project:		 ManEz
*   Description:
*
*   Team:			 TAP2J
*
*   Last Created by: Perat Damrongsiri
*                    Theodore Yun
*   Date Created:    21 Feb 2021
                    v 1.0 : Initial creation
                    v 1.1 : Edition 24 Feb 2021
"""


import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import datetime
import ManClass
#just for read_db function
import ManCus
from decimal import Decimal

"""
*   Class: ItemDatabase
*   Description:
*   Date: 21 Feb 2021
*   Last Created by: Perat Damrongsiri
*   Edit History: 21 Feb 2021 - Theodore Yun
*                 v1.0: Creating all the function.
"""

class ItemDatabase:
    def __init__(self):
        self.engine = None
        self.connection = None
        self.metadata = None

    def start_session(self):
        self.engine = db.create_engine('sqlite:///ManEzItems.sqlite')
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()

        self.item = db.Table('item', self.metadata,
              db.Column('name', db.String(255), nullable=False),
              db.Column('category', db.String(255), nullable=False),
              db.Column('price', db.Float(), default=0.0),
              db.Column('discount', db.Float(), default=1.0)
              )
        self.metadata.create_all(self.engine)

    def add_item(self, item):
        if item:
            query = db.insert(self.item).values(name=item.get_name(), category=item.get_category(),
                      price=item.get_price(),
                      discount=item.get_discount())
            ret = self.connection.execute(query)
        else:
            print("Invalid Input")
            ret = False
        return ret

    def delete_item(self, name):
        if name:
            query = db.delete(self.item)
            query = query.where(self.item.columns.name == item.name)
            ret = self.connection.execute(query)
        else:
            print("Invalid Input")
            ret = False
        return ret

    def edit_item(self, name):
        if name:
            query = db.update(self.item).values(name=item.name)
            query = query.where(self.item.columns.Id == 1)
            ret = self.connection.execute(query)
        else:
            print("Invalid Input")
            ret = False
        return ret

    def read_db(self):
        query = db.select([self.item])
        return self.connection.execute(query).fetchall()
            
"""
*   Class: ReceiptDatabase
*   Description:
*   Date: 21 Feb 2021
*   Last Created by: Perat Damrongsiri
*   Edit History: 21 Feb 2021 - Perat Damrongsiri
*                 v1.0: Creating all the function.
"""


class ReceiptDatabase:
    def __init__(self):
        self.engine = None
        self.connection = None
        self.metadata = None

    def start_session(self):
        self.engine = db.create_engine('sqlite:///ManEzReceipts.sqlite')
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.receipts = db.Table('receipts', self.metadata,
              db.Column('number', db.Integer()),
              db.Column('date', db.Date()),
              db.Column('datetime', db.DateTime()),
              db.Column('name', db.String(255), nullable=False),
              db.Column('orders', db.String(255), nullable=False),
              db.Column('discount', db.Float(), default=1.0),
              db.Column('amount', db.Integer(), default=1),
              db.Column('price', db.Float())
              )

        self.metadata.create_all(self.engine)

    def add_receipt(self, receipt):
        if type(receipt) == ManClass.receipt:
            Session = sessionmaker(bind=self.engine)
            session = Session()
            desc_expression = db.sql.expression.desc(self.receipts.c.date)
            last_item = session.query(self.receipts).order_by(desc_expression).first()
            if last_item and last_item.date == datetime.date.today():
                rec_num = last_item.number + 1
            else:
                rec_num = 1

            orders = receipt.get_orders()
            for elem in orders:
                query = db.insert(self.receipts).values(number=rec_num, date=datetime.date.today(),
                    datetime=datetime.datetime.now(), name=receipt.get_customer(),
                    orders=elem, discount=receipt.get_discount(),
                    amount=orders[elem].get_amount(), price=receipt.get_total())
                ResultProxy = self.connection.execute(query)
            ret = True
        else:
            print("Error: ReceiptDatabase(): add_receipt(): receipt: Invalid data type.")
            ret = False
        return ret

    def delete_receipt(self, receipt_num, date, name):
        if Decimal(receipt_num) % 1 == 0 and Decimal(receipt_num) > 0:
            if isinstance(date, datetime.date):
                if isinstance(name, str):
                    Session = sessionmaker(bind=engine)
                    session = Session()
                    query_res = session.query(self.receipts).filter(self.receipts.c.number == receipt_num). \
                        filter(self.receipts.c.date == date).filter(self.receipts.c.name == name).all()
                    if len(query_res) > 1:
                        if len(query_res) == 0:
                            query = db.delete(self.receipts)
                            query = query.where(self.receipts.c.number == receipt_num). \
                                where(self.receipts.c.date == date). \
                                where(self.receipts.c.name == name)
                            self.connection.execute(query)
                            ret = True
                        else:
                            print("Error: ReceiptDatabase(): delete_receipt(): Receipt not found.")
                            ret = False
                    else:
                        print("Error: ReceiptDatabase(): delete_receipt(): Found more than 1 receipt.")
                        ret = False
                else:
                    print("Error: ReceiptDatabase(): delete_receipt(): Invalid name's data type")
                    ret = False
            else:
                print("Error: ReceiptDatabase(): delete_receipt(): Invalid date's data type")
                ret = False
        else:
            print("Error: ReceiptDatabase(): delete_receipt(): Invalid receipt number's data type")
            ret = False
        return ret

    def get_period(self, start_date, end_date):
        if isinstance(start_date, datetime.date) and isinstance(end_date, datetime.date):
            #regular database calls
            Session = sessionmaker(bind=self.engine)
            session = Session()
            #delta 1 day to start date to loop until end_date
            delta = datetime.timedelta(days=1)
            #return dic
            ret = {}
            while start_date <= end_date:
                query_res = session.query(self.receipts).filter(self.receipts.c.date.like(start_date)).all()
                ret[start_date] = query_res
                start_date += delta
        else:
            print("Error: get_report(): Invalid date input")
            ret = False
        return ret