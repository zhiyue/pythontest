'''
Created on 2010/08/02

@author: hooxin
'''

import sys
from PyQt4 import QtGui

class GridLayout2(QtGui.QWidget):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.setWindowTitle('grid title')
		
		title=QtGui.QLabel('Title')
		author=QtGui.QLabel('Author')
		review=QtGui.QLabel('Review')
		test=QtGui.QLabel('test')
		
		titleEdit=QtGui.QLineEdit()
		authorEdit=QtGui.QLineEdit()
		reviewEdit=QtGui.QTextEdit()
		testEdit=QtGui.QTextEdit()
		
		grid=QtGui.QGridLayout()
		grid.setSpacing(10)
		
		grid.addWidget(title,1,0)
		grid.addWidget(titleEdit,1,1)
		
		grid.addWidget(author,2,0)
		grid.addWidget(authorEdit,2,1)
		
		grid.addWidget(review,3,0)
		grid.addWidget(reviewEdit,3,1)
		
		grid.addWidget(test,4,0)
		grid.addWidget(testEdit,4,1)
		
		
		self.setLayout(grid)
		self.resize(350,300)
		
		
app=QtGui.QApplication(sys.argv)
qb=GridLayout2()
qb.show()
sys.exit(app.exec_())