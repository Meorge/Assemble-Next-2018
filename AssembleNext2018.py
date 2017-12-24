# A window test.

import os
import sys
import importlib
import json

import NodeKit as nl
import AppKit
#from NodeKit.AddNode import AddNode
#from NodeKit.FloatNode import FloatNode


from PyQt5 import QtCore, QtGui, QtWidgets
Qt = QtCore.Qt


import BlockKit
from ANBlocks.TransformationBlocks import *
from ANBlocks.EffectBlocks import *

from ANClasses.SpriteClass import *

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

        self.currentCPPClass = NewerCPPClass_Sprite(parent=self)
        self.currentCPPFunction = preSpriteCollision()

        #self.layout.addWidget(self.mainCodeView)

        self.setCentralWidget(self.mainCodeTree)


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
        self.setupOutlineBox()

        self.setupMenuBar()


    def setupMenuBar(self):
        self.menuBar = QtWidgets.QMenuBar()
        self.fileMenu = self.menuBar.addMenu("&File")

        self.saveAsAction = QtWidgets.QAction("&Save As", self)
        self.saveAsAction.setShortcut(QtGui.QKeySequence.Save)
        self.saveAsAction.triggered.connect(self.saveFileAs)

        self.fileMenu.addAction(self.saveAsAction)
        self.setMenuBar(self.menuBar)

    def saveFileAs(self):
        print(self.generateSpriteContent())
        with open("out.an", "w") as file:
            #file.write(self.generateSpriteContent())
            file.close()

    def generateSpriteContent(self):
        """
        Four major levels of data:
        - Class
            - Category
                - Function
                    - Blocks
        """

        # Establishing class/overall variables (level 1)
        classDict = {}
        classDict["className"] = self.currentCPPClass.classInternalName
        classDict["categories"] = []

        
        # going to start looping through the categories of the class (level 2)
        for category in self.currentCPPClass.functions:
            catList = []
            categoryDict = {}
            categoryDict["categoryName"] = category["categoryName"]
            categoryDict["catFuncs"] = []

            blocklist = []
            # going to start looping through the functions in this category (level 3)
            for function in category["categoryFuncs"]:
                #print(function.__name__)
                newFuncDict = {}
                newFuncDict["functionName"] = function.__name__

                newFuncDict["functionBlocks"] = []

                #finally, start looping through the blocks in this function (level 4)

                #print("Function name is " + str(function.__name__) + ", blocks are " + str(function.blockPackedData))

                for block in function.blockPackedData:
                    #print(block.packedBlockData["blockName"])
                    newFuncDict["functionBlocks"].append(block.packedBlockData)

                categoryDict["catFuncs"].append(newFuncDict)

            # not it
            catList.append(categoryDict)
                
            # not it
            classDict["categories"].append(catList)

        savingJSON = json.dumps(classDict)
        return savingJSON

    """def saveAttemptTwo(self):
        invisibleroot = self.CPPFunctionOutline.invisibleRootItem()
        for childNo in range(invisibleRootItem.childCount()):
            if invisibleRootItem.child(childNo).childCount() > 0:
                for childNo_LVL2 in range(invisibleRootItem.child(childNo).childCount()):"""


    def setupOutlineBox(self):
        self.CPPFunctionOutline_DockW = QtWidgets.QDockWidget()
        self.CPPFunctionOutline_DockW.setWindowTitle("Outline")

        self.CPPFunctionOutline = OutlineTreeWidget()
        self.CPPFunctionOutline.currentItemChanged.connect(self.outlineItemChanged)
        self.CPPFunctionOutline.setHeaderHidden(True)
        self.CPPFunctionOutline.setMaximumWidth(300)

        self.rootOutlineItem = QtWidgets.QTreeWidgetItem()
        self.rootOutlineItem.setText(0, "assembleNextTestSprite")
        self.CPPFunctionOutline.addTopLevelItem(self.rootOutlineItem)

        for category in self.currentCPPClass.functions:
            newCategoryItem = OutlineTreeWidgetItem_Category()
            newCategoryItem.setText(0, category["categoryName"])
            self.rootOutlineItem.addChild(newCategoryItem)

            for func in category["categoryFuncs"]:
                newFuncItem = OutlineTreeWidgetItem_Func(func=func())
                newFuncItem.setText(0, func().title)
                newCategoryItem.addChild(newFuncItem)

        self.CPPFunctionOutline_DockW.setWidget(self.CPPFunctionOutline)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.CPPFunctionOutline_DockW)

        return

    def outlineItemChanged(self, current, previous):
        if type(current) != OutlineTreeWidgetItem_Func:
            print("OutlineTreeWidgetItem_Func is not " + str(type(current)) + ", so we're returning")
            return

        self.currentCPPFunction = current.func
        print(self.currentCPPFunction)
        print("We should have changed the function successfully")

        if type(previous) == OutlineTreeWidgetItem_Func:
            blockList = []
            for i in range(0, self.mainCodeTree.invisibleRootItem().childCount()):
                blockList.append(self.mainCodeTree.invisibleRootItem().child(i).packBlockData())
                #blockList.append("this should be saved" + str(self.mainCodeTree.invisibleRootItem().child(i)))


            previous.func.blocks = blockList
        self.mainCodeTree.clear()

        if type(current) == OutlineTreeWidgetItem_Func:
            for block in current.func.blocks:
                newBlock = self.createNewBlockFromData(block)
                #self.mainCodeTree.addBlock(newBlock)

        self.setWindowTitle("TestSpriteName - " + self.currentCPPFunction.title + " - Assemble Next 2018")

    def createNewBlockFromData(self, data):
        print("entering createNewBlockFromData func")
        print(data)
        #print("data[\"blockFile\"]: " + type(data["blockFile"]))
        moduleToImport = importlib.import_module(("ANBlocks." + data["blockFile"])[:-3])

        block = getattr(moduleToImport, data["blockName"])
        blockInstance = block(blockData=data, parent=self.mainCodeTree)
        self.mainCodeTree.addBlock(blockInstance)
        return

    def setupToolbox(self):
        self.toolboxDockWidget = QtWidgets.QDockWidget()
        self.toolboxDockWidget.setWindowTitle("Toolbox")
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
        return

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
                NewBlockListItem = BlockKit.BlockListItem(block["parent"].title, block["parent"])
                self.toolbox_TreeList.addTopLevelItem(NewBlockListItem)
                for subblock in block["children"]:
                    NewSubBlockListItem = BlockKit.BlockListItem(subblock.title, subblock)
                    NewBlockListItem.addChild(NewSubBlockListItem)

            else:
                NewBlockListItem = BlockKit.BlockListItem(block.title, block)
                self.toolbox_TreeList.addTopLevelItem(NewBlockListItem)
            #print("Added the block with title: " + block().title)

        return
        
        #print("Done refreshing the page")

    def addBlockFromList(self):
        currentlySelectedBlock = self.toolbox_TreeList.currentItem().blockClass(blockData=None, parent=self.mainCodeTree)
        #print(currentlySelectedBlock)

        self.mainCodeTree.addBlock(currentlySelectedBlock, True)

    def setupStatusBar(self):
        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)

        self.generateCodeButton = QtWidgets.QPushButton("Generate C++ Code")
        self.generateCodeButton.clicked.connect(self.generateCPP)
        #self.statusBar.addWidget(self.generateCodeButton)

    def generateCPP(self):
        self.CPPBuffer = """"""

        code_invisibleroot = self.mainCodeTree.invisibleRootItem()
        code_child_count = invisibleroot.childCount()

        for itemNo in range(child_count):
            item = invisibleroot.child(itemNo)
            #print(item.title)
            self.CPPBuffer += "\t" + item.CPPCodeComposite() + "\n"

        self.CPPBufferWithHeaderFooter = self.currentCPPClass.header + self.CPPBuffer + self.currentCPPClass.footer
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

class OutlineTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        super(OutlineTreeWidget, self).__init__(parent)
        
class OutlineTreeWidgetItem_Category(QtWidgets.QTreeWidgetItem):
    def __init__(self, parent=None):
        super(OutlineTreeWidgetItem_Category, self).__init__(parent)

class OutlineTreeWidgetItem_Func(QtWidgets.QTreeWidgetItem):
    def __init__(self, func=None, parent=None):
        super(OutlineTreeWidgetItem_Func, self).__init__(parent)
        self.func = func
        
#################################
#################################

if __name__ == '__main__':
    global app, window
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    
