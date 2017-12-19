import os
import sys
import NodeKit as nl

from PyQt5 import QtCore, QtGui, QtWidgets
Qt = QtCore.Qt


class AddNode(nl.Node):
	def __init__(self, parent=None):
		super(AddNode, self).__init__(parent)
		self.title = "Add"
		self.inputPinData = [
		{
			"viewerName": "A",
			"varType": "float",
			"varName": "A"},
		{
			"viewerName": "B",
			"varType": "float",
			"varName": "B"
		}
		]

		self.outputPinData = [
		{
			"viewerName": "Sum",
			"varType": "float",
			"varName": "sum"
		}
		]

		self.width = 100
		self.height = 100

