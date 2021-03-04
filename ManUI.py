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
		#Choose Background Color
		BG_COLOR = 'gray'
		self.master.configure(background=BG_COLOR)

		#Create Labels
		greeting = tk.Label(background=BG_COLOR, text="Welcome to ManEz", font=("Arial", 30, 'bold'))
		greeting.grid(row=0, column=2, columnspan=2)
		create_profile = tk.Label(background=BG_COLOR, text="Create Administrator Profile", font=("Arial", 25))
		create_profile.grid(row=1, column=2, columnspan=2)

		name_var = tk.StringVar()
		pin_var = tk.StringVar()

		name_label = tk.Label(self.master,background=BG_COLOR, text="Name", font=("Calibre", 20, 'bold'))
		name_entry = tk.Entry(self.master, textvariable=name_var, font=("Calibre", 20))

		pin_label = tk.Label(self.master,background=BG_COLOR, text="Pin", font=("Calibre", 20, 'bold'))
		pin_entry = tk.Entry(self.master, textvariable=pin_var, font=("Calibre", 20))

		name_label.grid(row=2, column=2)
		name_entry.grid(row=2, column=3)

		pin_label.grid(row=3, column=2)
		pin_entry.grid(row=3, column=3)

		submit = tk.Button(self.master, text="Submit", command=_init_submit_button, font=("Calibre", 20, 'bold'))
		submit.grid(row=4, column=2)

	def main_login_screen(self):
		for i in range(6):
			tk.Grid.rowconfigure(self.master, i, weight=1)
			tk.Grid.columnconfigure(self.master, i, weight=1)

		# Choose Background Color
		self.master.configure(background=BG_COLOR)

		greeting = tk.Label(background=BG_COLOR, text="Test Text", font=("Arial", 30, 'bold'))
		greeting.grid(row=0, column=2, columnspan=2)

		for r in range(6):
			for c in range(6):
				tk.Label(self.master, text='R%s/C%s' % (r, c),
						 borderwidth=1).grid(row=r, column=c)
		#TODO
		#Add New Order Button
		#Add Order History Button
		#Add Settings Button
		#Add Clock In Button

	def settings_menu(self, prev: tk.Frame):
		prev.pack_forget()
		settings_frame = tk.Frame(self.master)
		settings_frame.pack()

		title = tk.Label(settings_frame, text='ManEz Settings', font=("Calibre", 20, 'bold'), width='15', height='5')
		title.grid(row=1, column=2)

		new_account = tk.Button(settings_frame, cursor='circle', command=lambda: self.new_account(settings_frame), text='Create New Account', width='25', height='10',font=("Calibre", 20, 'bold'))
		new_account.grid(row=2, column=1)

		sales = tk.Button(settings_frame, cursor='circle', text='Sales Analytics', width='25', height='10', font=("Calibre", 20, 'bold'))
		sales.grid(row=2, column=3)

		edit = tk.Button(settings_frame, cursor='circle', text='Edit Menu', width='25', height='10',font=("Calibre", 20, 'bold'))
		edit.grid(row=3, column=3)

		employee = tk.Button(settings_frame, cursor='circle', text='Employee Analytics', width='25', height='10', font=("Calibre", 20, 'bold'))
		employee.grid(row=3, column=1)

	def new_account(self, prev: tk.Frame):
		prev.pack_forget()
		account_frame = tk.Frame(self.master)
		account_frame.pack()

		title = tk.Label(account_frame, text='Create New Account', font=("Calibre", 20, 'bold'), width='15', height='5')
		title.grid(row=1, column=2)

		type_var = tk.StringVar()
		name_var = tk.StringVar()
		pin_var = tk.StringVar()

		radio_label = tk.Label(account_frame, text='Select Account Type:', font=("Calibre", 18, 'bold'))
		admin = tk.Radiobutton(account_frame, text="Administrator", variable=type_var, value='admin')
		emplo = tk.Radiobutton(account_frame, text='Employee', variable=type_var, value='emp')

		name_label = tk.Label(account_frame, text="Name", font=("Calibre", 18, 'bold'))
		name_entry = tk.Entry(account_frame, textvariable=name_var, font=("Calibre", 16))

		pin_label = tk.Label(account_frame, text="Pin", font=("Calibre", 18, 'bold'))
		pin_entry = tk.Entry(account_frame, textvariable=pin_var, font=("Calibre", 16))

		submit = tk.Button(account_frame, text="Create", command=lambda: self.create_account(account_frame, name_var.get(), pin_var.get(), type_var.get()), font=("Calibre", 20, 'bold'))

		radio_label.grid(row=2, column=1)
		admin.grid(row=2, column=2)
		emplo.grid(row=2, column=3)

		name_label.grid(row=3, column=1, pady=20)
		name_entry.grid(row=3, column=2, columnspan=2, pady=20)

		pin_label.grid(row=4, column=1, pady=20)
		pin_entry.grid(row=4, column=2, columnspan=2, pady=20)

		submit.grid(row=5, column=2)

	def create_account(self, prev: tk.Frame, name, pin, permission):
		stf.add_employee(name, pin, permission)
		self.settings_menu(prev)


def main():
	root = tk.Tk(className="Welcome to ManEz")
	root.geometry("1024x768")
	manez = App(root)

	test = tk.Frame()
	test.pack()
	manez.init_screen()

	'''
	if stf.is_emp_db_empty():
		#manez.init_screen()
		pass
	else:
		#manez.main_login_screen()
		pass
	'''
	manez.settings_menu(test)
	manez.mainloop()

if __name__ == '__main__':
	main()
