"""
*   Report Module
*   Description: Module with all the reporting functionsd
*   Date: 21 Feb 2021
*   Last Created by: Jay Shin
*   Edit History: 25 Feb 2021 - Jay Shin
*                 v1.0: Creating all the function.
                  10 March 2021 - Jay Shin
                  v1.5: wrap up.
                  11 March 2021 - Jay Shin
                  v2.0: Add employee managing function.
"""
import datetime
import ManDB
'''
    This is report module
    Whenever user request report from one of these functions
    this module returns analysis of input date period
'''
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
    if sales:
        delta = datetime.timedelta(days=1)
        while start_date <= end_date:
            total_sale = sales[start_date][-1][0]
            sales[start_date] = total_sale
            start_date += delta
        return sales
    else:
        print("Invalid Input")
        return False

def total_profit_by_date(start_date, end_date):
    '''
    This function read all the receipts between input dates
    Returns total profit made in each date
    '''
    sales = get_sale_list(start_date, end_date)
    if sales:
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
    else:
        print("Invalid Input")
        return False

def report_by_item(start_date, end_date):
    '''
    This function read all the receipts between input dates
    Returns total amount of each sold item by date in range
    '''
    sales = get_sale_list(start_date, end_date)
    if sales:
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
    else:
        print("Invalid Input")
        return False

def report_by_category(start_date, end_date):
    '''
    This function read all the receipts between input dates
    Returns total amount of each sold category by date in range
    '''
    sales = get_sale_list(start_date, end_date)
    if sales:
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
    else:
        print("Invalid Input")
        return False

def daily_worktime_report(name, start_date, end_date):
    '''
    This function read all the employee log data between input dates
    Returns total amount of individual work time by date in range
    '''
    if isinstance(name, str):
        delta = datetime.timedelta(days=1)
        #   reading WorkTimeDatabase
        wtdb = ManDB.WorkTimeDatabase()
        wtdb.start_session()
        wts = wtdb.read_db()
        log_check = {}
        for wt in wts:
            if wt.name == name:
                if wt.date not in log_check:
                    log_check[wt.date] = wt.work_time
                else:
                    log_check[wt.date] += wt.work_time
            else:
                print("Invalid Input")
                return False
        #   Checking and adding worktime and its sum
        if start_date in log_check:
            ret_dic = {}
            while start_date <= end_date:
                ret_dic[start_date] = log_check[start_date]
                start_date += delta
        return ret_dic
    else:
        print("Invalid Input")
        return False

def total_worktime_report(name, start_date, end_date):
    '''
    This function read all the employee log data between input dates
    Returns total amount of individual work time by input period
    '''
    if isinstance(name, str):
        delta = datetime.timedelta(days=1)
        #   reading WorkTimeDatabase
        wtdb = ManDB.WorkTimeDatabase()
        wtdb.start_session()
        wts = wtdb.read_db()
        log_check = {}
        for wt in wts:
            if wt.name == name:
                if wt.date not in log_check:
                    log_check[wt.date] = wt.work_time
                else:
                    log_check[wt.date] += wt.work_time
            else:
                print("Invalid Name")
                return False
        #   Checking and adding worktime to get total
        if start_date in log_check:
            ret = log_check[start_date]
            start_date += delta
            while start_date <= end_date:
                if start_date in log_check:
                    ret += log_check[start_date]
                    start_date += delta
        return ret
    else:
        print("Invalid Input")
        return False

def pay_employee(name, wage, start_date, end_date):
    '''
    calculate total payment for the employee
    wage must be bigger than zero
    '''
    if isinstance(name, str):
        if wage > 0.0:
            wt = total_worktime_report(name, start_date, end_date)
            #datetime delta need to be changed into seconds
            #to calculate hours and minutes
            wtsec = wt.seconds
            wthour = wtsec//3600
            wtmin = (wtsec//60)%60
            wt = wthour + (wtmin/60)
            pay = wage * wt
            return pay
        else:
            print("Invalid Wage")
            return False    
    else:
        print("Invalid Name")
        return False

