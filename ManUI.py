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

	def _init_submit_button(self, name_var, pin_var):
		name = name_var.get()
		pin = pin_var.get()

		# insert name/pin in database
		print(name)
		print(pin)

		name_var.set("")
		pin_var.set("")

	def init_screen(self):

		#Choose Background Color
		bg_color = 'gray'
		self.master.configure(background=bg_color)

		#Create Labels
		greeting = tk.Label(background=bg_color, text="Welcome to ManEz", font=("Arial", 25))
		greeting.grid(row=0, column=3, pady=20)
		create_profile = tk.Label(background=bg_color, text="Create Administrator Profile", font=("Arial", 25))
		create_profile.grid(row=2, column=3)

		name_var = tk.StringVar()
		pin_var = tk.StringVar()

		name_label = tk.Label(self.master, text="Name", font=("Calibre", 20, 'bold'))
		name_entry = tk.Entry(self.master, textvariable=name_var, font=("Calibre", 20))

		pin_label = tk.Label(self.master, text="Pin", font=("Calibre", 20, 'bold'))
		pin_entry = tk.Entry(self.master, textvariable=pin_var, font=("Calibre", 20))

		name_label.grid(row=5, column=5)
		name_entry.grid(row=5, column=6)

		pin_label.grid(row=6, column=5)
		pin_entry.grid(row=6, column=6)

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
