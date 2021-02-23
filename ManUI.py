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
		self.pack()
		self.load_test_screen

	def load_test_screen(self):
		self.make_menu = tk.Button(self)
		self.make_menu["text"] = "Create New Menu"
		self.make_menu["command"] = self.make_menu_screen()
		self.make_menu.pack(side="top")
		self.quit = tk.Button(self, text="QUIT", fg="red",
							  command=self.master.destroy)
		self.quit.pack(side="bottom")

	def make_menu_screen(self):
		pass

def main():
	manez = App()
	manez.mainloop()

if __name__ == '__main__':
	main()
