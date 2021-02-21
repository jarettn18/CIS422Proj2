import sqlalchemy as db
import ManClass

class ItemDatabase:
    def __init__(self):
        self.engine = None
        self.connection = None
        self.metadata = None

    def start_session(self):
        self.engine = db.create_engine('sqlite:///ManEzItems.sqlite')
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()

        self.items = db.Table('items', metadata,
                             db.Column('name', db.String(255), nullable=False),
                             db.Column('category', db.String(255), nullable=False),
                             db.Column('price', db.Float(), deafault=10),
                             db.Column('discount', db.float(), default=1.0)
                             )

        metadata.create_all(engine)

    def add_item(self, items):
        for elem in ManClass.order().get_item():
            query = db.insert(self.items).values(name=ManClass.item().get_name(), category=ManClass.item().get_category(),
                                       price=ManClass.item().get_price(),
                                       discount=ManClass.item().get_discount())
            ResultProxy = connection.execute(query)

    def delete_item(self, name):
        for elem in ManClass.order().get_item():
            query = db.delete(self.items)
            query = query.where(self.items.columns.name == ManClass.item().name)
            results = connection.execute(query)

    def edit_item(self, name, option, new_value):
        for elem in ManClass.order().get_item():
            query = db.update(self.items).values(name=ManClass.item().name)
            query = query.where(self.items.columns.Id == 1)
            results = connection.execute(query)

class ReceiptDatabase:
    def __init__(self):
        self.engine = None
        self.connection = None
        self.metadata = None

    def start_session(self):
        self.engine = db.create_engine('sqlite:///ManEzReceipts.sqlite')
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.receipts = db.Table('receipts', metadata,
              db.Column('date', db.date()),
              db.Column('datetime', db.datetime()),
              db.Column('name', db.String(255), nullable=False),
              db.Column('orders', db.String(255), nullable=False),
              db.Column('discount', db.Float(), default=1.0),
              db.Column('amount', db.Integer(), default=1),
              db.Column('price', db.Boolean(), default=True)
              )

        metadata.create_all(engine) #Creates the table

    def add_receipt(self, item):
        pass

    def delete_receipt(self, name):
        pass

    def get_report(self, start_date, end_date):
        pass
