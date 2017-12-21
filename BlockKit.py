import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
Qt = QtCore.Qt

class BlockItem(QtWidgets.QTreeWidgetItem):
	def __init__(self, blockData=None, parent=None):
		super(BlockItem, self).__init__(parent)
		self.parent = parent
		self.inputs = []

		self.newBlockData = blockData

		self.backgroundTint = QtGui.QColor(255,255,255)

		self.title = "Empty node"

		self.CPPCode = "No CPP code loaded" # will be overwritten by the code that this 

		self.listOfInputs = ["wubba", "lubba"]

		print("parent is" + str(self.parent))
		#self.setupData()



	def setupData(self):
		#self.setText(0, self.title)

		self.TitleLabel = QtWidgets.QLabel(self.title)
		newLayout = QtWidgets.QHBoxLayout()

		#newLayout.addWidget(self.TitleLabel)


		for inputItem in self.inputs:
			if inputItem["inputType"] == "label":
				newLabel = QtWidgets.QLabel(inputItem["labelText"])
				newLayout.addWidget(newLabel)
				inputItem["inputWidget"] = newLabel

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
				
				newCombo.addItems(self.listOfInputs)
				newLayout.addWidget(newCombo)

				inputItem["inputWidget"] = newCombo

			elif inputItem["inputType"] == "actorAP":
				newCombo = ActorAPComboBox(parent=self.parent)

				newCombo.populateItems()
				newLayout.addWidget(newCombo)

				inputItem["inputWidget"] = newCombo

		self.itemWidget = QtWidgets.QWidget()
		self.itemWidget.setLayout(newLayout)

		self.parent.setItemWidget(self, 0, self.itemWidget)

		self.setIsCurrentSelection(False)
		self.TitleLabel.setStyleSheet("QLabel {color: black;}")

		print("We've set up the data")

		if self.newBlockData != None:
			self.unpackBlockData()

		return

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
			inputVar = inputItem["internalName"]
			inputWidget = inputItem["inputWidget"]

			if inputItem["inputType"] == "actorAP":
				compositeCPP = compositeCPP.replace(inputVar, str(inputWidget.codeValue))

			try:
				
				

				if inputItem["inputType"] == "float":
					compositeCPP = compositeCPP.replace(inputVar, str(inputWidget.value()))

				elif inputItem["inputType"] == "editableCombo":
					compositeCPP = compositeCPP.replace(inputVar, str(inputWidget.currentText()))



			except:
				pass

		return compositeCPP

	def setIsCurrentSelection(self, isSelected):
		if isSelected:
			#print("Setting block with title " + self.title + " as current selection")
			self.TitleLabel.setStyleSheet("QLabel {color: white;}")
		else:
			#print("Setting block with title " + self.title + " as not selected")
			self.TitleLabel.setStyleSheet("QLabel {color: black;}")

	def setTint(self):
		brush = QtGui.QBrush(self.backgroundTint)
		self.setBackground(0, brush)
		self.setBackground(-1, brush)

	def mimeData(self):
		newMimeData = QtCore.QMimeData()
		newMimeData.setData("AN2018Block", self)


	def populateListOfInputs(self, path):
		list = []
		with open(path, "r") as file:
			list = file.readlines()

		for i in list:
			self.listOfInputs.append(i.rstrip())

		return

	def packBlockData(self):
		blockVarData = []
		for i in self.inputs:
			if i["inputType"] == "label":
				continue

			varDict = {}
			varDict["var"] = i["internalName"]

			varDict["value"] = None
			if i["inputType"] == "float": varDict["value"] = i["inputWidget"].value()
			elif i["inputType"] == "editableCombo": varDict["value"] = i["inputWidget"].currentText()
			elif i["inputType"] == "actorAP": varDict["value"] = i["inputWidget"].currentIndex()

			blockVarData.append(varDict)

		blockData = {
			"blockName": self.__class__.__name__,
			"blockVars": blockVarData
		}
		print(blockData)
		return blockData

	def unpackBlockData(self):
		for i in self.inputs:

			for var in self.newBlockData:
				if i["internalName"] == var["var"]:
					if i["inputType"] == "float": i["inputWidget"].setValue(var["value"])
					elif i["inputType"] == "editableCombo": i["inputWidget"].setCurrentText(var["value"])
					elif i["inputType"] == "actorAP": i["inputWidget"].setCurrentIndex(var["value"])

		return


