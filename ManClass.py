"""
*   Title:			 ManClass.py
*   Project:		 ManEz
*   Description:
*
*   Team:			 TAP2J
*
*   Last Created by: Jay Shin
*					 Perat Damrongsiri
*   Date Created:    18 Feb 2021
"""


"""
*   Class: item
*   Description: This class contains detail of an item for sale. The detail that
*				 will be contain in this class are item's name, category, price,
*				 and discount factor.
*   Date: 18 Feb 2021
*   Last Created by: Jay Shin
*   Edit History: v1.0: Creating all the function.
*				  20 Feb 2021 - Perat Damrongsiri
*				  v1.1: Edited set_discount()
"""

import copy
import hashlib
import datetime
import random

class item:
	def __init__(self):
		self.name = None
		self.category = None
		self.price = 0.0
		self.discount = 1.0

	def get_name(self):
		return self.name

	def get_category(self):
		return self.category

	def get_price(self):
		return self.price

	def get_discount(self):
		return self.discount

	def set_name(self, name):
		if name:
			self.name = name
			return True
		else:
			print("Invalid Name")
			return False

	def set_category(self, category):
		if category:
			self.category = category
			return True
		else:
			print("Invalid Category")
			return False

	def set_price(self, price):
		if price > 0:
			self.price = price
			return True
		else:
			print("Invalid Price")
			return False

	def set_discount(self, discount):
		if discount >= 0 and discount <= 100:
			self.discount = (100 - discount) / 100
			ret = True
		else:
			print("Error: item(): set_discount(): Invalid discount (range should be 0 - 100).")
			ret = False
		return ret
"""
*   Class: order
*   Description: This class contains details of a order. It contains
*
*   Date: 20 Feb 2021
*   Last Created by: Jay Shin
*   Edit History: v1.0: Creating all the function.
*				  20 Feb 2021 - Perat Damrongsiri
*				  v1.1: Added type checking for setters.
"""

class order():
	"""docstring for order"""
	def __init__(self):
		self.item = None
		self.amount = 1

	def get_item(self):
		if self.item:
			ret = self.item
		else:
			print("Error: order(): get_item(): item is empty.")
			ret = False
		return ret

	def get_amount(self):
		if self.item:
			ret = self.amount
		else:
			print("Error: order(): get_amount(): item is empty.")
			ret = False
		return ret

	def set_item(self, value):
		if value and type(value) == item:
			self.item = copy.deepcopy(value)
			ret = True
		else:
			print("Error: order(): set_item(): Invalid value for item.")
			ret = False
		return ret

	def set_amount(self, amount):
		if amount > 0 and str(amount).isdigit():
			self.amount = float(amount)
			ret = True
		else:
			print("Error: order(): set_amount(): Invalid value for amount.")
			ret = False
		return ret



"""
*   Class: receipt
*   Description: This class contains details of a receipt. It contains
*				 customer's name, orders list, total cost, and discount factor.
*   Date: 18 Feb 2021
*   Last Created by: Perat Damrongsiri
*   Edit History: v1.0: Creating all the function.
*				  20 Feb 2021
*				  v1.1: Change total setter to calculate total.
*				  20 Feb 2021
*				  v1.2: Remove orders setter. Added functions related to orders.
"""


