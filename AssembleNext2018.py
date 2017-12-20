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
from ANBlocks.EffectBlocks import *

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

        self.setMinimumSize(1200,600)

        self.layout = QtWidgets.QSplitter()

        #self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.mainCodeTree)
        self.layout.addWidget(self.mainCodeView)

        #self.mainWidget = QtWidgets.QWidget()
        #self.mainWidget.setLayout(self.layout)
        self.setCentralWidget(self.layout)


        self.currentCPPClass = playerCollisionClass(parent=self)

        #test1 = TranslateXBlock(parent=self.mainCodeTree)

        #self.transXBlock.setText(0, "lolahah")
        #self.mainCodeTree.addBlock(test1)


        self.CPPBuffer = """"""

        self.blockList = [
        {
            "categoryName": "Transform",
            "categoryBlocks": [
                {
                    "parent": TranslateXYZBlock,
                    "children": [
                        TranslateXBlock,
                        TranslateYBlock,
                        TranslateZBlock
                    ]
                },
                {
                    "parent": RotateXYZBlock,
                    "children": [
                        RotateXBlock,
                        RotateYBlock,
                        RotateZBlock
                        ]
                },
                {
                    "parent": ScaleXYZBlock,
                    "children": [
                        ScaleXBlock,
                        ScaleYBlock,
                        ScaleZBlock
                        ]
                },
                {
                    "parent": SetPosXYZBlock,
                    "children": [
                        SetPosXBlock,
                        SetPosYBlock,
                        SetPosZBlock
                        ]
                },
                {
                    "parent": SetRotXYZBlock,
                    "children": [
                        SetRotXBlock,
                        SetRotYBlock,
                        SetRotZBlock
                    ]
                },
                {
                    "parent": SetScaleXYZBlock,
                    "children": [
                        SetScaleXBlock,
                        SetScaleYBlock,
                        SetScaleZBlock
                    ]
                },

                DeleteObjectBlock

            ]
        },
        {
            "categoryName": "Effects",
            "categoryBlocks": [
                SoundEffectBlock,
                VisualEffectBlock
            ]
        },
        {
            "categoryName": "Empty",
            "categoryBlocks": [
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
        #print("\n\n\n")
        #print("Starting to refresh the page")
        #print("Index is " + str(index))

        numberOfBlocks = self.toolbox_TreeList.invisibleRootItem().childCount()
        #print("We should be deleting " + str(numberOfBlocks) + " items (same as the previous count)")
        """for itemNo in range(numberOfBlocks):
            print(self.toolbox_TreeList.takeTopLevelItem(itemNo))
            #print("removing an item")"""
        self.toolbox_TreeList.clear()

        #print("Current child count is " + str(self.toolbox_TreeList.invisibleRootItem().childCount()) + "; it should be 0")

        BlockList = []
        BlockList = self.blockList[index]["categoryBlocks"]
        #print("There are " + str(len(BlockList)) + " items in this list of blocks")
        for block in BlockList:

            if type(block) is dict:
                NewBlockListItem = BlockKit.BlockListItem(block["parent"]().title, block["parent"])
                self.toolbox_TreeList.addTopLevelItem(NewBlockListItem)
                for subblock in block["children"]:
                    NewSubBlockListItem = BlockKit.BlockListItem(subblock().title, subblock)
                    NewBlockListItem.addChild(NewSubBlockListItem)

            else:
                NewBlockListItem = BlockKit.BlockListItem(block().title, block)
                self.toolbox_TreeList.addTopLevelItem(NewBlockListItem)
            #print("Added the block with title: " + block().title)

        
        #print("Done refreshing the page")

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
            #print(item.title)
            self.CPPBuffer += "\t" + item.CPPCodeComposite() + "\n"

        self.CPPBufferWithHeaderFooter = "int assembleNextTestSprite::playerCollision(ActivePhysics *apThis, ActivePhysics *apOther) {\n" + self.CPPBuffer + "}"
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

class NewerCPPClass(object):
    validTransformArgs = []
    def __init__(self, parent=None):
        pass

        
class playerCollisionClass(NewerCPPClass):
    def __init__(self, parent=None):
        self.validTransformArgs = [
        {
            "argVisibleName": "this actor",
            "argCodeValue": "this",

        },
        {
            "argVisibleName": "colliding actor",
            "argCodeValue": "&apOther->owner"
        }]

#################################
#################################

if __name__ == '__main__':
    global app, window
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    
