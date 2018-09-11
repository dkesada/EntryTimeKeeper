#! /usr/bin/python
# -*- coding: utf-8 -*-
#author: David Quesada López

"""
User interface, let's see how Tkinter goes.
"""

import Tkinter as ttk


class Gui:
	def __init__(self, back):
		self.backend = back
		self.home = ttk.Tk()
		
		self.home.geometry('400x200')
		self.home.resizable(width=False,height=False)
		self.home.configure(bg = 'beige')
		self.home.title('Home')
		self.canvas = ttk.Frame(self.home)
		self.inicio()
		
		self.home.mainloop()
	
	def inicio(self):
		#Frame que se irá destruyendo
		self.canvas.pack_forget()
		self.canvas.destroy()
		self.canvas = ttk.Frame(self.home)
		self.canvas.pack()
		ttk.Button(self.canvas, text='Fichar entrada', command = self.entrada).pack()
		ttk.Button(self.canvas, text='Fichar salida', command = self.salida).pack()
		ttk.Button(self.canvas, text='Salir', command = self.home.destroy).pack()
		
	def entrada(self):
		self.canvas.pack_forget()
		self.canvas.destroy()
		self.canvas = ttk.Frame(self.home)
		self.canvas.pack()
		
		up = ttk.Frame(self.canvas)
		up.pack(side=ttk.TOP)
		down = ttk.Frame(self.canvas)
		down.pack(side=ttk.BOTTOM)
		
		ttk.Label(up, text='Introduzca su código para que su entrada quede registrada').pack()
		ttk.Label(down, text='Código: ').grid(row=0, column=0)
		ttk.Entry(down, bd = 5).grid(row=0, column=1)
		ttk.Button(down, text='Fichar', command = self.entrada).grid(row=1, column=0)
		ttk.Button(down, text='Volver', command = self.inicio).grid(row=1, column=1)
		
	def salida(self):
		self.canvas.pack_forget()
		self.canvas.destroy()
		self.canvas = ttk.Frame(self.home)
		self.canvas.pack()
		
		up = ttk.Frame(self.canvas)
		up.pack(side=ttk.TOP)
		down = ttk.Frame(self.canvas)
		down.pack(side=ttk.BOTTOM)
		
		ttk.Label(up, text='Introduzca su código para que su salida quede registrada').pack()
		ttk.Label(down, text='Código: ').grid(row=0, column=0)
		ttk.Entry(down, bd = 5).grid(row=0, column=1)
		ttk.Button(down, text='Fichar', command = self.entrada).grid(row=1, column=0)
		ttk.Button(down, text='Volver', command = self.inicio).grid(row=1, column=1)
		