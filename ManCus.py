
#ManCus
#This module have functions for users
"""
*   Description: Functions for Point of Sales
*   Date: 18 Feb 2021
*   Last Created by: Theodore Yun
*   Edit History: v1.0: Jay Basic functions
*				  20 Feb 2021
*				  v1.1: Jay end of basic functions
*				  20 Feb 2021
*				  v1.2: Fix edit_order, pay_order based on modification on ManClass.py
"""

import copy
import os
import ManDB
import ManClass
#Global lists
list_items = {}
list_orders = ManClass.receipt()

navigator_symbol = "/" # This will make the program runnable on any unix based enviroument because it has differnet file system
if os.name == "nt":
    navigator_symbol = "\\" # This will make the program runnable on Windows

#Discount will be optional argument by using *
def add_item(name, category, price, *discount):
	#add new data into the list
	#read and write lists from the file
	item = ManClass.item()
	item.set_name(name)
	item.set_category(category)
	item.set_price(price)
	#default should be 1.0
	if discount:
		item.set_discount(discount)

	list_items[name] = item

def add_order(name, amount):
	#add order
	#copy and paste selected item to order list
	ret = list_items[name]
	if ret:
		order = ManClass.order()
		order.set_item(ret)
		order.set_amount(amount)
		list_orders.add_order(name)
		ret = True
	else:
		print("Item does not exist")
		ret = False
	return ret

def edit_item(name, factor, newkey):
	#edit item data
	#read and write the list
	if name in list_items:
		if factor == 'name':
			list_items[name].set_name(newkey)
		elif factor == 'category':
			list_items[name].set_category(newkey)
		elif factor == 'price':
			list_items[name].set_price(newkey)
		elif factor == 'discount':
			list_items[name].set_discount(newkey)
		else:
			print("Invalid Input")
			return False
	else:
		print("Invalid Input")
		return False

def edit_order(name, factor, newkey):
	#edit order data
	#read and write the list
	return list_orders.edit_order(name, factor, newkey)

def delete_menu(name):
	#delete menu from list
	#read and write lists from the file?
	try:
		del list_items[name]
		return True
	except KeyError:
		print("Option does not exist")
		return False

def delete_order(name):
	#delete order from list
	#read and write the list
	return list_orders.delete_order(name)

def show_item():
	#present orders from list
	#read the orders
	if list_items:
		return list_items
	else:
		print("Option is empty")
		return False

def show_order():
	#present orders from list
	#read the orders
	return list_orders.get_orders()

def get_total():
	#get total price of the each order
	return list_orders.get_total()

def pay_order(customer):
	if customer:
		list_orders.set_customer(customer)
		# database move
		ret = list_orders.get_receipt()
		list_orders = ManClass.receipt()
	else:
		print("Invalid Input")
		ret = False
	return ret

def report_sale(begin_date,end_date):
	#call analized report from DB
	pass