class receipt:
	def __init__(self):
		self.customer = None
		self.orders = {}
		self.total = 0.0
		self.discount = 1.0

	def add_order(self, new_order):
		if type(new_order) == order:
			name = new_order.get_item().get_name()
			if name in self.orders:
				self.orders[name].set_amount(elem.get_amount() + order.get_amount())
				self.cal_total()
				return True
			self.orders[name] = new_order
			self.cal_total()
			return True
		else:
			print("Error: receipt(): add_order(): new_order is not order object")
			return False

	def delete_order(self, name):
		if name in self.orders:
			del self.orders[name]
			self.cal_total()
			ret = True
		else:
			print("Error: receipt(): delete_order(): ", name, " does not exist in orders.")
			ret = False
		return ret

	def edit_order(self, name, option, new_value):
		if name in self.orders:
			if option == 'item':
				self.orders[name].set_item(new_value)
				self.add_order(self.orders[name])
				self.delete_order(name)
				return True
			elif option == 'amount':
				self.orders[name].set_amount(new_value)
				self.cal_total()
				return True
			else:
				print("Error: receipt(): edit_order(): ", option, "is invalid.")
				return False
		print("Error: receipt(): edit_order(): ", name, "does not exist in orders.")
		return False

	def get_customer(self):
		if self.customer:
			ret = self.customer
		else:
			print("Error: receipt(): get_customer(): customer is empty.")
			ret = False
		return ret

	def get_orders(self):
		if self.orders:
			ret = self.orders
		else:
			print("Error: receipt(): get_orders(): orders is empty.")
			ret = False
		return ret

	def get_total(self):
		if self.total:
			ret = self.total
		else:
			print("Error: receipt(): get_total(): total is empty.")
			ret = False
		return ret

	def get_discount(self):
		if self.discount:
			ret = self.discount
		else:
			print("Error: receipt(): get_discount(): discount is empty.")
			ret = False
		return ret

	def set_customer(self, name):
		if isinstance(name, str):
			self.customer = name
			ret = True
		else:
			print("Error: receipt(): set_customer(): Invalid name.")
			ret = False
		return ret

	def cal_total(self):
		if self.orders:
			self.total = 0
			for elem in self.orders:
				item = self.orders[elem].get_item()
				self.total += item.get_price() * item.get_discount() * self.orders[elem].get_amount()
			self.total *= self.discount
			ret = True
		else:
			print("Error: receipt(): cal_total(): No order is made.")
			ret = False
		return ret

	def set_discount(self, discount):
		if discount >= 0 and discount <= 100:
			self.discount = (100 - discount) / 100
			ret = True
		else:
			print("Error: receipt(): set_discount(): Invalid discount (range should be 0 - 100).")
			ret = False
		return ret

	def get_receipt(self):
		ret_str = 'Date: '
		ret_str += datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + '\n'
		ret_str += 'Customer: ' + self.get_customer() + '\n'
		ret_str += '---------------------------------------------\n'
		ret_str += 'order                         amount    price\n'
		ret_str += '---------------------------------------------\n'
		orders = self.get_orders()
		for order in orders:
			order_txt = orders[order].get_item().get_name()
			for i in range(30 - len(order_txt)):
				order_txt += ' '
			order_amount = str(orders[order].get_amount())
			for i in range(6 - len(order_amount)):
				order_txt += ' '
			order_txt += order_amount + '    '
			order_price = '$' + str(orders[order].get_item().get_price())
			for i in range(5 - len(order_price)):
				order_txt += ' '
			order_txt += order_price + '\n'
			ret_str += order_txt
		ret_str += '---------------------------------------------\n'
		ret_str += 'Total:'
		total = '$' + str(self.get_total())
		for i in range(39 - len(total)):
			ret_str += ' '
		ret_str += total + '\n'
		ret_str += '==============================================\n'
		return ret_str

"""
*   Class: Employee
*   Description: This class contains details of an employee. It contains
*				 employee's name, password, permission, login time, logout time,
*				 and recovery key.
*   Date: 27 Feb 2021
*   Last Created by: Perat Damrongsiri
*   Edit History: v1.0: Creating all the function.
"""


