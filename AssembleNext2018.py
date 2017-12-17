# A window test.

import os
import sys
import nodelib as nl

from AddNode import AddNode
from FloatNode import FloatNode
from PyQt5 import QtCore, QtGui, QtWidgets
Qt = QtCore.Qt

class Window(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.nodeView = nl.NodeView()
        self.nodeScene = nl.NodeScene()

        self.nodeView.setScene(self.nodeScene)

        self.setCentralWidget(self.nodeView)


        #testNode = Node("Add", 175, 100, -115, -170, [{"name": "Input 1", "type": "float", "varname": "a"}, {"name": "Input 2", "type": "float", "varname": "b"}], [{"name": "Output", "type": "float"}])
        #testNode = nl.Node("Add", 175, 100, -115, -170, ["Input 1", "Input 2"], ["Output"])

        testAddNode1 = AddNode()
        testFloatNode2 = FloatNode()
        self.nodeScene.addNode(testAddNode1)
        self.nodeScene.addNode(testFloatNode2)

        self.resize(750,500)
        #self.nodeScene.addNode(testNode2)

        #testNodeOutlet = InputNode("hoohoo", 0, 0)
        #self.nodeScene.addItem(testNodeOutlet)

#################################
#################################


		
#################################
#################################

if __name__ == '__main__':
    global app, window
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())

    
