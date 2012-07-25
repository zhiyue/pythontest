#!/usr/bin/python
#coding=utf8
#filename=escape.py
'''
Created on 2010/08/08

@author: hooxin
'''

import sys
from PyQt4 import QtGui,QtCore

class Escape(QtGui.QWidget):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		
		self.setWindowTitle('escape')
		self.resize(250,150)
		
	def keyPressEvent(self,event):
		if event.key() == QtCore.Qt.Key_Escape:
			self.close()
		if event.key() == QtCore.Qt.Key_Enter:
			self.close()
		if event.key() == QtCore.Qt.Key_A:
			self.close()


app=QtGui.QApplication(sys.argv)
qb=Escape()
qb.show()
sys.exit(app.exec_())
