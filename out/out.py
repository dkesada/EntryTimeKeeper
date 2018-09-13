#! /usr/bin/python
# -*- coding: utf-8 -*-
#author: David Quesada López

"""
Backend. Each time a user arrives, we will show it on an excell file.
It will read a dictionary for the users and codes and then it will create excells
for each day.

Will use Pickle to load a dictionary with the names and codes of the users, 
and OpenPyXL for creating and editing the excels
"""

import pickle
import datetime
import os
from openpyxl import Workbook
from openpyxl import load_workbook # To do

data_name = 'base.p'
file_name = './informes/'+datetime.datetime.now().strftime("%d-%m-%Y") + '.xlsx'

class Backend:
	def __init__(self):
		#a = os.path.dirname(os.path.abspath(__file__))
		with open(data_name,'rb') as f:
			self.base = pickle.load(f)
		self.date = datetime.datetime.today() # .day , .month , .year
		
		#Check if the file for today exists
		if not os.path.isfile(file_name):
			self.createFile()
		
	def createFile(self):
		wb = Workbook()
		ws = wb.active		
		for i in self.base.items():
			ws['A'+str(i[1][1])] = i[1][0].decode(encoding='latin1') #badly encoded
		wb.save(file_name)
	
	def check(self, code):
		"""
		Check if the code exists
		"""
		if code in self.base: return True
		else: return False
		
	
	def entry(self, code):
		"""
		First, check if the entry has already been registered.
		If not, register the entry
		"""
		ret = False
		wb = load_workbook(file_name)
		ws = wb['Sheet']
		
		if ws['D'+str(self.base[code][1])].value is None:
			hora = self.digits(datetime.datetime.now().hour) +':'+ self.digits(datetime.datetime.now().minute)
			ws['D'+str(self.base[code][1])] = hora
			wb.save(file_name)
			ret = True
		
		return ret
		
	def exit(self, code):
		"""
		First, check if the entry has already been registered.
		If not, register the entry
		"""
		ret = False
		wb = load_workbook(file_name)
		ws = wb['Sheet']
		
		if ws['E'+str(self.base[code][1])].value is None:
			hora = self.digits(datetime.datetime.now().hour) +':'+ self.digits(datetime.datetime.now().minute)
			ws['E'+str(self.base[code][1])] = hora
			wb.save(file_name)
			ret = True
		
		return ret
		
	def digits(self, num):
		""" Puts '0' before single digit numbers for format purposes """
		ret = str(num)
		if num < 10:
			ret = '0' + str(num)	
		return ret