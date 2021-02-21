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
import datetime

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

	def set_item(self, item):
		if item:
			self.item = copy.deepcopy(item)
			ret = True
		else:
			print("Error: order(): set_item(): Invalid item.")
			ret = False
		return ret

	def set_amount(self, amount):
		if amount > 0:
			self.amount = amount
			ret = True
		else:
			print("Error: order(): set_amount(): Invalid amount.")
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
		self.orders = []
		self.total = 0.0
		self.discount = 1.0

	def add_order(self, order):
		for elem in self.orders:
			if order.get_item().get_name() == elem.get_item().get_name():
				elem.set_amount(elem.get_amount() + order.get_amount())
				self.cal_total()
				return True
		orders.append(order)
		self.cal_total()
		return True

	def delete_order(self, name):
		for i in range(len(self.orders)):
			elem = self.orders[i]
			if name == elem.get_item().get_name():
				del elem
				self.cal_total()
				return True
		print("Error: receipt(): delete_order(): ", name, " does not exist in orders.")
		return False

	def edit_order(self, name, new_amount):
		for elem in self.orders:
			if name == elem.get_item().get_name():
				elem.set_amount(new_amount)
				self.cal_total()
				return True
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
			self.name = name
			ret = True
		else:
			print("Error: receipt(): set_customer(): Invalid name.")
			ret = False
		return ret

	def cal_total(self):
		if self.orders:
			self.total = 0
			for elem in self.orders:
				item = elem.get_item()
				self.total += item.get_price() * item.get_discount() * elem.get_amount()
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
		str = 'Date: ' + datetime.datetime.now() + '\n'
		str += 'Customer: ' + self.get_customer() + '\n'
		str += '---------------------------------------------\n'
		str += 'order                         amount    price\n'
		str += '---------------------------------------------\n'
		for order in self.get_orders():
			order_txt = order.get_item().get_name()
			for i in range(30 - len(order_txt)):
				order_txt += ' '
			order_amount = str(order.get_amount())
			for i in range(6 - len(order_amount)):
				order_txt += ' '
			order_txt += order_amount + '    '
			order_price = '$' + str(order.get_item().get_price())
			for i in range(5 - len(order_price)):
				order_txt += ' '
			order_txt += order_price + '\n'
			str += order_txt
		str += '---------------------------------------------\n'
		str += 'Total:'
		total = '$' + str(self.get_total())
		for i in range(39 - len(total)):
			str += ' '
		str += total + '\n'
		str += '==============================================\n'
		return str
