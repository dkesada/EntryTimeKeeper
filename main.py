#! /usr/bin/python
# -*- coding: utf-8 -*-
#author: David Quesada López

"""
First, we'll build the interface. Then, the backend. 
Lastly, we'll see how to put all the info down in a not yet decided file format.
"""

from gui import gui
from out import out

def main():
	back = out.Backend()
	prog = gui.Gui(back)
	return 0
	
main()