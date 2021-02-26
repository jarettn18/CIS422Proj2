import ManUI
from ManCus import *
import ManDB
import ManClass
from ManReport import *
#Testing
import datetime

def main():
    # start everything from this main functions -- UI, Database, blah blah blah
	d = datetime.date.today()
	add_item('pepsi', 'drink', 2.5)
	add_item('papeyes', 'sandwitch', 5.5)

	add_order('pepsi', 3)
	add_order('papeyes', 3)
	print(show_order())
	print(pay_order('jay'))
	print(get_sale_list(d, d))
	print(total_sale_by_date(d, d))
	print(total_profit_by_date(d, d))

	add_order('pepsi', 1)
	add_order('papeyes', 2)
	print(show_order())
	print(pay_order('poom'))
	print(get_sale_list(d, d))
	print(total_sale_by_date(d, d))
	print(total_profit_by_date(d, d))

	print(report_by_item(d, d))
	print(report_by_category(d, d))

if __name__ == '__main__':
    main()
