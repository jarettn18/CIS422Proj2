import ManUI
from ManCus import *
import ManDB
import ManClass

#Testing
import datetime

def main():
    # start everything from this main functions -- UI, Database, blah blah blah
	d = datetime.date.today()
	add_item('pepsi', 'drink', 2.5)
	show_item()
	add_order('pepsi', 69)
	show_order()
	print(pay_order('jay'))
	print(report_sale(d, d))

if __name__ == '__main__':
    main()
