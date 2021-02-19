
#ManClass
#This module contains class to create menu

class item():
	def __init__():
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


class receipt():
	def __init__():
		self.customer_name = None
		self.orders = None
		self.total = 0.0
		self.discount = 1.0

	def get_customer_name():
		pass

	def get_orders():
		pass

	def get_total():
		pass

	def get_discount():
		pass

	def set_customer_name():
		pass

	def set_orders():
		pass

	def set_total():
		pass

	def set_discount():
		pass