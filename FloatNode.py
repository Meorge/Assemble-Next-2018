import os
import sys
import nodelib as nl

from PyQt5 import QtCore, QtGui, QtWidgets
Qt = QtCore.Qt


class FloatNode(nl.Node):
	def __init__(self, parent=None):
		super(FloatNode, self).__init__(parent)
		self.title = "Float Value"
		self.inputPinData = []

		self.outputPinData = [
		{
			"viewerName": "Value",
			"varType": "float",
			"varName": "value"
		}
		]

		self.inputWidgetData = [
		{
			"varType": "float"
		}]
		self.width = 175
		self.height = 70