"""
*   Title:			 ManDB.py
*   Project:		 ManEz
*   Description:     Database for saving report data from item,order,and employee
*
*   Team:			 TAP2J
*
*   Last Created by: Perat Damrongsiri
*                    Theodore Yun
*   Date Created:    21 Feb 2021
                    v 1.0 : Initial creation
                    v 1.1 : Edition 24 Feb 2021
"""

import sqlalchemy_utils as db_utils
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import datetime
import ManClass
# just for read_db function
from decimal import Decimal

"""
*   Class: ItemDatabase
*   Description:
*   Date: 21 Feb 2021
*   Last Created by: Perat Damrongsiri
*   Edit History: 21 Feb 2021 - Theodore Yun
*                 v1.0: Creating all the function.
"""


# Create item Database for saving data
class ItemDatabase:
    def __init__(self):
        self.engine = None
        self.connection = None
        self.metadata = None
        self.item = None

    def start_session(self):
        self.engine = db.create_engine('sqlite:///ManEzItems.sqlite')
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()

        # Set each column for each variable
        self.item = db.Table('item', self.metadata,
                             db.Column('name', db.String(255), nullable=False),
                             db.Column('category', db.String(255), nullable=False),
                             db.Column('price', db.Float(), default=0.0),
                             db.Column('discount', db.Float(), default=1.0)
                             )
        self.metadata.create_all(self.engine)

    # Add item into item list
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

    # Delete selected item in item list
    def delete_item(self, name):
        if name:
            query = db.delete(self.item)
            query = query.where(self.item.columns.name == self.item.name)
            ret = self.connection.execute(query)
        else:
            print("Invalid Input")
            ret = False
        return ret

    # Modify information of the item
    def edit_item(self, name):
        if name:
            query = db.update(self.item).values(name=self.item.name)
            query = query.where(self.item.columns.Id == 1)
            ret = self.connection.execute(query)
        else:
            print("Invalid Input")
            ret = False
        return ret

    # Read data of item from item database
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
*                 11 Mar 2021 - Perat Damrongsiri
*                 v1.0.1: fix datetime different on the same receipt problem.
*                         fixed the logic problem in delete_receipt.
"""


class ReceiptDatabase:
    def __init__(self):
        """
        class variables
        """
        self.engine = None
        self.connection = None
        self.metadata = None
        self.receipts = None

    def start_session(self):
        """
        Binding the sql engine to the receipt database. If the receipt database
        does not exist, it will create one.
        """
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
        """
        Add the receipt to the receipt database
        """
        # check the datatype of receipt
        if type(receipt) == ManClass.Receipt:
            # finding the latest added receipt
            Session = sessionmaker(bind=self.engine)
            session = Session()
            desc_expression = db.sql.expression.desc(self.receipts.c.datetime)
            last_item = session.query(self.receipts).order_by(desc_expression).first()
            # checking the date of the latest receipt and today date
            if last_item and last_item.date == datetime.date.today():
                # on the same date. increse the receipt number by 1
                rec_num = last_item.number + 1
            else:
                # different date. reset receipt number to 1
                rec_num = 1

            orders = receipt.get_orders()
            date = datetime.date.today()
            dt = datetime.datetime.now()
            # loop through orders in receipt
            for elem in orders:
                # put each order into each row
                query = db.insert(self.receipts).values(number=rec_num, date=date,
                                                        datetime=dt, name=receipt.get_customer(),
                                                        orders=elem, discount=receipt.get_discount(),
                                                        amount=orders[elem].get_amount(),
                                                        price=orders[elem].get_item().get_price())
                self.connection.execute(query)
            ret = True
        else:
            # invalid datatype
            print("Error: ReceiptDatabase(): add_receipt(): receipt: Invalid data type.")
            ret = False
        return ret

    def delete_receipt(self, receipt_num, date, name):
        """
        Remove the specific receipt from the database
        """
        # checking the receipt number
        if Decimal(receipt_num) % 1 == 0 and Decimal(receipt_num) > 0:
            # check the date parameter
            if isinstance(date, datetime.date):
                # check the name
                if isinstance(name, str):
                    # delete the receipt.
                    query = db.delete(self.receipts)
                    query = query.where(self.receipts.c.number == receipt_num). \
                        where(self.receipts.c.date == date). \
                        where(self.receipts.c.name == name)
                    self.connection.execute(query)
                    ret = True
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
        """
        Get the dictionary of receipts during start_date to end_date
        """
        if isinstance(start_date, datetime.date) and isinstance(end_date, datetime.date):
            # regular database calls
            Session = sessionmaker(bind=self.engine)
            session = Session()
            # delta 1 day to start date to loop until end_date
            delta = datetime.timedelta(days=1)
            # return dic
            ret = {}
            while start_date <= end_date:
                query_res = session.query(self.receipts).filter(self.receipts.c.date.like(start_date)).all()
                ret[start_date] = query_res
                start_date += delta
        else:
            print("Error: get_report(): Invalid date input")
            ret = False
        return ret


"""
*   Class: WorkTimeDatabase
*   Description:
*   Date: 7 March 2021
*   Last Created by: Jay Shin
*   Edit History: 27 Feb 2021 - Jay Shin
*                 v1.0: Creating all the functions.
*                 v2.0: Edit functions.
"""


class WorkTimeDatabase:
    def __init__(self):
        self.engine = None
        self.connection = None
        self.metadata = None
        self.work = None

    def start_session(self):
        self.engine = db.create_engine('sqlite:///ManEzUsers.sqlite')
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.work = db.Table('users', self.metadata,
                             db.Column('name', db.String(255), nullable=False),
                             db.Column('date', db.Date()),
                             db.Column('login_time', db.DateTime()),
                             db.Column('logout_time', db.DateTime()),
                             db.Column('work_time', db.Interval())
                             )

        self.metadata.create_all(self.engine)

    def checkout(self, employee):
        if type(employee) == ManClass.Employee:
            if employee.get_login_time():
                query = db.insert(self.work).values(name=employee.get_name(),
                                                    date=datetime.date.today(),
                                                    login_time=employee.get_login_time(),
                                                    logout_time=employee.get_logout_time(),
                                                    work_time=(employee.get_logout_time() - employee.get_login_time())
                                                    )
                self.connection.execute(query)
                ret = True
            else:
                print("Error: WorkTimeDatabase(): employee: require log-in first.")
                ret = False
        else:
            print("Error: WorkTimeDatabase(): employee: Invalid data type.")
            ret = False
        return ret

    def read_db(self):
        query = db.select([self.work])
        return self.connection.execute(query).fetchall()


"""
*   Class: EmployeesDatabase
*   Description:
*   Date: 2 Mar 2021
*   Last Created by: Perat Damrongsiri
*   Edit History: v1.0: Creating all the function.
"""


class EmployeesDatabase:
    def __init__(self):
        """
        class variables
        """
        self.engine = None
        self.connection = None
        self.metadata = None
        self.employees = None

    def start_session(self):
        """
        Binding the sql engine to the employees database. If the employees database
        does not exist, it will create one.
        """
        self.engine = db.create_engine('sqlite:///ManEzEmployees.sqlite')
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.employees = db.Table('employees', self.metadata,
                                  db.Column('name', db.String(255), nullable=False),
                                  db.Column('permission', db.String(255), nullable=False),
                                  db.Column('pass_hash', db.String(255), nullable=False),
                                  db.Column('recov_key', db.String(255), nullable=False)
                                  )

        self.metadata.create_all(self.engine)

    def add_employee(self, employee):
        """
        add employee to the database.
        """
        # check the datatype of employee
        if type(employee) == ManClass.Employee:
            # add employee to the database
            query = db.insert(self.employees).values(name=employee.get_name(),
                                                     permission=employee.get_permission(),
                                                     pass_hash=employee.get_pass_hash(),
                                                     recov_key=employee.get_key())
            self.connection.execute(query)
            ret = True
        else:
            print("Error: EmployeesDatabase(): add_employee(): Invalid datatype.")
            ret = False
        return ret

    def delete_employee(self, name):
        """
        delete employee from database
        """
        delete = self.employees.delete().where(self.employees.c.name == name)
        self.connection.execute(delete)

    def edit_employee(self, name, option, value):
        """
        edit employee's data in database according to the options which are name,
        permission, and password.
        """
        if option == 'name':
            # change name.
            update = self.employees.update().where(self.employees.c.name == name).values(name=value)
            self.connection.execute(update)
            ret = True
        elif option == 'permission':
            # change permission
            update = self.employees.update().where(self.employees.c.name == name).values(permission=value)
            self.connection.execute(update)
            ret = True
        elif option == 'password':
            # change password
            update = self.employees.update().where(self.employees.c.name == name).values(pass_hash=value)
            self.connection.execute(update)
            ret = True
        else:
            print("Error: EmployeesDatabase(): edit_employee(): Invalid option.")
            ret = False
        return ret

    def is_exist(self):
        """
        checking that the database is exist or not.
        """
        if db_utils.database_exists('sqlite:///ManEzEmployees.sqlite'):
            ret = True
        else:
            ret = False
        return ret

    def read_db(self):
        """
        read the database and return the data as a list.
        """
        query = db.select([self.employees])
        return self.connection.execute(query).fetchall()
