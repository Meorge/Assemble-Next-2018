import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
Qt = QtCore.Qt

class BlockItem(QtWidgets.QTreeWidgetItem):
	def __init__(self, parent=None):
		super(BlockItem, self).__init__(parent)
		self.parent = parent
		self.inputs = []

		self.backgroundTint = QtGui.QColor(255,255,255)

		self.title = "Empty node"

		self.CPPCode = "No CPP code loaded" # will be overwritten by the code that this 

		if parent:
			self.setupData()

	def setupData(self):
		#self.setText(0, self.title)

		self.TitleLabel = QtWidgets.QLabel(self.title)
		newLayout = QtWidgets.QHBoxLayout()

		newLayout.addWidget(self.TitleLabel)


		for inputItem in self.inputs:
			if inputItem["inputType"] == "float":
				#newLabel = QtWidgets.QLabel(inputItem["inputName"])
				newSpinBox = QtWidgets.QSpinBox()
				newSpinBox.setMinimum(-255)
				newSpinBox.setMaximum(255)
				newLayout.addWidget(newSpinBox)

				inputItem["inputWidget"] = newSpinBox

		self.itemWidget = QtWidgets.QWidget()
		self.itemWidget.setLayout(newLayout)
		self.parent.setItemWidget(self, 0, self.itemWidget)
		self.setIsCurrentSelection(False)
		self.TitleLabel.setStyleSheet("QLabel {color: black;}")

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
				inputWidget = inputItem["inputWidget"]
				inputVar = inputItem["internalName"]

				compositeCPP = compositeCPP.replace(inputVar, str(inputWidget.value()))

		return compositeCPP

	def setIsCurrentSelection(self, isSelected):
		if isSelected:
			print("Setting block with title " + self.title + " as current selection")
			self.TitleLabel.setStyleSheet("QLabel {color: white;}")
		else:
			print("Setting block with title " + self.title + " as not selected")
			self.TitleLabel.setStyleSheet("QLabel {color: black;}")

	def setTint(self):
		brush = QtGui.QBrush(self.backgroundTint)
		self.setBackground(0, brush)
		self.setBackground(-1, brush)
		print("IT HATH BEEN DONE")

	def mimeData(self):
		newMimeData = QtCore.QMimeData()
		newMimeData.setData("AN2018Block", self)

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
		print("the pasta is ready")

		return

	def addBlock(self, item):
		item.setupData()
		self.addTopLevelItem(item)
		item.setIsCurrentSelection(False)
		#self.takeTopLevelItem(self.indexFromItem(self.addBlockItem).row())
		self.setupAddBox()

	def itemChanged(self, current, previous):
		try:
			current.setIsCurrentSelection(True)
		except:
			pass
		print("AAAA")
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
		print(parent.title)

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
