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

        self.item = db.Table('item', metadata,
                             db.Column('name', db.String(255), nullable=False),
                             db.Column('category', db.String(255), nullable=False),
                             db.Column('price', db.Float(), deafault=0),
                             db.Column('discount', db.float(), default=1.0)
                             )

        metadata.create_all(engine)

    def add_item(self, item):
        query = db.insert(self.item).values(name=item.get_name(), category=item.get_category(),
                                       price=item.get_price(),
                                       discount=item.get_discount())
        ResultProxy = connection.execute(query)

    def delete_item(self, name):
        query = db.delete(self.item)
        query = query.where(self.item.columns.name == item.name)
        results = connection.execute(query)

    def edit_item(self, name, option, new_value):
        query = db.update(self.item).values(name=item.name)
        query = query.where(self.item.columns.Id == 1)
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
