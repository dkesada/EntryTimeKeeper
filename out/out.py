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
file_name = datetime.datetime.now().strftime("%d-%m-%Y") + '.xlsx'

class Backend:
	def __init__(self):
		#a = os.path.dirname(os.path.abspath(__file__))
		self.base = pickle.load(open(data_name,"rb"))
		self.date = datetime.datetime.today() # .day , .month , .year
		
		#Check if the file for today exists
		if not os.path.isfile(file_name):
			self.createFile()
		
	def createFile(self):
		wb = Workbook()
		ws = wb.active		
		for i in self.base.items():
			ws['A'+str(i[1][1])] = i[1][0].decode(encoding='utf_8') #badly encoded
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
		hora = str(datetime.datetime.now().hour) +':'+ str(datetime.datetime.now().minute)