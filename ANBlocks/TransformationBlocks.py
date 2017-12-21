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
	title = "Translate"

	inputs = [
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
	]

	CPPCode = "~POSTHING~->pos.x += ~X~;\n\t~POSTHING~->pos.y += ~Y~;\n\t~POSTHING~->pos.z += ~Z~;"

	def __init__(self, parent=None):
		super(TranslateXYZBlock, self).__init__(parent)

class TranslateXBlock(BasicXBlock):
		title = "Translate on X axis"
		inputs = [
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
		]

		CPPCode = "~POSTHING~->pos.x += ~X~;"

class TranslateYBlock(BasicYBlock):
	title = "Translate on Y axis"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->pos.y += ~Y~;"


class TranslateZBlock(BasicZBlock):
	title = "Translate on Z axis"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->pos.z += ~Z~;"


###########################
###### Rotate Blocks ######
###########################

class RotateXYZBlock(BasicTransformBlock):
	title = "Rotate"

	inputs = [
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
	]

	CPPCode = "~POSTHING~->rot.x += ~X~;\n\t~POSTHING~->rot.y += ~Y~;\n\t~POSTHING~->rot.z += ~Z~;"

class RotateXBlock(BasicXBlock):
	title = "Rotate on X axis"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->rot.x += ~X~;"

class RotateYBlock(BasicYBlock):
	title = "Rotate on Y axis"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->rot.y += ~Y~;"


class RotateZBlock(BasicZBlock):
	title = "Rotate on Z axis"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->rot.z += ~VAL~;"


###########################
###### Scale Blocks #######
###########################
class ScaleXYZBlock(BasicTransformBlock):
	title = "Scale"

	inputs = [
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
	]

	CPPCode = "~POSTHING~->scale.x += ~X~;\n\t~POSTHING~->scale.y += ~Y~;\n\t~POSTHING~->scale.z += ~Z~;"

class ScaleXBlock(BasicXBlock):
	title = "Scale on X axis"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->scale.x += ~VAL~;"

class ScaleYBlock(BasicYBlock):
	title = "Scale on Y axis"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->scale.y += ~VAL~;"


class ScaleZBlock(BasicZBlock):
	title = "Scale on Z axis"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->scale.z += ~VAL~;"

###############################################
###############################################
###############################################
###############################################

###########################
### Set Position Blocks ###
###########################
class SetPosXYZBlock(BasicTransformBlock):
	title = "Set position"

	inputs = [
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
	]

	CPPCode = "~POSTHING~->pos.x = ~X~;\n\t~POSTHING~->pos.y = ~Y~;\n\t~POSTHING~->pos.z = ~Z~;"

class SetPosXBlock(BasicXBlock):
	title = "Set X axis position"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->pos.x = ~VAL~;"

class SetPosYBlock(BasicYBlock):
	title = "Set Y axis position"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->pos.y = ~VAL~;"


class SetPosZBlock(BasicZBlock):
	title = "Set Z axis position"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->pos.z = ~VAL~;"


###########################
### Set Rotation Blocks ###
###########################
class SetRotXYZBlock(BasicTransformBlock):
	title = "Set rotation"

	inputs = [
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
	]

	CPPCode = "~POSTHING~->rot.x = ~X~;\n\t~POSTHING~->rot.y = ~Y~;\n\t~POSTHING~->rot.z = ~Z~;"

class SetRotXBlock(BasicXBlock):
	title = "Set X axis rotation"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->rot.x = ~VAL~;"

class SetRotYBlock(BasicYBlock):
	title = "Set Y axis rotation"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->rot.y = ~VAL~;"


class SetRotZBlock(BasicZBlock):
	title = "Set Z axis rotation"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->rot.z = ~VAL~;"


###########################
#### Set Scale Blocks #####
###########################

class SetScaleXYZBlock(BasicTransformBlock):
	title = "Set scale"

	inputs = [
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
	]

	CPPCode = "~POSTHING~->scale.x = ~X~;\n\t~POSTHING~->scale.y = ~Y~;\n\t~POSTHING~->scale.z = ~Z~;"

class SetScaleXBlock(BasicXBlock):
	title = "Set X axis scale"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->scale.x = ~VAL~;"

class SetScaleYBlock(BasicYBlock):
	title = "Set Y axis scale"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->scale.y = ~VAL~;"


class SetScaleZBlock(BasicZBlock):
	title = "Set Z axis scale"
	inputs = [
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
	]

	CPPCode = "~POSTHING~->scale.z = ~VAL~;"

###########################
###### Other Blocks #######
###########################

class DeleteObjectBlock(BasicOtherBlock):
	title = "Delete actor"
	inputs = [
		{
			"inputType": "label",
			"labelText": "Delete",
			"internalName": "label1"
		},
		{
			"inputType": "actorAP",
			"internalName": "~ACTOR~"
		}]

	CPPCode = "~ACTOR~->Delete(1);"