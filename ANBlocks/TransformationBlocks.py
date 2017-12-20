import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
Qt = QtCore.Qt

from BlockKit import BlockItem

###########################
# Base Transform Template #
###########################

class BasicXBlock(BlockItem):
	def __init__(self, parent=None):
		super(BasicXBlock, self).__init__(parent)

		self.backgroundTint = QtGui.QColor(255, 215, 215)
		self.setTint()

class BasicYBlock(BlockItem):
	def __init__(self, parent=None):
		super(BasicYBlock, self).__init__(parent)

		self.backgroundTint = QtGui.QColor(217, 255, 215)
		self.setTint()

class BasicZBlock(BlockItem):
	def __init__(self, parent=None):
		super(BasicZBlock, self).__init__(parent)

		self.backgroundTint = QtGui.QColor(215, 215, 255)
		self.setTint()

class BasicOtherBlock(BlockItem):
	def __init__(self, parent=None):
		super(BasicOtherBlock, self).__init__(parent)

		self.backgroundTint = QtGui.QColor(215, 215, 215)
		self.setTint()


###########################
#### Translate Blocks #####
###########################

class TranslateXBlock(BasicXBlock):
	def __init__(self, parent=None):
		super(TranslateXBlock, self).__init__(parent)
		self.setTitle("Translate on X axis by")
		self.setInputs([
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~X"
			}
		])

		self.setCPPCode("this->pos.x += ~X;")

class TranslateYBlock(BasicYBlock):
	def __init__(self, parent=None):
		super(TranslateYBlock, self).__init__(parent)
		self.setTitle("Translate on Y axis by")
		self.setInputs([
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~Y"
			}
		])

		self.setCPPCode("this->pos.y += ~Y;")


class TranslateZBlock(BasicZBlock):
	def __init__(self, parent=None):
		super(TranslateZBlock, self).__init__(parent)
		self.setTitle("Translate on Z axis by")
		self.setInputs([
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~Z"
			}
		])

		self.setCPPCode("this->pos.z += ~Z;")


###########################
###### Rotate Blocks ######
###########################

class RotateXBlock(BasicXBlock):
	def __init__(self, parent=None):
		super(RotateXBlock, self).__init__(parent)
		self.setTitle("Rotate on X axis by")
		self.setInputs([
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~X"
			}
		])

		self.setCPPCode("this->rot.x += ~X;")

class RotateYBlock(BasicYBlock):
	def __init__(self, parent=None):
		super(RotateYBlock, self).__init__(parent)
		self.setTitle("Rotate on Y axis by")
		self.setInputs([
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~Y"
			}
		])

		self.setCPPCode("this->rot.y += ~Y;")


class RotateZBlock(BasicZBlock):
	def __init__(self, parent=None):
		super(RotateZBlock, self).__init__(parent)
		self.setTitle("Rotate on Z axis by")
		self.setInputs([
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~Z"
			}
		])

		self.setCPPCode("this->rot.z += ~Z;")


###########################
###### Scale Blocks #######
###########################

class ScaleXBlock(BasicXBlock):
	def __init__(self, parent=None):
		super(ScaleXBlock, self).__init__(parent)
		self.setTitle("Scale on X axis by")
		self.setInputs([
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~X"
			}
		])

		self.setCPPCode("this->scale.x += ~X;")

class ScaleYBlock(BasicYBlock):
	def __init__(self, parent=None):
		super(ScaleYBlock, self).__init__(parent)
		self.setTitle("Scale on Y axis by")
		self.setInputs([
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~Y"
			}
		])

		self.setCPPCode("this->scale.y += ~Y;")


class ScaleZBlock(BasicZBlock):
	def __init__(self, parent=None):
		super(ScaleZBlock, self).__init__(parent)
		self.setTitle("Rotate on Z axis by")
		self.setInputs([
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~Z"
			}
		])

		self.setCPPCode("this->scale.z += ~Z;")

###############################################
###############################################
###############################################
###############################################

###########################
### Set Position Blocks ###
###########################

class SetPosXBlock(BasicXBlock):
	def __init__(self, parent=None):
		super(SetPosXBlock, self).__init__(parent)
		self.setTitle("Set X axis position to")
		self.setInputs([
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~X"
			}
		])

		self.setCPPCode("this->pos.x = ~X;")

class SetPosYBlock(BasicYBlock):
	def __init__(self, parent=None):
		super(SetPosYBlock, self).__init__(parent)
		self.setTitle("Set Y axis position to")
		self.setInputs([
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~Y"
			}
		])

		self.setCPPCode("this->pos.y = ~Y;")


class SetPosZBlock(BasicZBlock):
	def __init__(self, parent=None):
		super(SetPosZBlock, self).__init__(parent)
		self.setTitle("Set Z axis position to")
		self.setInputs([
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~Z"
			}
		])

		self.setCPPCode("this->pos.z = ~Z;")


###########################
### Set Rotation Blocks ###
###########################

class SetRotXBlock(BasicXBlock):
	def __init__(self, parent=None):
		super(SetRotXBlock, self).__init__(parent)
		self.setTitle("Set X axis rotation to")
		self.setInputs([
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~X"
			}
		])

		self.setCPPCode("this->rot.x = ~X;")

class SetRotYBlock(BasicYBlock):
	def __init__(self, parent=None):
		super(SetRotYBlock, self).__init__(parent)
		self.setTitle("Set Y axis rotation to")
		self.setInputs([
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~Y"
			}
		])

		self.setCPPCode("this->rot.y = ~Y;")


class SetRotZBlock(BasicZBlock):
	def __init__(self, parent=None):
		super(SetRotZBlock, self).__init__(parent)
		self.setTitle("Set Z axis rotation to")
		self.setInputs([
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~Z"
			}
		])

		self.setCPPCode("this->rot.z = ~Z;")


###########################
#### Set Scale Blocks #####
###########################

class SetScaleXBlock(BasicXBlock):
	def __init__(self, parent=None):
		super(SetScaleXBlock, self).__init__(parent)
		self.setTitle("Set X axis scale to")
		self.setInputs([
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~X"
			}
		])

		self.setCPPCode("this->scale.x = ~X;")

class SetScaleYBlock(BasicYBlock):
	def __init__(self, parent=None):
		super(SetScaleYBlock, self).__init__(parent)
		self.setTitle("Set Y axis scale to")
		self.setInputs([
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~Y"
			}
		])

		self.setCPPCode("this->scale.y = ~Y;")


class SetScaleZBlock(BasicZBlock):
	def __init__(self, parent=None):
		super(SetScaleZBlock, self).__init__(parent)
		self.setTitle("Set Z axis scale to")
		self.setInputs([
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~Z"
			}
		])

		self.setCPPCode("this->scale.z = ~Z;")

###########################
###### Other Blocks #######
###########################

class DeleteObjectBlock(BasicOtherBlock):
	def __init__(self, parent=None):
		super(DeleteObjectBlock, self).__init__(parent)
		self.setTitle("Delete this actor")
		self.setInputs([])

		self.setCPPCode("this->Delete(1);")