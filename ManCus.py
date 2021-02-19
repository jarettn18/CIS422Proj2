
#ManCus
#This module have functions for users

import copy
import os
#import ManDB
import ManClass
#Global lists
list_items = {}
list_orders = {}

navigator_symbol = "/" # This will make the program runnable on any unix based enviroument because it has differnet file system
if os.name == "nt":
    navigator_symbol = "\\" # This will make the program runnable on Windows

def add_item(name, catagory, price, *discount):
	#add new data into the list
	#read and write lists from the file
	item = ManClass.item()
	item.set_name(name)
	item.set_catagory(catagory)
	item.set_price(price)
	#default should be 1.0
	if discount:
		item.set_discount(discount)

	list_items[name] = item

def add_order(name):
	#add order
	#copy and paste selected item to order list
	if list_items:
		list_orders[name] = copy.deepcopy(list_items[name])
		return True
	else:
		print("Options do not exist")
		return False

def add_modif(name, ):
	#select food options
	#read and write the list
	pass

def edit_item(name, ):
	#edit item data
	#read and write the list
	pass

def edit_order():
	#edit order data
	#read and write the list
	pass	

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
	try:
		del list_orders[name]
		return True
	except KeyError:
		print("Option does not exist")
		return False

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
	if list_orders:
		return list_orders
	else:
		print("Order is empty")
		return False

def pay_order():
	#send order data to DB
	pass

def report_sale(date):
	#call analized report from DB
	pass
