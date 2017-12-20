import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
Qt = QtCore.Qt

class BlockItem(QtWidgets.QTreeWidgetItem):
	def __init__(self, parent=None):
		super(BlockItem, self).__init__(parent)
		self.parent = parent
		self.inputs = [{"inputType": "float", "inputName": "X"}]

		self.title = "Empty node"

		self.CPPCode = "No CPP code loaded" # will be overwritten by the code that this 

		self.setupData()

	def setupData(self):
		#self.setText(0, self.title)

		TitleLabel = QtWidgets.QLabel(self.title)
		newLayout = QtWidgets.QHBoxLayout()
		newLayout.addWidget(TitleLabel)


		for inputItem in self.inputs:
			if inputItem["inputType"] == "float":
				#newLabel = QtWidgets.QLabel(inputItem["inputName"])
				newSpinBox = QtWidgets.QSpinBox()
				newSpinBox.setMinimum(-255)
				newSpinBox.setMaximum(255)
				newLayout.addWidget(newSpinBox)

				inputItem["inputWidget"] = newSpinBox

			elif inputItem["inputType"] == "editableCombo":
				newCombo = QtWidgets.QComboBox()
				newCombo.setEditable(True)
				print("setupData")
				newCombo.addItems(self.listOfInputs)
				newLayout.addWidget(newCombo)

				inputItem["inputWidget"] = newCombo

		itemWidget = QtWidgets.QWidget()
		itemWidget.setLayout(newLayout)
		self.parent.setItemWidget(self, 0, itemWidget)

	def columnCount(self):
		return len(self.inputs)

	def parent(self):
		return self.parent

	def setTitle(self, newTitle):
		self.title = newTitle

	def setCPPCode(self, newCode):
		self.CPPCode = newCode

	def setInputs(self, newInputs):
		self.inputs = newInputs

	def CPPCodeComposite(self):
		compositeCPP = self.CPPCode
		for inputItem in self.inputs:
			if inputItem["inputType"] == "float":
				print("We have a float")
				inputWidget = inputItem["inputWidget"]
				inputVar = inputItem["internalName"]

				print(inputWidget.value(), inputVar)
				compositeCPP = compositeCPP.replace(inputVar, str(inputWidget.value()))
				#compositeCPP = compositeCPP.replace("this", "blarg")
				print(compositeCPP)

		return compositeCPP


class BlockTreeWidget(QtWidgets.QTreeWidget):
	def __init__(self, parent=None):
		super(BlockTreeWidget, self).__init__(parent)

	def addBlock(self, item):
		item.setupData()
		self.addTopLevelItem(item)
