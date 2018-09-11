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

data_name = 'base.p'

class Backend:
	def __init__(self):
		a = os.path.dirname(os.path.abspath(__file__))
		self.base = pickle.load(open(a+"/base.p","rb"))