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
        self.mainCodeTree.setAttribute(Qt.WA_MacShowFocusRect, 0)

        self.mainCodeView = QtWidgets.QPlainTextEdit()
        self.mainCodeViewFont = QtGui.QFont("Menlo")
        self.mainCodeViewFont.setStyleHint(QtGui.QFont.Monospace)
        self.mainCodeView.setFont(self.mainCodeViewFont)
        self.mainCodeView.setReadOnly(True)

        self.layout = QtWidgets.QSplitter()

        #self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.mainCodeTree)
        self.layout.addWidget(self.mainCodeView)

        #self.mainWidget = QtWidgets.QWidget()
        #self.mainWidget.setLayout(self.layout)
        self.setCentralWidget(self.layout)

        test1 = TranslateXBlock(parent=self.mainCodeTree)

        #self.transXBlock.setText(0, "lolahah")
        self.mainCodeTree.addBlock(test1)


        self.CPPBuffer = """"""

        self.blockList = [
        {
            "categoryName": "Transform",
            "categoryBlocks": [
                    TranslateXBlock,
                    TranslateYBlock,
                    TranslateZBlock,
                    RotateXBlock,
                    RotateYBlock,
                    RotateZBlock,
                    ScaleXBlock,
                    ScaleYBlock,
                    ScaleZBlock,
                    SetPosXBlock,
                    SetPosYBlock,
                    SetPosZBlock,
                    SetRotXBlock,
                    SetRotYBlock,
                    SetRotZBlock,
                    SetScaleXBlock,
                    SetScaleYBlock,
                    SetScaleZBlock,
                    DeleteObjectBlock

                ]
        },
        {
            "categoryName": "Other",
            "categoryBlocks": [
                    RotateZBlock
                ]
        }]

        self.setupStatusBar()
        self.setupToolbox()


    def setupToolbox(self):
        self.toolboxDockWidget = QtWidgets.QDockWidget()
        #self.toolboxDockWidget.setTitle("Toolbox")
        #self.toolboxDockWidget.setWidget()

        self.toolbox_TabWidget = QtWidgets.QTabWidget()

        self.toolbox_ComboBox = QtWidgets.QComboBox()

        self.toolbox_TreeList = BlockKit.BlockListItemSource()

        self.toolbox_AddNodeButton = QtWidgets.QPushButton("Add Node")
        self.toolbox_AddNodeButton.clicked.connect(self.addBlockFromList)

        for category in self.blockList:
            self.toolbox_ComboBox.addItem(category["categoryName"])

        #self.toolboxDockWidget.setTitleBarWidget(self.toolbox_ComboBox)
        self.toolbox_Layout = QtWidgets.QVBoxLayout()
        self.toolbox_Layout.addWidget(self.toolbox_ComboBox)
        self.toolbox_Layout.addWidget(self.toolbox_TreeList)
        self.toolbox_Layout.addWidget(self.toolbox_AddNodeButton)
        self.toolbox_Widget = QtWidgets.QWidget()
        self.toolbox_Widget.setLayout(self.toolbox_Layout)

        self.toolboxDockWidget.setWidget(self.toolbox_Widget)

        self.toolbox_ComboBox.currentIndexChanged.connect(self.toolboxCategoryChanged)

        self.addDockWidget(Qt.RightDockWidgetArea, self.toolboxDockWidget)

        self.toolboxCategoryChanged(0)

    def toolboxCategoryChanged(self, index):
        numberOfBlocks = self.toolbox_TreeList.invisibleRootItem().childCount()

        for itemNo in range(numberOfBlocks):
            self.toolbox_TreeList.takeTopLevelItem(itemNo)

        BlockList = []
        BlockList = self.blockList[index]["categoryBlocks"]
        print("Found it")


        for block in BlockList:
            NewBlockListItem = BlockKit.BlockListItem(block().title, block)
            self.toolbox_TreeList.addTopLevelItem(NewBlockListItem)

        print(BlockList)

    def addBlockFromList(self):
        currentlySelectedBlock = self.toolbox_TreeList.currentItem().blockClass(parent=self.mainCodeTree)
        self.mainCodeTree.addBlock(currentlySelectedBlock)

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

    
