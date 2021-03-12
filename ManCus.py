
# ManCus
# This module have functions for users
"""
*   Description: Functions for Point of Sales
*   Date: 10 Mar 2021
*   Last Created by: Theodore Yun
*   Edit History: v1.0: Jay Basic functions
*                  20 Feb 2021
*                  v1.1: Jay end of basic functions
*                  20 Feb 2021
*                  v1.2: Fix edit_order, pay_order based on modification on ManClass.py
"""

import copy
import os
import ManDB
import ManClass

# Global lists
list_items = {}
# read the newest item list
list_dict = {'list_orders': ManClass.receipt()}

navigator_symbol = "/" # This will make the program runnable on any unix based enviroument because it has differnet file system
if os.name == "nt":
    navigator_symbol = "\\" # This will make the program runnable on Windows

# ManCus ONLY
"""
*   Function: set_itemlist
*   Description: Create item list from database
*  Date: 10 Mar 2021
*   Last Created by: Theodore Yun
*   Edit History: v1.0: Jay Basic functions
*                  20 Feb 2021
*                  v1.1: Jay end of basic functions
"""
def set_itemlist():
    # Just to set item list from database
    itemdb = ManDB.ItemDatabase()
    itemdb.start_session()
    items = itemdb.read_db()
    for item in items:
        data = ManClass.item()
        data.name = item[0]
        data.category = item[1]
        data.price = item[2]
        data.discount = item[3]
        list_items[item[0]] = data
    return True

# fresh item list from database
set_itemlist()

"""
*   Function: add_item
*   Description: Add item to item list
*   Date: 10 Mar 2021
*   Last Created by: Theodore Yun
*   Edit History: v1.0: Jay Basic functions
*                  20 Feb 2021
*                  v1.1: Jay end of basic functions
"""
# Discount will be optional argument by using *
def add_item(name, category, price, discount=0, add_to_db=True):
    try:
        # add new data into the list
        # read and write lists from the file
        item = ManClass.item()
        item.set_name(name)
        item.set_category(category)
        item.set_price(price)
        # default should be 1.0, if the discount rate is 10% it would be 0.9
        if discount:
            item.set_discount(discount)

        list_items[name] = item
        if add_to_db:
            itemdb = ManDB.ItemDatabase()
            itemdb.start_session()
            itemdb.add_item(item)
        return True
    except:
        return False
"""
*   Function: query_items
*   Description: Add item to menu dictionary
*   Date: 10 Mar 2021
*   Last Created by: Theodore Yun
*   Edit History: v1.0: Jay Basic functions
*                  20 Feb 2021
*                  v1.1: Jay end of basic functions
"""
def query_items():
    menu_dict = {}
    itemdb = ManDB.ItemDatabase()
    itemdb.start_session()
    for i in itemdb.read_db():
        if i[1] not in menu_dict:
            items = [(i[0], i[2], i[3])]
            menu_dict[i[1]] = items
        else:
            menu_dict[i[1]].append((i[0], i[2], i[3]))
    return menu_dict

"""
*   Function: add_order
*   Description: Make order with item name and amount
*   Date: 10 Mar 2021
*   Last Created by: Theodore Yun
*   Edit History: v1.0: Jay Basic functions
*                  20 Feb 2021
*                  v1.1: Jay end of basic functions
"""
def add_order(name, amount):
    # add order
    # copy and paste selected item to order list
    ret = list_items[name]
    if ret:
        order = ManClass.order()
        order.set_item(ret)
        order.set_amount(amount)
        ret = list_dict['list_orders'].add_order(order)
    # if item is not on list, then prints the following
    else:
        print("Item does not exist")
        ret = False
    return ret

"""
*   Function: edit_item
*   Description: Edit the features of item ex)name, category, price, and discount
*   Date: 10 Mar 2021
*   Last Created by: Theodore Yun
*   Edit History: v1.0: Jay Basic functions
*                  20 Feb 2021
*                  v1.1: Jay end of basic functions
"""
def edit_item(name, factor, newkey):
    # edit item data
    # read and write the list
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

"""
*   Function: edit_order
*   Description: Edit the features of order
*   Date: 10 Mar 2021
*   Last Created by: Theodore Yun
*   Edit History: v1.0: Jay Basic functions
*                  20 Feb 2021
*                  v1.1: Jay end of basic functions
"""
def edit_order(name, factor, newkey):
    # edit order data
    # read and write the list
    return list_dict['list_orders'].edit_order(name, factor, newkey)

"""
*   Function: delete_menu
*   Description: deleting function for item from item list
*   Date: 10 Mar 2021
*   Last Created by: Theodore Yun
*   Edit History: v1.0: Jay Basic functions
*                  20 Feb 2021
*                  v1.1: Jay end of basic functions
"""
def delete_menu(name):
    # delete menu from list
    # read and write lists from the file?
    try:
        del list_items[name]
        itemdb = ManDB.ItemDatabase()
        itemdb.start_session()
        return itemdb.delete_item(name)
    except KeyError:
        print("Option does not exist")
        return False

"""
*   Function: delete_order
*   Description: deleting function the order from order list
*   Date: 10 Mar 2021
*   Last Created by: Theodore Yun
*   Edit History: v1.0: Jay Basic functions
*                  20 Feb 2021
*                  v1.1: Jay end of basic functions
"""
def delete_order(name):
    # delete order from list
    # read and write the list
    return list_dict['list_orders'].delete_order(name)

"""
*   Function: show_item
*   Description: display the items that are in current item list
*   Date: 10 Mar 2021
*   Last Created by: Theodore Yun
*   Edit History: v1.0: Jay Basic functions
*                  20 Feb 2021
*                  v1.1: Jay end of basic functions
"""
def show_item():
    # present item from list
    # read the item
    if list_items:
        return list_items
    else:
        print("Option is empty")
        return False

"""
*   Function: show_order
*   Description: display the items that are in current order
*   Date: 10 Mar 2021
*   Last Created by: Theodore Yun
*   Edit History: v1.0: Jay Basic functions
*                  20 Feb 2021
*                  v1.1: Jay end of basic functions
"""
def show_order():
    # present orders from list
    # read the orders
    return list_dict['list_orders'].get_orders()

"""
*   Function: get_total
*   Description: get total price of each order, get_total from ManClass.get_total
*   Date: 10 Mar 2021
*   Last Created by: Theodore Yun
*   Edit History: v1.0: Jay Basic functions
*                  20 Feb 2021
*                  v1.1: Jay end of basic functions
"""
def get_total():
    # get total price of the each order
    return list_dict['list_orders'].get_total()

"""
*   Function: pay_order
*   Description: display receipt from ManClass.get_receipt
*   Date: 10 Mar 2021
*   Last Created by: Theodore Yun
*   Edit History: v1.0: Jay Basic functions
*                  20 Feb 2021
*                  v1.1: Jay end of basic functions
"""
def pay_order(customer):
    if customer:
        list_dict['list_orders'].set_customer(customer)
        # database move
        try:
            ret = list_dict['list_orders'].get_receipt()
            receiptdb = ManDB.ReceiptDatabase()
            receiptdb.start_session()
            receiptdb.add_receipt(list_dict['list_orders'])
            list_dict['list_orders'] = ManClass.receipt()
        except TypeError:
            return False
        except:
            return False
    else:
        print("Invalid Input")
        ret = False
    return ret
