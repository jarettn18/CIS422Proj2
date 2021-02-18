
#ManCus
#This module have functions for users

import os

#Global lists
list_foods = {}
list_drinks = {}
list_others = {}
list_orders = {}

navigator_symbol = "/" # This will make the program runnable on any unix based enviroument because it has differnet file system
if os.name == "nt":
    navigator_symbol = "\\" # This will make the program runnable on Windows

def add_menu():
	#add new data into the list
	#read and write lists from the file?
	pass

def add_order():
	#add order
	#read and write the list
	pass

def add_modif():
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

def show_order():
	#present orders from list
	#read the list
	pass

def pay_order():
	#send order data to DB
	pass

def report_sale():
	#call analized report from DB
	pass