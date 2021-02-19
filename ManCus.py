
#ManCus
#This module have functions for users

import os
import ManDB
import ManRcpt
#Global lists
list_menus = {}
#talk to ui
list_orders = {}

navigator_symbol = "/" # This will make the program runnable on any unix based enviroument because it has differnet file system
if os.name == "nt":
    navigator_symbol = "\\" # This will make the program runnable on Windows

def add_menu(name, catagory, ):
	#add new data into the list
	#read and write lists from the file
	pass

def add_order(name, ):
	#add order
	#read and write the list
	pass

def add_modif(name):
	#select food options
	#read and write the list
	pass

def edit_order():
	#edit order data
	#read and write the list
	pass	

def delete_menu():
	#delete menu from list
	#read and write lists from the file?
	pass	

def delete_order():
	#delete order from list
	#read and write the list
	pass	

def show_menu():
	#present orders from list
	#read the orders
	pass

def show_order():
	#present orders from list
	#read the orders
	pass

def pay_order():
	#send order data to DB
	ManDB()
	{} = {}
	pass

def report_sale(date):
	#call analized report from DB
	md = ManDB()
	md.report(date)
	pass