class BlockTreeWidget(QtWidgets.QTreeWidget):
	def __init__(self, parent=None):
		super(BlockTreeWidget, self).__init__(parent)

		self.parent = parent
		self.currentItemChanged.connect(self.itemChanged)
		self.setCurrentItem(None)

		self.setAcceptDrops(True)
		self.setDragEnabled(True)
		#self.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
		self.setHeaderHidden(True)
		self.setRootIsDecorated(False)

		self.setupAddBox()

	def setupAddBox(self):
		self.addBlockItem = QtWidgets.QTreeWidgetItem()

		self.addBlockItem_Label = QtWidgets.QLabel("Add a new block...")

		self.addBlockItem_Layout = QtWidgets.QHBoxLayout()
		self.addBlockItem_Layout.addWidget(self.addBlockItem_Label)

		self.addBlockItem_Widget = QtWidgets.QWidget()
		self.addBlockItem_Widget.setLayout(self.addBlockItem_Layout)

		
		#self.addTopLevelItem(self.addBlockItem)
		self.setItemWidget(self.addBlockItem, 0, self.addBlockItem_Widget)
		#print("the pasta is ready")

		return

	def addBlock(self, item):
		#item.setupData()
		print("addBlock() function with type item " + str(item))
		print("the parent *should* be " + str(self))
		newItem = item(parent=self)
		self.addTopLevelItem(newItem)
		#self.takeTopLevelItem(self.indexFromItem(self.addBlockItem).row())
		#self.setupAddBox()

	def itemChanged(self, current, previous):
		try:
			current.setIsCurrentSelection(True)
		except:
			pass
		#print("AAAA")
		try:
			previous.setIsCurrentSelection(False)
		except:
			pass

	def dragEnterEvent(self, event):
		event.acceptProposedAction()

	def dropEvent(self, event):
		event.acceptProposedAction()
		#print("drop event")
		print(event.mimeData().data("AN2018Block"))

	def dropMimeData(self, parent, index, data, action):
		#print(parent.title)
		pass

	def mousePressEvent(self, event):
		try:
			self.currentItem().setIsCurrentSelection(False)
		except:
			pass
		self.clearSelection()
		QtWidgets.QTreeWidget.mousePressEvent(self, event)

class BlockListItem(QtWidgets.QTreeWidgetItem):
	def __init__(self, name, blockClass, parent=None):
		super(BlockListItem, self).__init__(parent)

		self.name = name
		self.blockClass = blockClass
		self.setText(0, self.name)


class BlockListItemSource(QtWidgets.QTreeWidget):
	def __init__(self, parent=None):
		super(BlockListItemSource, self).__init__(parent)

		self.setDragEnabled(True)
		self.setHeaderHidden(True)

class BlockListItemSourceModel(QtCore.QAbstractItemModel):
	def __init__(self, parent=None):
		super(BlockListItemSourceModel, self).__init__(parent)

class ActorAPComboBox(QtWidgets.QComboBox):
	def __init__(self, parent=None):
		super(ActorAPComboBox, self).__init__(parent)
		self.parent = parent

		self.codeValue = ""

		self.currentIndexChanged.connect(self.updateCodeValue)

	def populateItems(self):
		if self.parent == None:
			print("This combo box can't find its parent QTreeWidget; therefore it cannot populate.")
			return

		if self.parent.parent == None:
			print("This combo box can't find the main class; therefore it cannot populate.")
			return

		print(self.parent.parent.currentCPPFunction())
		print(self.parent.parent.currentCPPFunction().title)
		print("Valid transform args: " + str(self.parent.parent.currentCPPFunction().validTransformArgs))

		self.validTransformArgs = self.parent.parent.currentCPPFunction().validTransformArgs

		for i in self.validTransformArgs:
			self.addItem(i["argVisibleName"])

		return

	def updateCodeValue(self, index):
		print(index)
		self.codeValue = self.validTransformArgs[index]["argCodeValue"]
		print(self.codeValue)

		