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

class App (tk.Frame):
	
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
		bg_color = 'gray'
		self.master.configure(background=bg_color)

		#Create Labels
		greeting = tk.Label(background=bg_color, text="Welcome to ManEz", font=("Arial", 30, 'bold'))
		greeting.grid(row=0, column=2, columnspan=2)
		create_profile = tk.Label(background=bg_color, text="Create Administrator Profile", font=("Arial", 25))
		create_profile.grid(row=1, column=2, columnspan=2)

		name_var = tk.StringVar()
		pin_var = tk.StringVar()

		name_label = tk.Label(self.master,background=bg_color, text="Name", font=("Calibre", 20, 'bold'))
		name_entry = tk.Entry(self.master, textvariable=name_var, font=("Calibre", 20))

		pin_label = tk.Label(self.master,background=bg_color, text="Pin", font=("Calibre", 20, 'bold'))
		pin_entry = tk.Entry(self.master, textvariable=pin_var, font=("Calibre", 20))

		name_label.grid(row=2, column=2)
		name_entry.grid(row=2, column=3)

		pin_label.grid(row=3, column=2)
		pin_entry.grid(row=3, column=3)

		submit = tk.Button(self.master, text="Submit", command=_init_submit_button, font=("Calibre", 20, 'bold'))
		submit.grid(row=4, column=2)

	def make_menu_screen(self):
		pass

def main():
	root = tk.Tk(className="Welcome to ManEz")
	root.geometry("1024x768")
	manez = App(root)
	manez.init_screen()
	manez.mainloop()

if __name__ == '__main__':
	main()
