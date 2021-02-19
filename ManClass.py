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
"""


class item:
	def __init__(self):
		self.name = None
		self.category = None
		self.price = 0.0
		self.discount = 1.0

	def get_name(self):
		return self.name

	def get_catagory(self):
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

	def set_catagory(self, category):
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
		if (0 <= discount) and (discount <= 1):
			self.discount = discount
			return True
		else:
			print("Invalid Discount")
			return False


"""
*   Class: receipt
*   Description: This class contains details of a receipt. It contains
*				 customer's name, orders list, total cost, and discount factor.
*   Date: 18 Feb 2021
*   Last Created by: Perat Damrongsiri
*   Edit History: v1.0: Creating all the function.
"""


class receipt:
	def __init__(self):
		self.customer_name = None
		self.orders = None
		self.total = 0.0
		self.discount = 1.0

	def get_customer_name(self):
		if self.customer_name:
			ret = self.customer_name
		else:
			print("Error: receipt(): get_customer_name(): customer_name is empty.")
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

	def set_customer_name(self, name):
		if isinstance(name, str):
			self.name = name
			ret = True
		else:
			print("Error: receipt(): set_customer_name(): Invalid name.")
			ret = False
		return ret

	def set_orders(self, orders):
		if isinstance(orders, dict):
			self.orders = orders
			ret = True
		else:
			print("Error: receipt(): set_orders(): Invalid orders data type.")
			ret = False
		return ret

	def set_total(self, total):
		if total >= 0:
			self.total = total
			ret = True
		else:
			print("Error: receipt(): set_total(): Invalid total cost.")
			ret = False
		return ret

	def set_discount(self, discount):
		if discount >= 0 and discount <= 1:
			self.discount = discount
			ret = True
		else:
			print("Error: receipt(): set_discount(): Invalid discount factor.")
			ret = False
		return ret
