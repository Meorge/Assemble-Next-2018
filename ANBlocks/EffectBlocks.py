import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
Qt = QtCore.Qt

from BlockKit import BlockItem

###########################
## Base Effect Template ###
###########################

class BasicEffectBlock(BlockItem):
	moduleName = os.path.basename(__file__)
	def __init__(self, blockData=None, parent=None):
		super(BasicEffectBlock, self).__init__(blockData, parent)

		self.backgroundTint = QtGui.QColor(219, 198, 255)
		self.setTint()

###########################
## Base Effect Template ###
###########################

class SoundEffectBlock(BasicEffectBlock):
	title = ("Play a sound effect")
	listOfInputs = []

	inputs = [
		{
			"inputType": "label",
			"labelText": "Play sound effect",
			"internalName": "label1"
		},
		{
			"inputName": "SFX",
			"inputType": "editableCombo",
			"internalName": "~SFX",

		}
	]

	CPPCode = "PlaySound(this, ~SFX);"

	inputFilename = os.path.join(os.path.dirname(__file__), "SFXList.txt")


class VisualEffectBlock(BasicEffectBlock):
	title = "Play a visual effect"
	listOfInputs = []

	
	inputs = [
		{
			"inputType": "label",
			"labelText": "Play visual effect",
			"internalName": "label1"
		},
		{
			"inputName": "VFX",
			"inputType": "editableCombo",
			"internalName": "~VFX",

		}
	]

	inputFilename = os.path.join(os.path.dirname(__file__), "VFXList.txt")

	## TODO: Set up position, rotation, scale stuff
	CPPCode = "S16Vec simpleRot = {0,0,0};\n\tVec simpleScale = {1.0f, 1.0f, 1.0f};\n\tSpawnEffect(\"~VFX\", 0, &this->pos, &simpleRot, &simpleScale);"