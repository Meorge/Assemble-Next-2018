# A window test.

import os
import sys

import NodeKit as nl
import AppKit
#from NodeKit.AddNode import AddNode
#from NodeKit.FloatNode import FloatNode


from PyQt5 import QtCore, QtGui, QtWidgets
Qt = QtCore.Qt


import BlockKit
from ANBlocks.TransformationBlocks import *

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.mainCodeTree = BlockKit.BlockTreeWidget(parent=self)

        self.mainCodeView = QtWidgets.QPlainTextEdit()
        self.mainCodeViewFont = QtGui.QFont("Menlo")
        self.mainCodeViewFont.setStyleHint(QtGui.QFont.Monospace)
        self.mainCodeView.setFont(self.mainCodeViewFont)
        self.mainCodeView.setReadOnly(True)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.mainCodeTree)
        self.layout.addWidget(self.mainCodeView)

        self.mainWidget = QtWidgets.QWidget()
        self.mainWidget.setLayout(self.layout)
        self.setCentralWidget(self.mainWidget)

        test1 = TranslateXBlock(parent=self.mainCodeTree)

        #self.transXBlock.setText(0, "lolahah")
        self.mainCodeTree.addBlock(test1)


        self.CPPBuffer = """"""

        self.nodeList = [
        {
	        "categoryName": "Transform",
	        "categoryBlocks": [
			        TranslateXBlock(),
			        TranslateYBlock(),
			        TranslateZBlock(),
			        RotateXBlock(),
			        RotateYBlock(),
			        RotateZBlock(),
			        ScaleXBlock()
		        ]
        }]

        self.setupStatusBar()
        self.setupToolbox()


    def setupToolbox(self):
        self.toolboxDockWidget = QtWidgets.QDockWidget()
        #self.toolboxDockWidget.setTitle("Toolbox")
        #self.toolboxDockWidget.setWidget()
        self.addDockWidget(Qt.RightDockWidgetArea, self.toolboxDockWidget)

    def setupStatusBar(self):
    	self.statusBar = QtWidgets.QStatusBar()
    	self.setStatusBar(self.statusBar)

    	self.generateCodeButton = QtWidgets.QPushButton("Generate C++ Code")
    	self.generateCodeButton.clicked.connect(self.generateCPP)
    	self.statusBar.addWidget(self.generateCodeButton)


    def generateCPP(self):
    	self.CPPBuffer = """"""
    	
    	invisibleroot = self.mainCodeTree.invisibleRootItem()
    	child_count = invisibleroot.childCount()

    	for itemNo in range(child_count):
    		item = invisibleroot.child(itemNo)
    		print(item.title)
    		self.CPPBuffer += "\t" + item.CPPCodeComposite() + "\n"

    	self.CPPBufferWithHeaderFooter = "int assembleNextTestSprite::onExecute() {\n" + self.CPPBuffer + "\treturn true;\n}"
    	self.mainCodeView.setPlainText(self.CPPBufferWithHeaderFooter)

    def setupNodeView(self):
        self.nodeView = nl.NodeView()
        self.nodeScene = nl.NodeScene()

        self.nodeView.setScene(self.nodeScene)

        self.setCentralWidget(self.nodeView)

        self.nodeScene.addNode(testAddNode1)
        self.nodeScene.addNode(testFloatNode2)

        self.resize(750,500)

#################################
#################################


		
#################################
#################################

if __name__ == '__main__':
    global app, window
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    
