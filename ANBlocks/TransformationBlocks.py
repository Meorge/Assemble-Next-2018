import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
Qt = QtCore.Qt

from BlockKit import BlockItem



###########################
# Base Transform Template #
###########################
class BasicTransformBlock(BlockItem):
	def __init__(self, parent=None):
		super(BasicTransformBlock, self).__init__(parent)

class BasicXBlock(BasicTransformBlock):
	def __init__(self, parent=None):
		super(BasicXBlock, self).__init__(parent)

		self.backgroundTint = QtGui.QColor(255, 215, 215)
		self.setTint()

class BasicYBlock(BasicTransformBlock):
	def __init__(self, parent=None):
		super(BasicYBlock, self).__init__(parent)

		self.backgroundTint = QtGui.QColor(217, 255, 215)
		self.setTint()

class BasicZBlock(BasicTransformBlock):
	def __init__(self, parent=None):
		super(BasicZBlock, self).__init__(parent)

		self.backgroundTint = QtGui.QColor(215, 215, 255)
		self.setTint()

class BasicOtherBlock(BasicTransformBlock):
	def __init__(self, parent=None):
		super(BasicOtherBlock, self).__init__(parent)

		self.backgroundTint = QtGui.QColor(215, 215, 215)
		self.setTint()


###########################
#### Translate Blocks #####
###########################

class TranslateXYZBlock(BasicTransformBlock):
	def __init__(self, parent=None):
		super(TranslateXYZBlock, self).__init__(parent)
		self.setTitle("Translate")

		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Translate",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "by",
				"internalName": "label2"
			},
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~X~"
			},
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~Y~"
			},
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~Z~"
			}
		])

		self.setCPPCode("~POSTHING~->pos.x += ~X~;\n\t~POSTHING~->pos.y += ~Y~;\n\t~POSTHING~->pos.z += ~Z~;")

class TranslateXBlock(BasicXBlock):
	def __init__(self, parent=None):
		super(TranslateXBlock, self).__init__(parent)
		self.setTitle("Translate on X axis")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Translate",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "on X axis by",
				"internalName": "label2"
			},
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~X~"
			}
		])

		self.setCPPCode("~POSTHING~->pos.x += ~X~;")

class TranslateYBlock(BasicYBlock):
	def __init__(self, parent=None):
		super(TranslateYBlock, self).__init__(parent)
		self.setTitle("Translate on Y axis")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Translate",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "on Y axis by",
				"internalName": "label2"
			},
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~Y~"
			}
		])

		self.setCPPCode("~POSTHING~->pos.y += ~Y~;")


class TranslateZBlock(BasicZBlock):
	def __init__(self, parent=None):
		super(TranslateZBlock, self).__init__(parent)
		self.setTitle("Translate on Z axis")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Translate",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "on Z axis by",
				"internalName": "label2"
			},
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~Z~"
			}
		])

		self.setCPPCode("~POSTHING~->pos.z += ~Z~;")


###########################
###### Rotate Blocks ######
###########################

class RotateXYZBlock(BasicTransformBlock):
	def __init__(self, parent=None):
		super(RotateXYZBlock, self).__init__(parent)
		self.setTitle("Rotate")

		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Rotate",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "by",
				"internalName": "label2"
			},
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~X~"
			},
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~Y~"
			},
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~Z~"
			}
		])

		self.setCPPCode("~POSTHING~->rot.x += ~X~;\n\t~POSTHING~->rot.y += ~Y~;\n\t~POSTHING~->rot.z += ~Z~;")

class RotateXBlock(BasicXBlock):
	def __init__(self, parent=None):
		super(RotateXBlock, self).__init__(parent)
		self.setTitle("Rotate on X axis")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Rotate",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "on X axis by",
				"internalName": "label2"
			},
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~X~"
			}
		])

		self.setCPPCode("~POSTHING~->rot.x += ~X~;")

class RotateYBlock(BasicYBlock):
	def __init__(self, parent=None):
		super(RotateYBlock, self).__init__(parent)
		self.setTitle("Rotate on Y axis")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Rotate",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "on Y axis by",
				"internalName": "label2"
			},
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~Y~"
			}
		])

		self.setCPPCode("~POSTHING~->rot.y += ~Y~;")


