"""
*	Title:			ManUI.py
*	Project:		ManEz
*	Description:	UI File for ManEz Program
*
*	Team:			TAP2J
*
*	Last Created By: Jarett Nishijo
*
*	Date Created: 22 Feb 2022
"""
import tkinter as tk
import tkinter.ttk as ttk
import ManCus as cus
import ManStaff as stf
import ManReport as rep
import datetime as dt
import copy as cp

BG_COLOR = 'gray'

"""
*   Class: App
*   Description: Core Class that ManEz runs through
*
*   Date: 5 Mar 2021
*   Created by: Jarett Nishijo
*   Edit History: 5 Mar 2021 - Jarett Nishijo
*					v1.0 - Created
"""
class App(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.grid()
		self.clocked = []
		self.active = None
		stf.read_emp_db()

	"""
	*   Function: reset
	*   Description: Clear widgets on screen
	*
	*   Date: 5 Mar 2021
	*   Created by: Alex Villa
	*   Edit History: 5 Mar 2021 - Alex Villa
	*					v1.0 - Created
	"""
	def reset(self):
		"""Reset the list of participants"""
		for child in self.master.winfo_children():
			child.destroy()

	"""
	*   Function: init_screen
	*   Description: Creates initialization screen upon installation
	*
	*   Date: 5 Mar 2021
	*   Created by: Jarett Nishijo
	*   Edit History: 5 Mar 2021 - Jarett Nishijo
	*					v1.0 - Created
	"""
	def init_screen(self):

		def _init_submit_button():
			name = name_var.get()
			pin = pin_var.get()
			confirm = confirm_pin_var.get()

			if (pin != confirm):
				confirm_pin_label = tk.Label(self.master, background=BG_COLOR, text="Pin Must Be Equal",
											 font=("Calibre", 15, 'bold'))
				confirm_pin_label.grid(row=5, column=2)
			else:
				# insert name/pin in database
				stf.add_employee(name.lower(), None, pin, firstrun=True)
				name_var.set("")
				pin_var.set("")
				for widget in self.master.winfo_children():
					widget.destroy()

				self.main_login_screen()

		for i in range(6):
			tk.Grid.rowconfigure(self.master, i, weight=1)
			tk.Grid.columnconfigure(self.master, i, weight=1)
		"""
		for r in range(6):
			for c in range(6):
				tk.Label(self.master, text='R%s/C%s' % (r, c),
						 borderwidth=1).grid(row=r, column=c)
		"""
		# Choose Background Color
		BG_COLOR = 'gray'
		self.master.configure(background=BG_COLOR)

		# Create Labels
		greeting = tk.Label(background=BG_COLOR, text="Welcome to ManEz", font=("Arial", 30, 'bold'))
		greeting.grid(row=0, column=2, columnspan=2)
		create_profile = tk.Label(background=BG_COLOR, text="Create Administrator Profile", font=("Arial", 25))
		create_profile.grid(row=1, column=2, columnspan=2)

		name_var = tk.StringVar()
		pin_var = tk.StringVar()
		confirm_pin_var = tk.StringVar()

		name_label = tk.Label(self.master, background=BG_COLOR, text="Name", font=("Calibre", 20, 'bold'))
		name_entry = tk.Entry(self.master, textvariable=name_var, font=("Calibre", 20))

		pin_label = tk.Label(self.master, background=BG_COLOR, text="Pin", font=("Calibre", 20, 'bold'))
		pin_entry = tk.Entry(self.master, textvariable=pin_var, font=("Calibre", 20))

		confirm_pin_label = tk.Label(self.master, background=BG_COLOR, text="Confirm Pin", font=("Calibre", 20, 'bold'))
		confirm_pin_entry = tk.Entry(self.master, textvariable=confirm_pin_var, font=("Calibre", 20))

		name_label.grid(row=2, column=2)
		name_entry.grid(row=2, column=3)

		pin_label.grid(row=3, column=2)
		pin_entry.grid(row=3, column=3)

		confirm_pin_label.grid(row=4, column=2)
		confirm_pin_entry.grid(row=4, column=3)

		submit = tk.Button(self.master, text="Submit", command=_init_submit_button, font=("Calibre", 20, 'bold'))
		submit.grid(row=5, column=3)

	"""
	*   Function: main_login_screen
	*   Description: Creates initialization screen for future program launches
	*
	*   Date: 5 Mar 2021
	*   Created by: Jarett Nishijo
	*   Edit History: 5 Mar 2021 - Jarett Nishijo
	*					v1.0 - Created
	"""
	def main_login_screen(self, clear_screen=True):
		self.active=None
		if clear_screen:
			self.reset()

		def _order_history():
			self.reset()
			print("Order History")
			date = dt.datetime.now()
			date = date.strftime("%d %B %Y")
			splits = date.split()
			tup = (int(splits[2]), splits[1], int(splits[0]))

			analysis = ShowSaleData(self.master)
			analysis.findBySale(tup, tup)

			back = tk.Button(self.master, text="Back", command=lambda: self.main_login_screen(),
							 font=("Calibre", 20, 'bold'))
			back.grid(row=2, column=1)

			title = tk.Label(background=BG_COLOR, text="Order History", width="30", font=("Arial", 50, 'bold'))
			title.grid(row=1, column=2, columnspan=2)

		if len(self.clocked) > 0:
			clocked_in = ""
			for emp in self.clocked:
				clocked_in += emp
				clocked_in += ", "
			clocked_in = clocked_in[:len(clocked_in) - 2]
			user = tk.Label(background=BG_COLOR, text=("Clocked in as: " + clocked_in), font=("Arial", 25, 'bold'))
			user.grid(row=3, column=4, columnspan=2)

		for i in range(6):
			tk.Grid.rowconfigure(self.master, i, weight=1)
			tk.Grid.columnconfigure(self.master, i, weight=1)

		# Choose Background Color
		self.master.configure(background=BG_COLOR)

		greeting = tk.Label(background=BG_COLOR, text="ManEz", font=("Arial", 25, 'bold'))
		greeting.grid(row=0, column=2, columnspan=2)

		"""
		for r in range(6):
			for c in range(6):
				tk.Label(self.master, text='R%s/C%s' % (r, c),
						 borderwidth=1).grid(row=r, column=c)
		"""

		new_order = tk.Button(self.master, text="New Order", command=lambda: self.order_screen(),
							  font=("Calibre", 50, 'bold'))
		new_order.grid(row=1, column=1)

		order_hist = tk.Button(self.master, text="Order History", command=_order_history, font=("Calibre", 50, 'bold'))
		order_hist.grid(row=1, column=4)

		settings = tk.Button(self.master, text="Settings", command=lambda: self.pin_screen("settings"),
							 font=("Calibre", 30, 'bold'))
		settings.grid(row=4, column=1)

		clock_in = tk.Button(self.master, text="Clock In", command=lambda: self.pin_screen("clock"),
							 font=("Calibre", 30, 'bold'))
		clock_in.grid(row=4, column=4)

		clock_out = tk.Button(self.master, text="Clock Out", command=lambda: self.pin_screen("clock_out"),
							  font=("Calibre", 30, 'bold'))
		clock_out.grid(row=5, column=4)

		name_label = tk.Label(self.master, background=BG_COLOR, text="Administrator Use Only",
							  font=("Calibre", 20, 'bold'))
		name_label.grid(row=3, column=1, pady=20)

	"""
	*   Function: pin_screen
	*   Description: Creates screen for pin and account verification
	*
	*   Date: 5 Mar 2021
	*   Created by: Jarett Nishijo
	*   Edit History: 5 Mar 2021 - Jarett Nishijo
	*					v1.0 - Created
	"""
	def pin_screen(self, mode):
		self.reset()

		def login(mode):
			name = name_var.get()
			pin = pin_var.get()
			# login with pin number
			if mode == "settings":
				if stf.is_admin(name.lower()) and stf.admin_entry(name.lower(), pin) == 39:
					self.active = name
					self.settings_menu()
				else:
					admin_label = tk.Label(self.master, background=BG_COLOR, text="Invalid Login",
										   font=("Calibre", 20, "bold"))
					admin_label.grid(row=0, column=4)
			elif mode == "clock":
				succ = stf.login(name.lower(), pin)
				msg, success = stf.get_message(succ)
				if (success == True):
					self.clocked.append(name)
					self.main_login_screen()
				else:
					self.main_login_screen(True)
			elif mode == "clock_out":
				succ = stf.logout(name.lower(), pin)
				msg, success = stf.get_message(succ)
				if (success == True):
					self.clocked.remove(name)
					self.main_login_screen()
				else:
					self.main_login_screen()

		def add_char(c):
			pin = pin_var.get()
			pin_var.set(pin + c)

		def delete_char():
			pin = pin_var.get()
			pin_var.set(pin[:len(pin) - 1])

		for i in range(7):
			tk.Grid.rowconfigure(self.master, i, weight=1)
			tk.Grid.columnconfigure(self.master, i, weight=1)
		# Choose Background Color
		self.master.configure(background=BG_COLOR)
		"""
		for r in range(7):
			for c in range(7):
				tk.Label(self.master, text='R%s/C%s' % (r, c),
						 borderwidth=1).grid(row=r, column=c)
		"""
		name_var = tk.StringVar()
		name_label = tk.Label(self.master, background=BG_COLOR, text="Name", font=("Calibre", 20, 'bold'))
		name_entry = tk.Entry(self.master, textvariable=name_var, font=("Calibre", 18))

		name_label.grid(row=0, column=2)
		name_entry.grid(row=0, column=3)

		pin_var = tk.StringVar()
		pin_label = tk.Label(self.master, background=BG_COLOR, text="Pin", font=("Calibre", 20, 'bold'))
		pin_entry = tk.Entry(self.master, textvariable=pin_var, font=("Calibre", 18))

		pin_label.grid(row=1, column=2)
		pin_entry.grid(row=1, column=3)

		button1 = tk.Button(self.master, text="1", command=lambda: add_char("1"), font=("Calibre", 50, 'bold'))
		button1.grid(row=2, column=2)

		button2 = tk.Button(self.master, text="2", command=lambda: add_char("2"), font=("Calibre", 50, 'bold'))
		button2.grid(row=2, column=3)

		button3 = tk.Button(self.master, text="3", command=lambda: add_char("3"), font=("Calibre", 50, 'bold'))
		button3.grid(row=2, column=4)

		button4 = tk.Button(self.master, text="4", command=lambda: add_char("4"), font=("Calibre", 50, 'bold'))
		button4.grid(row=3, column=2)

		button5 = tk.Button(self.master, text="5", command=lambda: add_char("5"), font=("Calibre", 50, 'bold'))
		button5.grid(row=3, column=3)

		button6 = tk.Button(self.master, text="6", command=lambda: add_char("6"), font=("Calibre", 50, 'bold'))
		button6.grid(row=3, column=4)

		button7 = tk.Button(self.master, text="7", command=lambda: add_char("7"), font=("Calibre", 50, 'bold'))
		button7.grid(row=4, column=2)

		button8 = tk.Button(self.master, text="8", command=lambda: add_char("8"), font=("Calibre", 50, 'bold'))
		button8.grid(row=4, column=3)

		button9 = tk.Button(self.master, text="9", command=lambda: add_char("9"), font=("Calibre", 50, 'bold'))
		button9.grid(row=4, column=4)

		button0 = tk.Button(self.master, text="0", command=lambda: add_char("0"), font=("Calibre", 50, 'bold'))
		button0.grid(row=5, column=3)

		button0 = tk.Button(self.master, text="DEL", command=delete_char, font=("Calibre", 30, 'bold'))
		button0.grid(row=5, column=4)

		if mode == "clock" or mode == "settings":
			login_button = tk.Button(self.master, text="login", command=lambda: login(mode),
									 font=("Calibre", 25, 'bold'))
			login_button.grid(row=1, column=4)
		else:
			logout_button = tk.Button(self.master, text="logout", command=lambda: login(mode),
									  font=("Calibre", 25, 'bold'))
			logout_button.grid(row=1, column=4)

		back = tk.Button(self.master, text="Back", command=lambda: self.main_login_screen(),
						 font=("Calibre", 20, 'bold'))
		back.grid(row=1, column=1)

	"""
	*   Function: settings_menu
	*   Description: Creates menu screen for the settings tab
	*
	*   Date: 5 Mar 2021
	*   Created by: Alex Villa
	*   Edit History: 5 Mar 2021 - Alex Villa
	*					v1.0 - Created
	"""
	def settings_menu(self):
		self.reset()

		title = tk.Label(self.master, text='ManEz Settings', font=("Calibre", 20, 'bold'), background=BG_COLOR)
		title.grid(row=1, column=3)

		back = tk.Button(self.master, text="Back", command=lambda: self.main_login_screen(),
						 font=("Calibre", 20, 'bold'))
		back.grid(row=1, column=2)

		new_account = tk.Button(self.master, cursor='circle', command=lambda: self.new_account(),
								text='Create New Account', width='25', height='10', font=("Calibre", 20, 'bold'))
		new_account.grid(row=2, column=2)

		sales = tk.Button(self.master, cursor='circle', command=lambda: self.analysis(), text='Sales Analytics',
						  width='25', height='10',
						  font=("Calibre", 20, 'bold'))
		sales.grid(row=2, column=4)

		edit = tk.Button(self.master, cursor='circle', text='Menu Settings',
						 command=lambda: self.add_menu(), width='25', height='10',
						 font=("Calibre", 20, 'bold'))
		edit.grid(row=3, column=4)

		employee = tk.Button(self.master, cursor='circle', command=lambda: self.emp_analysis(),
							 text='Employee Analytics', width='25', height='10',
							 font=("Calibre", 20, 'bold'))
		employee.grid(row=3, column=2)

	"""
	*   Function: new_account
	*   Description: Creates new account screen
	*
	*   Date: 8 Mar 2021
	*   Created by: Alex Villa
	*   Edit History: 8 Mar 2021 - Alex Villa
	*					v1.0 - Created
	"""
	def new_account(self):
		self.reset()

		title = tk.Label(self.master, text='Create New Account', font=("Calibre", 20, 'bold'), background=BG_COLOR)

		title.grid(row=1, column=3)

		back = tk.Button(self.master, text="Back", command=lambda: self.settings_menu(),
						 font=("Calibre", 20, 'bold'))
		back.grid(row=1, column=2)

		name_var = tk.StringVar()
		pin_var = tk.StringVar()
		confirmvar = tk.StringVar()

		name_label = tk.Label(self.master, text="Name", font=("Calibre", 18, 'bold'), background=BG_COLOR)
		name_entry = tk.Entry(self.master, textvariable=name_var, font=("Calibre", 16))

		pin_label = tk.Label(self.master, text="Pin", font=("Calibre", 18, 'bold'), background=BG_COLOR)
		pin_entry = tk.Entry(self.master, textvariable=pin_var, font=("Calibre", 16))

		confirm_label = tk.Label(self.master, text="Confirm Pin", font=("Calibre", 18, 'bold'), background=BG_COLOR)
		confirm_entry = tk.Entry(self.master, textvariable=confirmvar, font=("Calibre", 16))

		submit = tk.Button(self.master, text="Create",
						   command=lambda: self.create_account(name_var.get(), pin_var.get(),
															   confirmvar.get()), font=("Calibre", 20, 'bold'))


		name_label.grid(row=2, column=2, pady=20)
		name_entry.grid(row=2, column=3, columnspan=2, pady=20)

		pin_label.grid(row=3, column=2, pady=20)
		pin_entry.grid(row=3, column=3, columnspan=2, pady=20)

		confirm_label.grid(row=4, column=2, pady=20)
		confirm_entry.grid(row=4, column=3, columnspan=2, pady=20)

		submit.grid(row=5, column=3)

	"""
	*   Function: create_account
	*   Description: Creates account and adds to database
	*
	*   Date: 5 Mar 2021
	*   Created by: Alex Villa
	*   Edit History: 5 Mar 2021 - Alex Villa
	*					v1.0 - Created
	"""
	def create_account(self, name: str, pin: str, confirm: int):
		confirm_pin_label = tk.Label(self.master, background=BG_COLOR,
									 font=("Calibre", 15, 'bold'))
		if (pin != confirm):
			confirm_pin_label['text'] = "Pin Must Be Equal"
			confirm_pin_label.grid(row=6, column=3)
		else:
			# insert name/pin in database
			if self.active:
				stf.add_employee(name.lower(), self.active.lower(), pin)
				self.settings_menu()
			else:
				confirm_pin_label['text'] = "Need a clocked in Admin to create account"
				confirm_pin_label.grid(row=6, column=3)

	"""
	*   Function: add_menu
	*   Description: Creates the Add Menu Screen
	*
	*   Date: 5 Mar 2021
	*   Created by: Alex Villa
	*   Edit History: 5 Mar 2021 - Alex Villa
	*					v1.0 - Created
	"""
	def add_menu(self):
		self.reset()

		curr_men_frame = tk.Frame(self.master, background=BG_COLOR)
		curr_men_frame.grid(row=1, column=4, rowspan=5)

		item_frames = UpdatingCategories(curr_men_frame)
		item_frames.show_cat_list()

		title = tk.Label(self.master, text='Add New Menu', font=("Calibre", 20, 'bold'), background=BG_COLOR)
		title.grid(row=1, column=2)

		back = tk.Button(self.master, text="Back", command=lambda: self.settings_menu(),
						 font=("Calibre", 20, 'bold'))
		back.grid(row=1, column=1)

		name_var = tk.StringVar()
		price_var = tk.DoubleVar()
		cat_var = tk.StringVar()

		header = tk.Label(self.master, text="New Item", font=("Calibre", 18, 'bold'), background=BG_COLOR)
		item_name = tk.Label(self.master, text="Name", font=("Calibre", 16, 'bold'), background=BG_COLOR)
		name_entry = tk.Entry(self.master, textvariable=name_var, font=("Calibre", 16))

		item_price = tk.Label(self.master, text="Price", font=("Calibre", 16, 'bold'), background=BG_COLOR)
		price_entry = tk.Entry(self.master, textvariable=price_var, font=("Calibre", 16))

		item_category = tk.Label(self.master, text="Category", font=("Calibre", 16, 'bold'), background=BG_COLOR)
		category_entry = tk.Entry(self.master, textvariable=cat_var, font=("Calibre", 16))

		submit = tk.Button(self.master, text="Add",
						   command=lambda: item_frames.insert_item(name_var.get(), cat_var.get(), price_var.get(),
																   name_entry,
																   price_entry),
						   font=("Calibre", 20, 'bold'), width="10", height="3")

		header.grid(column=2, row=2)

		item_name.grid(column=1, row=3)
		name_entry.grid(column=2, row=3)

		item_price.grid(column=1, row=4)
		price_entry.grid(column=2, row=4)

		item_category.grid(column=1, row=5)
		category_entry.grid(column=2, row=5)

		submit.grid(column=2, row=6, pady=20)

	"""
	*   Function: order_screen
	*   Description: Creates new order screen
	*
	*   Date: 8 Mar 2021
	*   Created by: Alex Villa
	*   Edit History: 8 Mar 2021 - Alex Villa
	*					v1.0 - Created
	"""
	def order_screen(self):
		self.reset()

		title_frame = tk.Frame(self.master, background=BG_COLOR)
		title_frame.grid(row=1, column=2, columnspan=2)

		title = tk.Label(title_frame, text='New Order', font=("Calibre", 20, 'bold'), background=BG_COLOR)
		title.grid(row=1, column=2)

		action_frame = tk.Frame(self.master)
		action_frame.grid(row=3, column=1, columnspan=4)

		category_buttons = DynamicMenu(action_frame)
		category_buttons.show_cat_list()

		back = tk.Button(title_frame, command=lambda: category_buttons.delete_whole_order(self), text="Back",
						 font=("Calibre", 20, 'bold'))
		back.grid(row=1, column=1)


		send_button = category_buttons.get_send_button()
		send_button['command'] = lambda: category_buttons.send_order(self)

	"""
	*   Function: analysis
	*   Description: Creates sales analytics widget
	*
	*   Date: 10 Mar 2021
	*   Created by: Alex Villa
	*   Edit History: 10 Mar 2021 - Alex Villa
	*					v1.0 - Created
	"""
	def analysis(self):
		self.reset()

		title_frame = tk.Frame(self.master, background=BG_COLOR)
		title_frame.grid(row=1, column=2, columnspan=3)

		back = tk.Button(title_frame, command=lambda: self.settings_menu(), text="Back", font=("Calibre", 20, 'bold'))
		back.pack(side=tk.LEFT)

		title = tk.Label(title_frame, text='Sales Analytics', background=BG_COLOR, font=("Calibre", 20, 'bold'),
						 width='20', height='5')
		title.pack(side=tk.LEFT)

		date = tk.Label(self.master, text='Date Range:', background=BG_COLOR, font=("Calibre", 16, 'bold'), width='15',
						height='5')
		date.grid(row=2, column=1)

		to = tk.Label(self.master, text='To:', background=BG_COLOR, font=("Calibre", 16, 'bold'), width='10',
					  height='5')
		to.grid(row=2, column=3)

		from_frame = tk.Frame(self.master)
		from_frame.grid(row=2, column=2)

		to_frame = tk.Frame(self.master)
		to_frame.grid(row=2, column=4)

		style = ttk.Style()
		style.configure("bg.TCombobox", forground=BG_COLOR, background=BG_COLOR)

		date_today = dt.date.today()
		year_today = date_today.year
		month_today = date_today.month
		day_today = date_today.day

		monthvar = tk.StringVar()
		month = ttk.Combobox(from_frame, state="readonly", style="bg.TCombobox", textvariable=monthvar,
							 font=("Calibre", 16, 'bold'), width='10', height='5')
		month['values'] = (
			'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
			'November',
			'December')
		month.pack(side=tk.LEFT)
		month.current(int(month_today) - 1)

		dayvar = tk.IntVar()
		day = ttk.Combobox(from_frame, state="readonly", style="bg.TCombobox", textvariable=dayvar,
						   font=("Calibre", 16, 'bold'), width='5', height='5')
		day['values'] = [x for x in range(1, 32)]
		day.pack(side=tk.LEFT)
		day.current(int(day_today) - 1)

		yearvar = tk.IntVar()
		year = ttk.Combobox(from_frame, state="readonly", style="bg.TCombobox", textvariable=yearvar,
							font=("Calibre", 16, 'bold'), width='5', height='5')
		year['values'] = (2021)
		year.pack(side=tk.LEFT)
		yearvar.set(int(year_today))

		tomonthvar = tk.StringVar()
		tomonth = ttk.Combobox(to_frame, state="readonly", style="bg.TCombobox", textvariable=tomonthvar,
							   font=("Calibre", 16, 'bold'), width='10', height='5')
		tomonth['values'] = (
			'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
			'November',
			'December')
		tomonth.pack(side=tk.LEFT)
		tomonth.current(int(month_today) - 1)

		todayvar = tk.IntVar()
		today = ttk.Combobox(to_frame, state="readonly", style="bg.TCombobox", textvariable=todayvar,
							 font=("Calibre", 16, 'bold'), width='5', height='5')
		today['values'] = [x for x in range(1, 32)]
		today.pack(side=tk.LEFT)
		today.current(int(day_today) - 1)

		toyearvar = tk.IntVar()
		toyear = ttk.Combobox(to_frame, state="readonly", style="bg.TCombobox", textvariable=toyearvar,
							  font=("Calibre", 16, 'bold'), width='5', height='5')
		toyear['values'] = (2021)
		toyear.pack(side=tk.LEFT)
		toyearvar.set(int(year_today))

		button_frame = tk.Frame(self.master, background=BG_COLOR, )
		button_frame.grid(row=2, column=5)

		saleData = ShowSaleData(self.master)

		findBy = tk.Label(button_frame, text='Find By:', background=BG_COLOR, font=("Calibre", 16, 'bold'),
						  width='20')
		findBy.pack(side=tk.TOP)

		findBySale = tk.Button(button_frame, width="10", background=BG_COLOR,
							   command=lambda: saleData.findBySale((yearvar.get(), monthvar.get(), dayvar.get()),
																   (toyearvar.get(), tomonthvar.get(), todayvar.get())),
							   text="Sales", font=("Calibre", 16, 'bold'))
		findBySale.pack(side=tk.TOP)

		findByItem = tk.Button(button_frame, width="10", background=BG_COLOR, command=lambda: saleData.findByItem((yearvar.get(), monthvar.get(), dayvar.get()),
																   (toyearvar.get(), tomonthvar.get(), todayvar.get())), text="Items",
							   font=("Calibre", 16, 'bold'))
		findByItem.pack(side=tk.TOP)

		findByCat = tk.Button(button_frame, width="10", background=BG_COLOR, command=lambda: saleData.findByCategory((yearvar.get(), monthvar.get(), dayvar.get()),
																   (toyearvar.get(), tomonthvar.get(), todayvar.get())),
							  text="Categories", font=("Calibre", 16, 'bold'))
		findByCat.pack(side=tk.TOP)

	"""
	*   Function: emp_analysis
	*   Description: Creates employee analytics widget
	*
	*   Date: 10 Mar 2021
	*   Created by: Alex Villa
	*   Edit History: 10 Mar 2021 - Alex Villa
	*					v1.0 - Created
	"""
	def emp_analysis(self):
		self.reset()

		title_frame = tk.Frame(self.master, background=BG_COLOR)
		title_frame.grid(row=1, column=3, columnspan=3)

		back = tk.Button(title_frame, command=lambda: self.settings_menu(), text="Back", font=("Calibre", 20, 'bold'))
		back.pack(side=tk.LEFT)

		title = tk.Label(title_frame, text='Employee Analytics', background=BG_COLOR, font=("Calibre", 20, 'bold'),
						 width='20', height='5')
		title.pack(side=tk.LEFT)

		data = ShowEmpData(self.master)
		data.show_employees()
		data.show_time_options()

"""
	*   Class: showEmpData
	*   Description: Class contains functions show employees data
	*
	*   Date: 10 Mar 2021
	*   Created by: Alex Villa
	*   Edit History: 10 Mar 2021 - Alex Villa
	*					v1.0 - Created
"""
class ShowEmpData(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
					   'September': 9, 'October': 10, 'November': 11, 'December': 12}
		self.ticket = tk.Text(self.master, font=("Calibre", 18, 'bold'))
		ys = tk.Scrollbar(self.master, orient='vertical', command=self.ticket.yview)
		self.ticket['yscrollcommand'] = ys.set
		self.ticket.grid(column=3, row=4, columnspan=4, rowspan=3)
		self.ticket['state'] = 'disabled'
		self.empty = True
		self.title = title = tk.Label(self.master, text='Employee Worklog', background=BG_COLOR, font=("Calibre", 20, 'bold'))
		title.grid(row=3, column=3, columnspan=4)
		self.button_grid = tk.Frame(self.master)
		self.button_grid.grid(column=2, row=3, rowspan=3)
		self.edit_grid = tk.Frame(self.master, background=BG_COLOR)
		self.edit_grid.grid(column=1, row=3, rowspan=3, padx=3)
		self.monthvar = tk.StringVar()
		self.dayvar = tk.IntVar()
		self.yearvar = tk.IntVar()
		self.tomonthvar = tk.StringVar()
		self.todayvar = tk.IntVar()
		self.toyearvar = tk.IntVar()
		self.employees = stf.get_emp_list()
		self.edit_menu = tk.Frame(self.master)
		self.this_color = "bisque2"
		self.uservar = tk.StringVar()
		self.passvar = tk.StringVar()
		self.error = None
		global EditIcon
		EditIcon = tk.PhotoImage(file="edit_icon.png")

	def show_employees(self):
		for child in self.button_grid.winfo_children():
			child.destroy()
		for child in self.edit_grid.winfo_children():
			child['command'] = None
			child.destroy()
		for emp in self.employees:
			new = tk.Button(self.button_grid, command=lambda j=emp: self.show_work_hours(j, (self.yearvar.get(), self.monthvar.get(), self.dayvar.get()),
																   (self.toyearvar.get(), self.tomonthvar.get(), self.todayvar.get())), text=f"{emp.capitalize()}", font=("Calibre", 16, 'bold'), width="15", height='3')
			edit = tk.Button(self.edit_grid, image=EditIcon, command=lambda k=emp: self.show_edit_menu(k), font=("Calibre", 16, 'bold'))
			edit.pack(side=tk.TOP, pady=11)
			new.pack(side=tk.TOP)

	def show_work_hours(self, emp, startdate: tuple, enddate: tuple):
		self.empty = True
		self.ticket['state'] = 'normal'
		self.ticket.delete('1.0', tk.END)
		start = dt.date(startdate[0], self.months[startdate[1]], startdate[2])
		end = dt.date(enddate[0], self.months[enddate[1]], enddate[2])
		self.title['text'] = f'show'
		punches = rep.daily_worktime_report(emp, start, end)
		total_work = rep.total_worktime_report(emp, start, end)
		if total_work:
			self.empty = False
			time = str(total_work).split(":")
			hr = time[0]
			minim = time[1]
			self.ticket.insert(tk.END, f"Showing Time Clock Data For {emp}\n")
			self.ticket.insert(tk.END, f"___________________________________\n")
			if punches:
				for entry in punches:
					self.ticket.insert(tk.END, f"Date: {entry} \t\t\t {str(punches[entry])}\n")
			else:
				self.ticket.insert(tk.END, f"No Work Data To Show\n")
		if self.empty:
			self.title['text'] = "No Orders To Show In Date Range"
			self.empty = True
		else:
			self.title['text'] = f" Showing Punches From {start} to {end} \t Total: {hr} Hours and {minim} Minutes"
		self.ticket['state'] = 'disabled'

	def show_edit_menu(self, emp):
		self.edit_menu.destroy()
		self.edit_menu = tk.Frame(self.master, background=self.this_color)
		self.edit_menu.grid(row=3,column=3,columnspan=4, rowspan=4, ipadx=20, ipady=20)
		title = tk.Label(self.edit_menu, text=f'Edit {emp}\n Role: {"Administrator" if self.employees[emp].is_admin() else "Employee"}', background=self.this_color, font=("Calibre", 20, 'bold'), width='20')
		title.pack(side=tk.TOP)
		curr_user = tk.Frame(self.edit_menu, background=self.this_color)
		user_label = tk.Label(curr_user, background=self.this_color, font=("Calibre", 14, 'bold'), width='24')
		user_entry = tk.Entry(curr_user, textvariable=self.uservar,font=("Calibre", 12, 'bold'), width='10')
		pass_label = tk.Label(curr_user, background=self.this_color, font=("Calibre", 14, 'bold'), width='12')
		pass_entry = tk.Entry(curr_user, textvariable=self.passvar, show="*", font=("Calibre", 12, 'bold'), width='10')
		self.error = tk.Label(curr_user, text="Invalid", background=self.this_color, font=("Calibre", 14, 'bold'), width='10')
		user_label.pack(side=tk.LEFT)
		user_entry.pack(side=tk.LEFT)
		pass_label.pack(side=tk.LEFT)
		pass_entry.pack(side=tk.LEFT)
		confirm_button = tk.Button(curr_user, text="confirm", font=("Calibre", 12, 'bold'))
		confirm_button.pack(side=tk.LEFT, padx=3)
		delete_button = tk.Button(self.edit_menu, text="Delete User", command=lambda: self._show_entry_bar(curr_user, "delete", user_label, pass_label, confirm_button, emp), font=("Calibre", 18, 'bold'), width='18')
		delete_button.pack(side=tk.TOP)
		status_button = tk.Button(self.edit_menu, text="Change Password", command=lambda: self._show_entry_bar(curr_user, "password", user_label, pass_label, confirm_button, emp), font=("Calibre", 18, 'bold'), width='18')
		status_button.pack(side=tk.TOP)
		pass_button = tk.Button(self.edit_menu, text=f"{'Demote to Employee' if self.employees[emp].is_admin() else 'Promote to Admin'}", command=lambda: self._show_entry_bar(curr_user, "role", user_label, pass_label, confirm_button, emp), font=("Calibre", 18, 'bold'), width='18')
		pass_button.pack(side=tk.TOP)
		ok = tk.Button(self.edit_menu, command=lambda: self._close_menu(self.edit_menu), text="OK", font=("Calibre", 20, 'bold'))
		ok.pack(side=tk.BOTTOM)

	def _show_entry_bar(self, frame, type, label1, label2, confirm, emp):
		self.uservar.set("")
		self.passvar.set("")
		self.error['text'] = ""
		if type == "password":
			label1['text'] = "New Pin"
			label2['text'] = "Old Pin"
			confirm['command'] = lambda: self.change_password(emp, self.uservar.get(), self.passvar.get(), frame)
		elif type == "delete":
			label1['text'] = f'Admin for confirmation:'
			label2['text'] = "Admin Pin"
			confirm['command'] = lambda: self.delete_user(emp, self.uservar.get(), self.passvar.get(), frame)
		elif type == "role":
			label1['text'] = f'Confirm with Admin:'
			label2['text'] = "Admin Pin"
			confirm['command'] = lambda: self.promote_demote(emp, self.uservar.get(), self.passvar.get(), frame)
		frame.pack(side=tk.TOP, pady=5)

	def change_password(self, emp, new_pass, old_pass, frame):
		if stf.change_password(emp, old_pass, new_pass) == 29:
			self.title['text'] = f"Successfully Changed {emp}'s Password"
			frame.grid_forget()
			self.show_edit_menu(emp)
		else:
			self.error['text'] = "Invalid"
			self.error.pack(side=tk.BOTTOM)

	def promote_demote(self, emp, admin, admin_password, frame):
		if self.employees[emp].is_admin():
			if stf.demote_from_admin(emp, admin, admin_password) == 22:
				self.title['text'] = f"{emp} Is Now an Employee"
				frame.grid_forget()
				self.show_edit_menu(emp)
			else:
				self.error['text'] = "Invalid"
				self.error.pack(side=tk.BOTTOM)
		else:
			if stf.promote_to_admin(emp, admin, admin_password) == 18:
				self.title['text'] = f"{emp} Is Now an Administrator"
				frame.grid_forget()
				self.show_edit_menu(emp)
			else:
				self.error['text'] = "Invalid"
				self.error.pack(side=tk.BOTTOM)

	def delete_user(self, user, curr, pin, frame):
		if stf.remove_employee(user, curr, pin) == 11:
			self.employees = stf.get_emp_list()
			self.title['text'] = f"Successfully Removed {user}"
			frame.grid_forget()
			self._close_menu(frame)
		else:
			self.error['text'] = "Invalid"
			self.error.pack(side=tk.BOTTOM)

	def _close_menu(self, menu_frame):
		menu_frame.destroy()
		self.show_employees()

	def show_time_options(self):
		date = tk.Label(self.master, text='Date Range:', background=BG_COLOR, font=("Calibre", 16, 'bold'), width='15',
						height='5')
		date.grid(row=2, column=2)

		to = tk.Label(self.master, text='To:', background=BG_COLOR, font=("Calibre", 16, 'bold'), width='10',
					  height='5')
		to.grid(row=2, column=4)

		from_frame = tk.Frame(self.master)
		from_frame.grid(row=2, column=3)

		to_frame = tk.Frame(self.master)
		to_frame.grid(row=2, column=5)

		style = ttk.Style()
		style.configure("bg.TCombobox", forground=BG_COLOR, background=BG_COLOR)

		date_today = dt.date.today()
		year_today = date_today.year
		month_today = date_today.month
		day_today = date_today.day

		month = ttk.Combobox(from_frame, state="readonly", style="bg.TCombobox", textvariable=self.monthvar,
							 font=("Calibre", 16, 'bold'), width='10', height='5')
		month['values'] = (
			'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
			'November',
			'December')
		month.pack(side=tk.LEFT)
		month.current(int(month_today) - 1)

		day = ttk.Combobox(from_frame, state="readonly", style="bg.TCombobox", textvariable=self.dayvar,
						   font=("Calibre", 16, 'bold'), width='5', height='5')
		day['values'] = [x for x in range(1, 32)]
		day.pack(side=tk.LEFT)
		day.current(int(day_today) - 1)

		year = ttk.Combobox(from_frame, state="readonly", style="bg.TCombobox", textvariable=self.yearvar,
							font=("Calibre", 16, 'bold'), width='5', height='5')
		year['values'] = (2021)
		year.pack(side=tk.LEFT)
		self.yearvar.set(int(year_today))

		tomonth = ttk.Combobox(to_frame, state="readonly", style="bg.TCombobox", textvariable=self.tomonthvar,
							   font=("Calibre", 16, 'bold'), width='10', height='5')
		tomonth['values'] = (
			'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
			'November',
			'December')
		tomonth.pack(side=tk.LEFT)
		tomonth.current(int(month_today) - 1)

		today = ttk.Combobox(to_frame, state="readonly", style="bg.TCombobox", textvariable=self.todayvar,
							 font=("Calibre", 16, 'bold'), width='5', height='5')
		today['values'] = [x for x in range(1, 32)]
		today.pack(side=tk.LEFT)
		today.current(int(day_today) - 1)

		toyear = ttk.Combobox(to_frame, state="readonly", style="bg.TCombobox", textvariable=self.toyearvar,
							  font=("Calibre", 16, 'bold'), width='5', height='5')
		toyear['values'] = (2021)
		toyear.pack(side=tk.LEFT)
		self.toyearvar.set(int(year_today))

"""
	*   Class: ShowSaleData
	*   Description: Class contains functions Sale data
	*
	*   Date: 10 Mar 2021
	*   Created by: Alex Villa
	*   Edit History: 10 Mar 2021 - Alex Villa
	*					v1.0 - Created
"""
class ShowSaleData(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
					   'September': 9, 'October': 10, 'November': 11, 'December': 12}
		self.ticket = tk.Text(self.master, font=("Calibre", 18, 'bold'))
		ys = tk.Scrollbar(self.master, orient='vertical', command=self.ticket.yview)
		self.ticket['yscrollcommand'] = ys.set
		self.ticket.grid(column=1, row=4, columnspan=6, rowspan=3)
		self.ticket['state'] = 'disabled'
		self.empty = True
		self.title = title = tk.Label(self.master, text='Select a Date Range', background=BG_COLOR, font=("Calibre", 20, 'bold'))
		title.grid(row=3, column=1, columnspan=6)

	def _calcTotalPeriod(self, day_totals: list):
		total_sales = 0
		total_rev = 0
		print(day_totals)
		for i in day_totals:
			total_sales += i[1]
			total_rev += i[0]
		return total_rev, total_sales

	def _calcTotalDay(self, receipts: dict):
		total = 0
		for item in receipts:
			for entry in receipts[item]:
				total += entry[0] * entry[2] * entry[3]
		return total

	def _calcTotal(self, collection: list):
		''' list[ ( amount, name, price, discount ), ... ] '''
		total = 0
		for item in collection:
			total += item[0] * item[2] * item [3]
		return total

	def findBySale(self, startdate: tuple, enddate: tuple):
		self.ticket['state'] = 'normal'
		self.ticket.delete('1.0', tk.END)
		start = dt.date(startdate[0], self.months[startdate[1]], startdate[2])
		end = dt.date(enddate[0], self.months[enddate[1]], enddate[2])
		sales = rep.get_sale_list(start, end)
		total_sales = rep.total_sale_by_date(start, end)
		period_totals = []
		for entry in sales:
			if sales[entry]:
				self.empty = False
				receipt_collection = {}
				receipt_info = {}
				for item in sales[entry]:
					receipt_num = f"{item[1].year}{item[1].month}{item[1].day}{item[0]}"
					if receipt_num in receipt_collection:
						receipt_collection[receipt_num].append(
							(item[6], item[4], item[7], item[5]))  # amount, item name, price, discount
					else:
						receipt_collection[receipt_num] = []
						receipt_collection[receipt_num].append((item[6], item[4], item[7], item[5]))
						hr = item[2].strftime("%H")
						if int(hr) > 12:
							ampm = "PM"
						else:
							ampm = "AM"
						time = item[2].strftime("%I:%M:%S") + f" {ampm}"
						receipt_info[receipt_num] = (item[3], item[1], time)  # Customer Name, Date, Time
				day_sales = total_sales[entry]
				day_total = self._calcTotalDay(receipt_collection)
				period_totals.append((day_total, day_sales))
				self.ticket.insert(tk.END, f"-Showing All Sales On {entry} \t\t Day Total: ${day_total} From {day_sales} Sales- \n\n")
				for item in receipt_collection:
					self.ticket.insert(tk.END, f"\t\tReceipt#: {item} \t Customer: {receipt_info[item][0]}\n")
					self.ticket.insert(tk.END, f"\t\tDate: {receipt_info[item][1]} \t Time: {receipt_info[item][2]}\n ")
					self.ticket.insert(tk.END, "\t\t________________________________________\n")
					for food in receipt_collection[item]:  # order of food: amount, item name, price, discount
						self.ticket.insert(tk.END, f"\t\t{food[0]} \t {food[1]} \t\t ${food[0] * food[2] * food[3]:.2f}\n")
						if int(food[3]) != 1:
							self.ticket.insert(tk.END, f"\t\t\t    Price Adjust by %{food[3]:.2f}\n")
					self.ticket.insert(tk.END, "\t\t\t_______________________________\n")
					self.ticket.insert(tk.END, f"\t\t\t Total: \t\t ${self._calcTotal(receipt_collection[item]):.2f}\n")
					self.ticket.insert(tk.END, "\n\n")
		if self.empty:
			self.title['text'] = "No Orders To Show In Date Range"
			self.empty = True
		else:
			all_totals = self._calcTotalPeriod(period_totals)
			self.title[
				'text'] = f"Showing Sales From {start} to {end} \t Period Total: ${all_totals[0]:.2f} from {all_totals[1]} Sales"
		self.ticket['state'] = 'disabled'

	def findByCategory(self, startdate: tuple, enddate: tuple):
		self.ticket['state'] = 'normal'
		self.ticket.delete('1.0', tk.END)
		start = dt.date(startdate[0], self.months[startdate[1]], startdate[2])
		end = dt.date(enddate[0], self.months[enddate[1]], enddate[2])
		dates = rep.report_by_category(start, end)
		for date in dates:
			if dates[date]:
				self.empty = False
				self.ticket.insert(tk.END, f"Showing Category Sales On {date} \n")
				self.ticket.insert(tk.END, "________________________________________\n\n")
				for cat in dates[date]:
					self.ticket.insert(tk.END, f"\t{dates[date][cat]} \t {cat}\n")
				self.ticket.insert(tk.END, "\n\n")
		if self.empty:
			self.title['text'] = "No Sales To Show In Date Range"
			self.empty = True
		else:
			self.title['text'] = f"Showing Category Sales From {start} to {end}"
		self.ticket['state'] = 'disabled'

	def findByItem(self, startdate: tuple, enddate: tuple):
		self.ticket['state'] = 'normal'
		self.ticket.delete('1.0', tk.END)
		start = dt.date(startdate[0], self.months[startdate[1]], startdate[2])
		end = dt.date(enddate[0], self.months[enddate[1]], enddate[2])
		dates = rep.report_by_item(start, end)
		for date in dates:
			if dates[date]:
				self.empty = False
				self.ticket.insert(tk.END, f"Showing Item Sales On {date} \n")
				self.ticket.insert(tk.END, "________________________________________\n\n")
				for cat in dates[date]:
					self.ticket.insert(tk.END, f"\t{dates[date][cat]} \t {cat}\n")
				self.ticket.insert(tk.END, "\n\n")
		if self.empty:
			self.title['text'] = "No Sales To Show In Date Range"
			self.empty = True
		else:
			self.title['text'] = f"Showing Item Sales From {start} to {end}"
		self.ticket['state'] = 'disabled'

"""
	*   Class: UpdatingCategories
	*   Description: Class contains functions for updating categories
	*
	*   Date: 10 Mar 2021
	*   Created by: Alex Villa
	*   Edit History: 10 Mar 2021 - Alex Villa
	*					v1.0 - Created
"""

class UpdatingCategories(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.indiv_frames = {}
		self.buttons_dict = {}
		self.c = 2

	def insert_item(self, name: str, category: str, price: float, name_entry: tk.Entry, price_entry: tk.Entry):
		if cus.add_item(name, category, price):
			name_entry.delete(0, 'end')
			price_entry.delete(0, 'end')
			self.show_cat_list()

	def show_cat_list(self):
		for child in self.master.grid_slaves():
			child.destroy()
		currents_header = tk.Label(self.master, text="Current Menu", font=("Calibre", 18, 'bold'), background=BG_COLOR)
		currents_header.grid(column=1, row=1, padx=50)
		self.c = 2
		for i in cus.query_items():
			self.create_category(i)

	def create_category(self, i):
		div = tk.Frame(self.master)  # Frame that holds the category button label and the individual item frame
		indiv_frame = tk.Frame(div)  # individual items frame
		div.grid(column=1, row=self.c)

		self.indiv_frames[i] = indiv_frame
		self.c += 1
		cat_label = tk.Button(div, bg='gray',
							  command=lambda i=i: self.toggle_items(self.buttons_dict[i], self.indiv_frames[i]),
							  text=f'{i}',
							  font=("Calibre", 18, 'bold'), width="50")
		self.buttons_dict[i] = cat_label
		cat_label.pack(side=tk.TOP)

		count = 2
		for j in cus.query_items()[i]:
			edit_frame = self.indiv_frames[i]
			self.create_item(j, edit_frame, count, i)
			count += 1

	def create_item(self, j: tuple, indiv_frame, count: int, frame_num: int):
		name_label = tk.Label(indiv_frame, text=f'{j[0]}', font=("Calibre", 18, 'bold'), width="30")
		price_label = tk.Label(indiv_frame, text=f'$ {j[1]:.2f}', font=("Calibre", 18, 'bold'), width="10")
		delete_button = tk.Button(indiv_frame, bg='gray',text="X",font=("Calibre", 14, 'bold'), width="3")
		delete_button['command'] = lambda j=j: self.delete_item(j)
		delete_button.grid(column=1, row=count)
		name_label.grid(column=2, row=count)
		price_label.grid(column=3, row=count)

	def delete_item(self, name):
		if cus.delete_menu(name[0]):
			self.show_cat_list()

	def toggle_items(self, btn: tk.Button, frm: tk.Frame):
		if btn['bg'] == 'gray':
			frm.pack(side=tk.BOTTOM)
			btn['bg'] = 'white'
		else:
			frm.pack_forget()
			btn['bg'] = 'gray'

"""
	*   Class: DynamicMenu
	*   Description: Class contains functions for handling items, orders(create, insert, delete)
	*
	*   Date: 10 Mar 2021
	*   Created by: Alex Villa
	*   Edit History: 10 Mar 2021 - Alex Villa
	*					v1.0 - Created
"""
class DynamicMenu(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.active = None
		self.buttons_dict = {}
		self.items = {}
		self.line = 1

		ticket_frame = tk.Frame(self.master)
		ticket_frame.grid(row=1, column=1)
		self.order_grid = tk.Frame(ticket_frame, width="50", height="200")
		self.order_grid.pack()
		self.total = tk.Label(ticket_frame, text="Total: No Items Selected", font=("Calibre", 18, 'bold'))
		self.total.pack(side=tk.TOP)
		name_bar = tk.Frame(ticket_frame)
		name_bar.pack(side=tk.TOP)
		name_label = tk.Label(name_bar, text="Customer Name: ", font=("Calibre", 18, 'bold'))
		name_label.pack(side=tk.LEFT)
		self.name_var = tk.StringVar()
		name_entry = tk.Entry(name_bar, textvariable=self.name_var, font=("Calibre", 16))
		name_entry.pack(side=tk.RIGHT)
		self.send_button = tk.Button(ticket_frame, width="30", height="5", text="Pay Order",
									 font=("Calibre", 20, 'bold'))

	def get_send_button(self):
		return self.send_button

	def show_cat_list(self):
		order_frame = tk.Frame(self.master)
		order_frame.grid(row=1, column=2)

		cat_frame = tk.Frame(order_frame)
		cat_frame.pack(side=tk.LEFT)
		c = 1
		for i in cus.query_items():
			cat_label = tk.Button(cat_frame, bg='gray', width="15", height="5",
								  command=lambda i=i: self.create_items(i, order_frame), text=f'{i}',
								  font=("Calibre", 18, 'bold'))
			self.buttons_dict[i] = cat_label
			cat_label.grid(column=1, row=c)
			c += 1


	def create_items(self, i: str, order_frame: tk.Frame):
		col = True
		if self.active:
			self.active.pack_forget()
		selections = tk.Frame(order_frame)
		selections.pack(side=tk.RIGHT)

		self.active = selections
		count = 1
		for j in cus.query_items()[i]:
			name_label = tk.Button(selections, command=lambda j=j: self.insert_item(j), width="15", height="5",
								   text=f'{j[0]}', font=("Calibre", 18, 'bold'))
			if col:
				val = 1
			else:
				val = 2
			name_label.grid(column=val, row=count)
			if val == 2:
				count += 1
			col = not col

	def insert_item(self, j: tuple):
		cus.add_order(j[0], 1)
		items = cus.show_order()

		self._delete_order_grid()
		self.items = {}
		i = 0;
		for order in reversed(list(items.keys())):
			order_button = tk.Button(self.order_grid, command=lambda i=i: self.delete_item(i), font=("Calibre", 18, 'bold'), width="40", justify="left", anchor="w")
			amount = int(items[order].get_amount())
			name = items[order].get_item().get_name()
			price = items[order].get_item().get_price()
			order_button['text'] = f' {amount}  {name:50} \n\t\t\t\t {price:10.2f}\n'
			order_button.pack(side=tk.TOP)
			self.items[i] = (order_button, name)
			i += 1;
		self.order_grid.pack(side=tk.TOP)
		self.total['text'] = f'Total: ${cus.get_total():.2f}'
		self.send_button.pack(side=tk.BOTTOM)

	def delete_item(self, i):
		cus.delete_order(self.items[i][1])
		self.items[i][0].destroy()
		del self.items[i]
		self.total['text'] = f'Total: ${round(cus.get_total(), 2)}'
		if not self.items:
			self.total['text'] = "Total: No Items Selected"


	def _delete_order_grid(self):
		"""Reset the list of participants"""
		for child in self.order_grid.winfo_children():
			child.destroy()

	def delete_whole_order(self, app):
		items = cp.deepcopy(cus.show_order())
		if items:
			for order in items:
				cus.delete_order(order)
		app.main_login_screen()

	def send_order(self, app):
		if not self.name_var.get():
			now = dt.datetime.now().strftime('%H%M%S')
			self.name_var.set(f"{now}")
		if cus.pay_order(self.name_var.get()):
			app.main_login_screen()


def main():
	root = tk.Tk(className="Welcome to ManEz")
	root.geometry("1200x2000")
	manez = App(root)
	stf.read_emp_db()
	if stf.is_emp_db_empty():
		manez.init_screen()
	else:
		manez.main_login_screen()
	manez.mainloop()


if __name__ == '__main__':
	main()
