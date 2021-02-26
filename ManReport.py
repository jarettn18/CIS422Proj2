
'''
    This is report module
    Whenever user request report from one of these functions
    this module returns analysis of input date period
'''
import datetime
import ManDB

def get_sale_list(start_date, end_date):
    '''
    This function read all receipts in input date period
    '''
    try:
        receiptdb = ManDB.ReceiptDatabase()
        receiptdb.start_session()
        ret = receiptdb.get_period(start_date, end_date)
    except ValueError:
        print("Invalid Input")
        ret = False
    return ret

def total_sale_by_date(start_date,end_date):
    '''
    This function read all the receipts between input dates
    Returns total sale amount by date in range
    '''
    sales = get_sale_list(start_date, end_date)
    delta = datetime.timedelta(days=1)
    while start_date <= end_date:
        total_sale = sales[start_date][-1][0]
        sales[start_date] = total_sale
        start_date += delta
    return sales

def total_profit_by_date(start_date, end_date):
    '''
    This function read all the receipts between input dates
    Returns total profit made in each date
    '''
    sales = get_sale_list(start_date, end_date)
    delta = datetime.timedelta(days=1)
    while start_date <= end_date:
        tot = 0.0
        prev_num = 0
        for sale in sales[start_date]:
            #check if the sale is still in same order
            if sale.number != prev_num:
                prev_num = sale.number
                tot += sale.price
        sales[start_date] = tot
        start_date += delta
    return sales

def report_by_item(start_date, end_date):
    '''
    This function read all the receipts between input dates
    Returns total amount of each sold item by date in range
    '''
    sales = get_sale_list(start_date, end_date)
    delta = datetime.timedelta(days=1)
    while start_date <= end_date:
        item_dic = {}
        for sale in sales[start_date]:
            if sale.orders not in item_dic:
                item_dic[sale.orders] = sale.amount
            else:
                item_dic[sale.orders] += sale.amount
        sales[start_date] = item_dic
        start_date += delta
    return sales

def report_by_category(start_date, end_date):
    '''
    This function read all the receipts between input dates
    Returns total amount of each sold category by date in range
    '''
    sales = get_sale_list(start_date, end_date)
    delta = datetime.timedelta(days=1)
    #   reading ItemDatabase to make category check dictionary
    itemdb = ManDB.ItemDatabase()
    itemdb.start_session()
    items = itemdb.read_db()
    category_check = {}
    for item in items:
        category_check[item.name] = item.category
    #   Checking and adding category and its amount
    while start_date <= end_date:
        category_dic = {}
        for sale in sales[start_date]:
            category = category_check[sale.orders]
            if category not in category_dic:
                category_dic[category] = sale.amount
            else:
                category_dic[category] += sale.amount   
        sales[start_date] = category_dic
        start_date += delta
    return sales

#Not sure if we need this
def report_by_date(start_date, end_date):
    pass
