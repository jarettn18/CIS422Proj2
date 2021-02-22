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

class App (tk.frame):
	
	def __init__(self, master):
		super().__init__(master)
		self.pack()

def main():
	manez = App()
	myapp.mainloop()

if __name__ == '__main__':
	main()