class RotateZBlock(BasicZBlock):
	def __init__(self, parent=None):
		super(RotateZBlock, self).__init__(parent)
		self.setTitle("Rotate on Z axis")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Rotate",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "on Z axis by",
				"internalName": "label2"
			},
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~VAL~"
			}
		])

		self.setCPPCode("~POSTHING~->rot.z += ~VAL~;")


###########################
###### Scale Blocks #######
###########################
class ScaleXYZBlock(BasicTransformBlock):
	def __init__(self, parent=None):
		super(ScaleXYZBlock, self).__init__(parent)
		self.setTitle("Scale")

		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Scale",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "by",
				"internalName": "label2"
			},
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~X~"
			},
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~Y~"
			},
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~Z~"
			}
		])

		self.setCPPCode("~POSTHING~->scale.x += ~X~;\n\t~POSTHING~->scale.y += ~Y~;\n\t~POSTHING~->scale.z += ~Z~;")

class ScaleXBlock(BasicXBlock):
	def __init__(self, parent=None):
		super(ScaleXBlock, self).__init__(parent)
		self.setTitle("Scale on X axis")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Scale",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "on X axis by",
				"internalName": "label2"
			},
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~VAL~"
			}
		])

		self.setCPPCode("~POSTHING~->scale.x += ~VAL~;")

class ScaleYBlock(BasicYBlock):
	def __init__(self, parent=None):
		super(ScaleYBlock, self).__init__(parent)
		self.setTitle("Scale on Y axis")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Scale",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "on Y axis by",
				"internalName": "label2"
			},
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~VAL~"
			}
		])

		self.setCPPCode("~POSTHING~->scale.y += ~VAL~;")


class ScaleZBlock(BasicZBlock):
	def __init__(self, parent=None):
		super(ScaleZBlock, self).__init__(parent)
		self.setTitle("Scale on Z axis")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Scale",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "on Z axis by",
				"internalName": "label2"
			},
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~VAL~"
			}
		])

		self.setCPPCode("~POSTHING~->scale.z += ~VAL~;")

###############################################
###############################################
###############################################
###############################################

###########################
### Set Position Blocks ###
###########################
class SetPosXYZBlock(BasicTransformBlock):
	def __init__(self, parent=None):
		super(SetPosXYZBlock, self).__init__(parent)
		self.setTitle("Set position")

		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Set position of",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "to",
				"internalName": "label2"
			},
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~X~"
			},
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~Y~"
			},
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~Z~"
			}
		])

		self.setCPPCode("~POSTHING~->pos.x = ~X~;\n\t~POSTHING~->pos.y = ~Y~;\n\t~POSTHING~->pos.z = ~Z~;")

class SetPosXBlock(BasicXBlock):
	def __init__(self, parent=None):
		super(SetPosXBlock, self).__init__(parent)
		self.setTitle("Set X axis position")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Set X axis position of",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "to",
				"internalName": "label2"
			},
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~VAL~"
			}
		])

		self.setCPPCode("~POSTHING~->pos.x = ~VAL~;")

class SetPosYBlock(BasicYBlock):
	def __init__(self, parent=None):
		super(SetPosYBlock, self).__init__(parent)
		self.setTitle("Set Y axis position")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Set Y axis position of",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "to",
				"internalName": "label2"
			},
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~VAL~"
			}
		])

		self.setCPPCode("~POSTHING~->pos.y = ~VAL~;")


class SetPosZBlock(BasicZBlock):
	def __init__(self, parent=None):
		super(SetPosZBlock, self).__init__(parent)
		self.setTitle("Set Z axis position")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Set Z axis position of",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "to",
				"internalName": "label2"
			},
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~VAL~"
			}
		])

		self.setCPPCode("~POSTHING~->pos.z = ~VAL~;")


