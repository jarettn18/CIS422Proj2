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
import ManCus as cus
import ManStaff as stf

BG_COLOR = 'gray'


class App(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master

	def init_screen(self):

		def _init_submit_button():
			name = name_var.get()
			pin = pin_var.get()

			# insert name/pin in database
			print(name)
			print(pin)

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

		name_label = tk.Label(self.master, background=BG_COLOR, text="Name", font=("Calibre", 20, 'bold'))
		name_entry = tk.Entry(self.master, textvariable=name_var, font=("Calibre", 20))

		pin_label = tk.Label(self.master, background=BG_COLOR, text="Pin", font=("Calibre", 20, 'bold'))
		pin_entry = tk.Entry(self.master, textvariable=pin_var, font=("Calibre", 20))

		name_label.grid(row=2, column=2)
		name_entry.grid(row=2, column=3)

		pin_label.grid(row=3, column=2)
		pin_entry.grid(row=3, column=3)

		submit = tk.Button(self.master, text="Submit", command=_init_submit_button, font=("Calibre", 20, 'bold'))
		submit.grid(row=4, column=2)

	def main_login_screen(self):

		def _new_order():
			print("New Order")

		def _order_history():
			print("Order History")

		def _settings():
			print("Settings")

		def _clock_in():
			print("Clock in")

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
		new_order = tk.Button(self.master, text="New Order", command=_new_order, font=("Calibre", 50, 'bold'))
		new_order.grid(row=1 ,column=1)

		order_hist = tk.Button(self.master, text="Order History", command=_order_history, font=("Calibre", 50, 'bold'))
		order_hist.grid(row=1, column=4)

		settings = tk.Button(self.master, text="Settings", command=_settings, font=("Calibre", 30, 'bold'))
		settings.grid(row=4, column=1)

		clock_in = tk.Button(self.master, text="Clock In", command=_clock_in, font=("Calibre", 30, 'bold'))
		clock_in.grid(row=4, column=4)

		name_label = tk.Label(self.master, background=BG_COLOR, text="Administrator Use Only", font=("Calibre", 20, 'bold'))
		name_label.grid(row=3, column=1, pady=20)

	def pin_screen(self):

		for i in range(7):
			tk.Grid.rowconfigure(self.master, i, weight=1)
			tk.Grid.columnconfigure(self.master, i, weight=1)
		# Choose Background Color
		self.master.configure(background=BG_COLOR)

		greeting = tk.Label(background=BG_COLOR, text="ManEz", font=("Arial", 25, 'bold'))
		greeting.grid(row=0, column=2, columnspan=2)

		for r in range(7):
			for c in range(7):
				tk.Label(self.master, text='R%s/C%s' % (r, c),
						 borderwidth=1).grid(row=r, column=c)

	# TODO
	# Add New Order Button
	# Add Order History Button
	# Add Settings Button
	# Add Clock In Button

	def settings_menu(self, prev: tk.Frame):
		prev.pack_forget()
		settings_frame = tk.Frame(self.master)
		settings_frame.pack()

		title = tk.Label(settings_frame, text='ManEz Settings', font=("Calibre", 20, 'bold'), width='15', height='5')
		title.grid(row=1, column=2)

		back = tk.Button(settings_frame, text="Back", command=None, font=("Calibre", 20, 'bold'))
		back.grid(row=1, column=1)

		new_account = tk.Button(settings_frame, cursor='circle', command=lambda: self.new_account(settings_frame),
								text='Create New Account', width='25', height='10', font=("Calibre", 20, 'bold'))
		new_account.grid(row=2, column=1)

		sales = tk.Button(settings_frame, cursor='circle', text='Sales Analytics', width='25', height='10',
						  font=("Calibre", 20, 'bold'))
		sales.grid(row=2, column=3)

		edit = tk.Button(settings_frame, cursor='circle', text='Menu Settings',
						 command=lambda: self.menu_settings(settings_frame), width='25', height='10',
						 font=("Calibre", 20, 'bold'))
		edit.grid(row=3, column=3)

		employee = tk.Button(settings_frame, cursor='circle', text='Employee Analytics', width='25', height='10',
							 font=("Calibre", 20, 'bold'))
		employee.grid(row=3, column=1)

	def new_account(self, prev: tk.Frame):
		prev.pack_forget()
		account_frame = tk.Frame(self.master)
		account_frame.pack()

		title = tk.Label(account_frame, text='Create New Account', font=("Calibre", 20, 'bold'), width='15', height='5')
		title.grid(row=1, column=2)

		back = tk.Button(account_frame, text="Back", command=lambda: self.settings_menu(account_frame),
						 font=("Calibre", 20, 'bold'))
		back.grid(row=1, column=1)

		type_var = tk.IntVar()
		name_var = tk.StringVar()
		pin_var = tk.StringVar()

		radio_label = tk.Label(account_frame, text='Select Account Type:', font=("Calibre", 18, 'bold'))
		admin = tk.Radiobutton(account_frame, text="Administrator", variable=type_var, value=1)
		emplo = tk.Radiobutton(account_frame, text='Employee', variable=type_var, value=2)

		name_label = tk.Label(account_frame, text="Name", font=("Calibre", 18, 'bold'))
		name_entry = tk.Entry(account_frame, textvariable=name_var, font=("Calibre", 16))

		pin_label = tk.Label(account_frame, text="Pin", font=("Calibre", 18, 'bold'))
		pin_entry = tk.Entry(account_frame, textvariable=pin_var, font=("Calibre", 16))

		submit = tk.Button(account_frame, text="Create",
						   command=lambda: self.create_account(account_frame, name_var.get(), pin_var.get(),
															   type_var.get()), font=("Calibre", 20, 'bold'))

		radio_label.grid(row=2, column=1)
		admin.grid(row=2, column=2)
		emplo.grid(row=2, column=3)

		name_label.grid(row=3, column=1, pady=20)
		name_entry.grid(row=3, column=2, columnspan=2, pady=20)

		pin_label.grid(row=4, column=1, pady=20)
		pin_entry.grid(row=4, column=2, columnspan=2, pady=20)

		submit.grid(row=5, column=2)

	def create_account(self, prev: tk.Frame, name: str, pin: str, permission: int):
		if permission == 1:
			perm_type = 'admin'
		else:
			perm_type = 'emp'
		stf.add_employee(name=name, current_user=None, password=pin, permission=perm_type)
		self.settings_menu(prev)

	def menu_settings(self, prev):
		prev.pack_forget()

		men_sett_frame = tk.Frame(self.master)
		men_sett_frame.pack()

		title = tk.Label(men_sett_frame, text='Menu Settings', font=("Calibre", 20, 'bold'), width='15', height='5')
		title.grid(row=1, column=2)

		back = tk.Button(men_sett_frame, text="Back", command=lambda: self.settings_menu(men_sett_frame),
						 font=("Calibre", 20, 'bold'))
		back.grid(row=1, column=1)

		add_menu = tk.Button(men_sett_frame, cursor='circle', command=lambda: self.add_menu(men_sett_frame),
							 text='Add New Menu', width='25', height='10', font=("Calibre", 20, 'bold'))
		add_menu.grid(row=2, column=2)

	def add_menu(self, prev):
		prev.pack_forget()

		men_main_frame = tk.Frame(self.master)
		men_main_frame.pack()

		add_men_frame = tk.Frame(men_main_frame)
		add_men_frame.pack(side=tk.LEFT)

		curr_men_frame = tk.Frame(men_main_frame)
		curr_men_frame.pack(side=tk.RIGHT)

		currents_header = tk.Label(curr_men_frame, text="Current Menu", font=("Calibre", 18, 'bold'))
		currents_header.grid(column=1, row=1, padx=50)

		item_frames = UpdatingCategories(curr_men_frame)
		item_frames.show_cat_list()

		title = tk.Label(add_men_frame, text='Add New Menu', font=("Calibre", 20, 'bold'), width='15', height='5')
		title.grid(row=1, column=2)

		back = tk.Button(add_men_frame, text="Back", command=lambda: self.menu_settings(men_main_frame),
						 font=("Calibre", 20, 'bold'))
		back.grid(row=1, column=1)

		name_var = tk.StringVar()
		price_var = tk.DoubleVar()
		cat_var = tk.StringVar()

		header = tk.Label(add_men_frame, text="New Item", font=("Calibre", 18, 'bold'))
		item_name = tk.Label(add_men_frame, text="Name", font=("Calibre", 16, 'bold'))
		name_entry = tk.Entry(add_men_frame, textvariable=name_var, font=("Calibre", 16))

		item_price = tk.Label(add_men_frame, text="Price", font=("Calibre", 16, 'bold'))
		price_entry = tk.Entry(add_men_frame, textvariable=price_var, font=("Calibre", 16))

		item_category = tk.Label(add_men_frame, text="Category", font=("Calibre", 16, 'bold'))
		category_entry = tk.Entry(add_men_frame, textvariable=cat_var, font=("Calibre", 16))

		submit = tk.Button(add_men_frame, text="Add",
						   command=lambda: item_frames.insert_item(name_var.get(), cat_var.get(), price_var.get(),
																   name_entry,
																   price_entry),
						   font=("Calibre", 20, 'bold'))

		header.grid(column=2, row=2)

		item_name.grid(column=1, row=3)
		name_entry.grid(column=2, row=3)

		item_price.grid(column=1, row=4)
		price_entry.grid(column=2, row=4)

		item_category.grid(column=1, row=5)
		category_entry.grid(column=2, row=5)

		submit.grid(column=2, row=6, pady=20)

	def order_screen(self, prev: tk.Frame):
		prev.pack_forget()

		order_main_frame = tk.Frame(self.master)
		order_main_frame.pack()

		title_frame = tk.Frame(order_main_frame)
		title_frame.grid(row=1)

		title = tk.Label(title_frame, text='New Order', font=("Calibre", 20, 'bold'), width='15', height='5')
		title.grid(row=1, column=2)

		back = tk.Button(title_frame, text="Back", font=("Calibre", 20, 'bold'))
		back.grid(row=1, column=1)

		action_frame = tk.Frame(order_main_frame)
		action_frame.grid(row=2)

		category_buttons = DynamicMenu(action_frame)
		category_buttons.show_cat_list()

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
			self.update_cat_list()

	def update_cat_list(self):
		for i in cus.query_items():
			if i in self.indiv_frames:
				indiv_frame = self.indiv_frames[i]
				count = 2
				for j in cus.query_items()[i]:
					self.create_item(j, indiv_frame, count)
					count += 1
			else:
				self.create_category(i)

	def show_cat_list(self):
		for i in cus.query_items():
			self.create_category(i)

	def create_category(self, i):
		div = tk.Frame(self.master)  # Frame that holds the category button label and the individual item frame
		indiv_frame = tk.Frame(div)  # individual items frame
		div.grid(column=1, row=self.c)

		self.indiv_frames[i] = indiv_frame
		self.c += 1
		cat_label = tk.Button(div, bg='gray', command=lambda i=i: self.toggle_items(self.buttons_dict[i], self.indiv_frames[i]), text=f'{i}',
							  font=("Calibre", 18, 'bold'))
		self.buttons_dict[i] = cat_label
		cat_label.pack(side=tk.TOP)

		count = 2
		for j in cus.query_items()[i]:
			edit_frame = self.indiv_frames[i]
			self.create_item(j, edit_frame, count)
			count += 1

	def create_item(self, j: tuple, indiv_frame, count: int):
		name_label = tk.Label(indiv_frame, text=f'{j[0]}', font=("Calibre", 18, 'bold'))
		price_label = tk.Label(indiv_frame, text=f'$ {j[1]}', font=("Calibre", 18, 'bold'))
		name_label.grid(column=1, row=count)
		price_label.grid(column=2, row=count)

	def toggle_items(self, btn: tk.Button, frm: tk.Frame):
		if btn['bg'] == 'gray':
			frm.pack(side=tk.BOTTOM)
			btn['bg'] = 'white'
		else:
			frm.pack_forget()
			btn['bg'] = 'gray'

class DynamicMenu(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.active = None
		self.buttons_dict = {}
		self.line = 1
		ticket_frame = tk.Frame(self.master)
		ticket_frame.grid(row=1, column=1)
		self.ticket = tk.Text(ticket_frame, font=("Calibre", 18, 'bold'), width="30")
		ys = tk.Scrollbar(ticket_frame, orient='vertical', command=self.ticket.yview)
		self.ticket['yscrollcommand'] = ys.set
		self.ticket.pack()
		self.ticket['state'] = 'disabled'
		self.total = tk.Label(ticket_frame, text="No Items Selected", font=("Calibre", 18, 'bold'))
		self.total.pack(side=tk.BOTTOM)


	def show_cat_list(self):
		order_frame = tk.Frame(self.master)
		order_frame.grid(row=1, column=2)

		cat_frame = tk.Frame(order_frame)
		cat_frame.pack(side=tk.LEFT)
		c = 1
		for i in cus.query_items():
			cat_label = tk.Button(cat_frame, bg='gray', width="15", height="5", command=lambda i=i: self.create_items(i, order_frame), text=f'{i}',
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
			name_label = tk.Button(selections, command=lambda j=j: self.insert_item(j), width="15", height="5", text=f'{j[0]}', font=("Calibre", 18, 'bold'))
			if col:
				val = 1
			else:
				val = 2
			name_label.grid(column=val, row=count)
			if val == 2:
				count += 1
			col = not col

	def insert_item(self, j: tuple):
		self.ticket['state'] = 'normal'
		cus.add_order(j[0], 1)
		items = cus.show_order()
		self.ticket.delete(1.0, tk.END)
		line = 1
		for order in reversed(list(items.keys())):
			amount = int(items[order].get_amount())
			name = items[order].get_item().get_name()
			price = items[order].get_item().get_price()
			self.ticket.insert(f'{self.line}.0', f'{amount}  {name} \t \t {price}\n')
			line += 1
		self.ticket['state'] = 'disabled'
		self.total['text'] = f'Total: ${round(cus.get_total(), 2)}'

def main():
	root = tk.Tk(className="Welcome to ManEz")
	root.geometry("1024x768")
	manez = App(root)

	test = tk.Frame()
	test.pack()
	#manez.pin_screen()
	if not stf.is_emp_db_empty():
		#manez.init_screen()
		pass
	#manez.settings_menu(test)
	manez.order_screen(test)
	manez.mainloop()


if __name__ == '__main__':
	main()