class Employee:
	def __init__(self, name=None, permission='emp', login=None):
		self._name = name
		self._password_hash = None
		self._permission = permission
		self._login_time = login
		self._logout_time = None
		self._recovery_key = None

	def is_admin(self):
		if self._permission == 'admin':
			ret = True
		else:
			ret = False
		return ret

	def set_login_time(self):
		if not self._login_time:
			self._login_time = datetime.datetime.now()
			ret = True
		else:
			print("Error: Employee(): set_login_time(): Already login.")
			ret = False
		return ret

	def set_logout_time(self):
		if self._login_time:
			if not self._logout_time:
				self._logout_time = datetime.datetime.now()
				ret = 1
			else:
				print("Error: Employee(): set_logout_time(): Already logout.")
				ret = 2
		else:
			print("Error: Employee(): set_logout_time(): This employee did not login yet.")
			ret = 3
		return ret

	def set_password(self, password):
		if not self._password_hash:
			if len(password) == 4:
				self._password_hash = hashing(password)
				ret = 1
			else:
				print("Error: Employee(): set_password(): password has to be 4 characters")
				ret = 2
		else:
			print("Trying to pass this wall?? no way!!!")
			ret = 3
		return ret

	def set_recovery_key(self):
		if not self._recovery_key:
			self._recovery_key = random.randint(1000, 10000)
			ret = self._recovery_key
		else:
			print("Error: Employee(): set_recovery_key(): recovery key is already set.")
			ret = False
		return ret

	def change_password(self, old_pass, new_pass):
		old_pass_hash = hashing(old_pass)
		if self._password_hash == old_pass_hash:
			if len(password) == 4:
				self._password_hash = hashing(new_pass)
				ret = 1
			else:
				print("Error: Employee(): change_password(): password has to be 4 characters")
				ret = 2
		else:
			print("Invalid Password (Previous Password does not match).")
			ret = 3
		return ret

	def forgot_password(self, key, new_pass):
		if key == self._recovery_key:
			self._password_hash = hashing(new_pass)
			ret = True
		else:
			print("Error: Employee(): forgot_password(): Wrong recovery key.")
			ret = False
		return ret

	def get_login_time(self):
		if self._login_time:
			ret = self._login_time
		else:
			print("Error: Employee(): get_login_time(): login time is none")
			ret = False
		return ret

	def get_name(self):
		if self._name:
			ret = self._name
		else:
			print("Error: employee(): get_name(): name is empty")
			ret = False
		return ret

	def set_to_admin(self, employee, password):
		if type(employee) == Employee:
			if self._permission == 'admin':
				if self._password_hash == hashing(password):
					employee._permission = 'admin'
					ret = 1
				else:
					print("Error: employee(): set_to_admin(): Wrong Password.")
					ret = 2
			else:
				print("Error: employee(): set_to_admin(): Require Admin Permission.")
				ret = 3
		else:
			print("Error: employee(): set_to_admin(): employee is not Employee object.")
			ret = 4
		return ret

	def add_employee(self, name):
		if name:
			ret = employee(name=name)
		else:
			print("Error: employee(): add_employee(): Invalid name.")
			ret = False
		return ret

	def add_admin(self, name, password):
		if self._permission == 'admin':
			if self._password_hash == hashing(password):
				new_employee = Employee(name=name, permission='admin')
				ret = new_employee
			else:
				print("Error: employee(): add_admin(): Wrong Password.")
				ret = 2
		else:
			print("Error: employee(): add_admin(): Require Admin Permission.")
			ret = 3
		return ret

	def demote_from_admin(self, admin, password):
		if type(employee) == admin:
			if self._permission == 'admin':
				if self._password_hash == hashing(password):
					admin._permission = 'emp'
					ret = 1
				else:
					print("Error: employee(): set_to_admin(): Wrong Password.")
					ret = 2
			else:
				print("Error: employee(): set_to_admin(): Require Admin Permission.")
				ret = 3
		else:
			print("Error: employee(): set_to_admin(): employee is not Employee object.")
			ret = 4
		return ret

	def checkpass(self, password):
		if self._password_hash == hashing(password):
			ret = True
		else:
			print("Error: employee(): checkpass(): Wrong password.")
			ret = False
		return ret

	def get_key(self):
		if self._recovery_key:
			ret = self._recovery_key
		else:
			ret = False
		return ret

	def get_permission(self):
		if self._permission:
			ret = self._permission
		else:
			ret = False
		return ret

	def get_pass_hash(self):
		if self._password_hash:
			ret = self._password_hash
		else:
			ret = False
		return ret

def hashing(param_in):
	return hashlib.sha256(param_in.encode('ascii')).hexdigest()