###########################
### Set Rotation Blocks ###
###########################
class SetRotXYZBlock(BasicTransformBlock):
	def __init__(self, parent=None):
		super(SetRotXYZBlock, self).__init__(parent)
		self.setTitle("Set rotation")

		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Set rotation of",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "to",
				"internalName": "label2"
			},
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~X~"
			},
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~Y~"
			},
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~Z~"
			}
		])

		self.setCPPCode("~POSTHING~->rot.x = ~X~;\n\t~POSTHING~->rot.y = ~Y~;\n\t~POSTHING~->rot.z = ~Z~;")

class SetRotXBlock(BasicXBlock):
	def __init__(self, parent=None):
		super(SetRotXBlock, self).__init__(parent)
		self.setTitle("Set X axis rotation")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Set X axis rotation of",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "to",
				"internalName": "label2"
			},
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~VAL~"
			}
		])

		self.setCPPCode("~POSTHING~->rot.x = ~VAL~;")

class SetRotYBlock(BasicYBlock):
	def __init__(self, parent=None):
		super(SetRotYBlock, self).__init__(parent)
		self.setTitle("Set Y axis rotation")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Set Y axis rotation of",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "to",
				"internalName": "label2"
			},
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~VAL~"
			}
		])

		self.setCPPCode("~POSTHING~->rot.y = ~VAL~;")


class SetRotZBlock(BasicZBlock):
	def __init__(self, parent=None):
		super(SetRotZBlock, self).__init__(parent)
		self.setTitle("Set Z axis rotation")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Set Z axis rotation of",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "to",
				"internalName": "label2"
			},
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~VAL~"
			}
		])

		self.setCPPCode("~POSTHING~->rot.z = ~VAL~;")


###########################
#### Set Scale Blocks #####
###########################

class SetScaleXYZBlock(BasicTransformBlock):
	def __init__(self, parent=None):
		super(SetScaleXYZBlock, self).__init__(parent)
		self.setTitle("Set scale")

		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Set scale of",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "to",
				"internalName": "label2"
			},
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~X~"
			},
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~Y~"
			},
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~Z~"
			}
		])

		self.setCPPCode("~POSTHING~->scale.x = ~X~;\n\t~POSTHING~->scale.y = ~Y~;\n\t~POSTHING~->scale.z = ~Z~;")

class SetScaleXBlock(BasicXBlock):
	def __init__(self, parent=None):
		super(SetScaleXBlock, self).__init__(parent)
		self.setTitle("Set X axis scale")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Set X axis scale of",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "to",
				"internalName": "label2"
			},
			{
				"inputName": "X",
				"inputType": "float",
				"internalName": "~VAL~"
			}
		])

		self.setCPPCode("~POSTHING~->scale.x = ~VAL~;")

class SetScaleYBlock(BasicYBlock):
	def __init__(self, parent=None):
		super(SetScaleYBlock, self).__init__(parent)
		self.setTitle("Set Y axis scale")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Set Y axis scale of",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "to",
				"internalName": "label2"
			},
			{
				"inputName": "Y",
				"inputType": "float",
				"internalName": "~VAL~"
			}
		])

		self.setCPPCode("~POSTHING~->scale.y = ~VAL~;")


class SetScaleZBlock(BasicZBlock):
	def __init__(self, parent=None):
		super(SetScaleZBlock, self).__init__(parent)
		self.setTitle("Set Z axis scale")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Set Z axis scale of",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~POSTHING~"
			},
			{
				"inputType": "label",
				"labelText": "to",
				"internalName": "label2"
			},
			{
				"inputName": "Z",
				"inputType": "float",
				"internalName": "~VAL~"
			}
		])

		self.setCPPCode("~POSTHING~->scale.z = ~VAL~;")

###########################
###### Other Blocks #######
###########################

class DeleteObjectBlock(BasicOtherBlock):
	def __init__(self, parent=None):
		super(DeleteObjectBlock, self).__init__(parent)
		self.setTitle("Delete actor")
		self.setInputs([
			{
				"inputType": "label",
				"labelText": "Delete",
				"internalName": "label1"
			},
			{
				"inputType": "actorAP",
				"internalName": "~ACTOR~"
			}])

		self.setCPPCode("~ACTOR~->Delete(1);")