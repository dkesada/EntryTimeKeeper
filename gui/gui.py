#! /usr/bin/python
# -*- coding: utf-8 -*-
# author: David Quesada López

"""
User interface, let's see how Tkinter goes.
"""

import tkinter as ttk


class Gui:
    def __init__(self, back):
        self.backend = back
        self.home = ttk.Tk()

        self.home.geometry('400x200')
        self.home.resizable(width=False, height=False)
        self.home.configure(bg='beige')
        self.home.title('Home')
        self.canvas = ttk.Frame(self.home)
        self.inicio()

        self.home.mainloop()

    def inicio(self):
        # Frame que se irá destruyendo
        self.canvas.pack_forget()
        self.canvas.destroy()
        self.canvas = ttk.Frame(self.home)
        self.canvas.pack()
        ttk.Button(self.canvas, text='Fichar entrada',
                   command=lambda: self.entrada('Introduzca su código para que su entrada quede registrada')).pack()
        ttk.Button(self.canvas, text='Fichar salida',
                   command=lambda: self.salida('Introduzca su código para que su salida quede registrada')).pack()
        ttk.Button(self.canvas, text='Gestionar usuarios',
                   command=lambda: self.login('Introduzca el código del administrador')).pack()
        ttk.Button(self.canvas, text='Salir', command=self.home.destroy).pack()

    def entrada(self, t):
        self.canvas.pack_forget()
        self.canvas.destroy()
        self.canvas = ttk.Frame(self.home)
        self.canvas.pack()

        up = ttk.Frame(self.canvas)
        up.pack(side=ttk.TOP)
        down = ttk.Frame(self.canvas)
        down.pack(side=ttk.BOTTOM)

        ttk.Label(up, text=t).pack()
        ttk.Label(down, text='Código: ').grid(row=0, column=0)
        entry = ttk.Entry(down, bd=5)
        entry.grid(row=0, column=1)
        ttk.Button(down, text='Fichar', command=lambda: self.processEntry(entry.get())).grid(row=1, column=0)
        ttk.Button(down, text='Volver', command=self.inicio).grid(row=1, column=1)

    def processEntry(self, code):
        """
        Takes the code introduced by the user, checks that it is valid and registers the entry
        """
        if self.backend.check(code):
            if self.backend.entry(code):
                self.entrada('Su entrada ha quedado registrada, gracias por su tiempo.')
            else:
                self.entrada('El código introducido ya ha fichado por hoy.')
        else:
            self.entrada('El código introducido no existe. Por favor, introdúzca un código válido.')

    def salida(self, t):
        self.canvas.pack_forget()
        self.canvas.destroy()
        self.canvas = ttk.Frame(self.home)
        self.canvas.pack()

        up = ttk.Frame(self.canvas)
        up.pack(side=ttk.TOP)
        down = ttk.Frame(self.canvas)
        down.pack(side=ttk.BOTTOM)

        ttk.Label(up, text=t).pack()
        ttk.Label(down, text='Código: ').grid(row=0, column=0)
        entry = ttk.Entry(down, bd=5)
        entry.grid(row=0, column=1)
        ttk.Button(down, text='Fichar salida', command=lambda: self.processExit(entry.get())).grid(row=1, column=0)
        ttk.Button(down, text='Volver', command=self.inicio).grid(row=1, column=1)

    def processExit(self, code):
        """
        Takes the code introduced by the user, checks that it is valid and registers the entry
        """
        if self.backend.check(code):
            if self.backend.exit(code):
                self.salida('Su salida ha quedado registrada, gracias por su tiempo.')
            else:
                self.salida('El código introducido ya ha fichado su salida por hoy.')
        else:
            self.salida('El código introducido no existe. Por favor, introdúzca un código válido.')

    def gestion(self, t='Elija añadir o eliminar usuarios.'):
        self.canvas.pack_forget()
        self.canvas.destroy()
        self.canvas = ttk.Frame(self.home)
        self.canvas.pack()

        up = ttk.Frame(self.canvas)
        up.pack(side=ttk.TOP)
        down = ttk.Frame(self.canvas)
        down.pack(side=ttk.BOTTOM)

        ttk.Label(up, text=t).pack()
        ttk.Button(self.canvas, text='Añadir',
                   command=lambda: self.addUser('Introduzca el nombre completo del nuevo usuario.')).pack()
        ttk.Button(self.canvas, text='Eliminar',
                   command=lambda: self.delUser('Introduzca el código del usuario a eliminar.')).pack()
        ttk.Button(self.canvas, text='Volver', command=self.inicio).pack()

    def addUser(self, t):
        self.canvas.pack_forget()
        self.canvas.destroy()
        self.canvas = ttk.Frame(self.home)
        self.canvas.pack()

        up = ttk.Frame(self.canvas)
        up.pack(side=ttk.TOP)
        down = ttk.Frame(self.canvas)
        down.pack(side=ttk.BOTTOM)

        ttk.Label(up, text=t).pack()
        ttk.Label(down, text='Nombre completo: ').grid(row=0, column=0)
        entry = ttk.Entry(down, bd=5)
        entry.grid(row=0, column=1)
        ttk.Button(down, text='Añadir', command=lambda: self.processAdd(entry.get())).grid(row=1, column=0)
        ttk.Button(down, text='Volver', command=self.gestion).grid(row=1, column=1)

    def processAdd(self, name):
        """
        Takes the name introduced by the user and adds a new user to the database
        """
        code = self.backend.addUser(name)
        self.backend.deleteFile()
        self.backend.createFile()
        self.addUser('Usuario añadido correctamente. Su código es ' + code)

    def delUser(self, t):
        self.canvas.pack_forget()
        self.canvas.destroy()
        self.canvas = ttk.Frame(self.home)
        self.canvas.pack()

        up = ttk.Frame(self.canvas)
        up.pack(side=ttk.TOP)
        down = ttk.Frame(self.canvas)
        down.pack(side=ttk.BOTTOM)

        ttk.Label(up, text=t).pack()
        ttk.Label(down, text='Código: ').grid(row=0, column=0)
        entry = ttk.Entry(down, bd=5)
        entry.grid(row=0, column=1)
        ttk.Button(down, text='Eliminar', command=lambda: self.processDel(entry.get())).grid(row=1, column=0)
        ttk.Button(down, text='Volver', command=self.gestion).grid(row=1, column=1)

    def processDel(self, code):
        """
        Takes the code introduced by the user and deletes the corresponding entry in the database
        """
        if self.backend.check(code):
            self.backend.delUser(code)
            self.backend.deleteFile()
            self.backend.createFile()
            self.delUser('Usuario eliminado correctamente.')
        else:
            self.delUser('El código introducido no existe. Por favor, introdúzca un código válido.')

    def login(self, t):
        self.canvas.pack_forget()
        self.canvas.destroy()
        self.canvas = ttk.Frame(self.home)
        self.canvas.pack()

        up = ttk.Frame(self.canvas)
        up.pack(side=ttk.TOP)
        down = ttk.Frame(self.canvas)
        down.pack(side=ttk.BOTTOM)

        ttk.Label(up, text=t).pack()
        ttk.Label(down, text='Código: ').grid(row=0, column=0)
        entry = ttk.Entry(down, bd=5)
        entry.grid(row=0, column=1)
        ttk.Button(down, text='Login', command=lambda: self.processLogin(entry.get())).grid(row=1, column=0)
        ttk.Button(down, text='Volver', command=self.inicio).grid(row=1, column=1)

    def processLogin(self, code):
        """
        Takes the code introduced by the user, checks that it is the same code as the admin's
        """
        if self.backend.checkAdmin(code):
            self.gestion()
        else:
            self.login('Código no válido. Introduzca el código del administrador')
