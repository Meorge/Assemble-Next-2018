import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
Qt = QtCore.Qt

from BlockKit import BlockItem

###########################
## Base Effect Template ###
###########################

class BasicEffectBlock(BlockItem):
	def __init__(self, parent=None):
		super(BasicEffectBlock, self).__init__(parent)

		self.backgroundTint = QtGui.QColor(219, 198, 255)
		self.setTint()

###########################
## Base Effect Template ###
###########################

class SoundEffectBlock(BasicEffectBlock):
	def __init__(self, parent=None):
		super(SoundEffectBlock, self).__init__(parent)
		self.setTitle("Play a sound effect")
		self.listOfInputs = []

		
		self.setInputs([
			{
				"inputName": "SFX",
				"inputType": "editableCombo",
				"inputOptions": self.listOfInputs,
				"internalName": "~SFX",

			}
		])

		self.populateListOfInputs(os.path.join(os.path.dirname(__file__), "SFXList.txt"))

		if parent:
			self.setupData()
		self.setCPPCode("PlaySound(this, ~SFX);")

class VisualEffectBlock(BasicEffectBlock):
	def __init__(self, parent=None):
		super(VisualEffectBlock, self).__init__(parent)
		self.setTitle("Play a visual effect")
		self.listOfInputs = []

		
		self.setInputs([
			{
				"inputName": "VFX",
				"inputType": "editableCombo",
				"inputOptions": self.listOfInputs,
				"internalName": "~VFX",

			}
		])

		self.populateListOfInputs(os.path.join(os.path.dirname(__file__), "VFXList.txt"))

		if parent:
			self.setupData()

		## TODO: Set up position, rotation, scale stuff
		self.setCPPCode("S16Vec simpleRot = {0,0,0};\n\tVec simpleScale = {1.0f, 1.0f, 1.0f};\n\tSpawnEffect(\"~VFX\", 0, &this->pos, &simpleRot, &simpleScale);")