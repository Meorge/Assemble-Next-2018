# A window test.

import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
Qt = QtCore.Qt

class Window(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.nodeView = NodeView()
        self.nodeScene = NodeScene()

        self.nodeView.setScene(self.nodeScene)

        self.setCentralWidget(self.nodeView)


        testNode = Node("Add", 175, 100, -115, -170, ["Input 1", "Input 2"], ["Output"])

        testNode2 = Node("Display", 175, 100, -600, -170, ["Input"], [])
        self.nodeScene.addNode(testNode)
        #self.nodeScene.addNode(testNode2)

        #testNodeOutlet = InputNode("hoohoo", 0, 0)
        #self.nodeScene.addItem(testNodeOutlet)

#################################
#################################

class NodeView(QtWidgets.QGraphicsView):
	def __init__(self, parent=None):
		super(NodeView, self).__init__(parent)
		self.setRenderHints(self.renderHints() | QtGui.QPainter.Antialiasing  | QtGui.QPainter.SmoothPixmapTransform)

	def mousePressEvent(self, event):
		event.ignore()
		print("view is recieving")
		super(NodeView, self).mousePressEvent(event)

	def mouseMoveEvent(self, event):
		event.ignore()
		#print("move the view")
		super(NodeView, self).mouseMoveEvent(event)

#################################
#################################

class NodeScene(QtWidgets.QGraphicsScene):
	def __init__(self, parent=None):
		super(NodeScene, self).__init__(parent)



	def addNode(self, node):
		self.addItem(node)

		node.EstablishInputsOutputs()

	def mousePressEvent(self, event):
		event.ignore()
		print("scene is recieving")
		super(NodeScene, self).mousePressEvent(event)

	def mouseMoveEvent(self, event):
		event.ignore()
		#print("move the scene")
		super(NodeScene, self).mouseMoveEvent(event)

#################################
#################################

class Node(QtWidgets.QGraphicsItem):
	def __init__(self, title, width, height, x, y, inputs, outputs, parent=None):
		super(Node, self).__init__(parent)
		self.title = title
		self.width = width
		self.height = height
		self.x = x
		self.y = y

		self.inputs = inputs
		self.outputs = outputs

		self.inputNodes = []
		self.outputNodes = []

		self.setAcceptHoverEvents(True)
		self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
		self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)

		self.isBeingDragged = False

		self.previousMousePosition = QtCore.QPointF()

	def EstablishInputsOutputs(self):
		self.inputNodes = []
		PinY = self.boundingRect().top() + 35
		for inputname in self.inputs:
			print("start: place input pin at " + str(PinY))
			newInputNode = IOPin(inputname, self.boundingRect().x() - 20, PinY, "input", parent=self)

			self.inputNodes.append(newInputNode)
			PinY += 30

			self.scene().addItem(newInputNode)

		self.outputNodes = []
		PinY = self.boundingRect().top() + 35
		for outputname in self.outputs:
			newOutputNode = IOPin(outputname, (self.boundingRect().x() + self.boundingRect().width()), PinY, "output", parent=self)

			self.outputNodes.append(newOutputNode)
			PinY += 30

			self.scene().addItem(newOutputNode)

	def recalculatePins(self):
		PinY_2 = self.boundingRect().top() + 35
		for inputpin in self.inputNodes:
			print("place input pin at " + str(PinY_2))
			inputpin.x = self.boundingRect().x() - 20
			inputpin.y = PinY_2
			PinY_2 += 30



		PinY_2 = self.boundingRect().top() + 35
		for outputpin in self.outputNodes:
			inputpin.x = self.boundingRect().x() - 20
			inputpin.y = PinY_2
			PinY_2 += 30		

	def paint(self, painter, option, widget):
		painter.setPen(QtGui.QPen(QtGui.QColor(95,95,95)))

		

		gradient = QtGui.QLinearGradient(self.boundingRect().center().x(), self.boundingRect().bottom(), self.boundingRect().center().x(), self.boundingRect().top())
		gradient.setColorAt(0, QtGui.QColor(50,50,50))
		gradient.setColorAt(1, QtGui.QColor(100,100,100))

		
		brush = QtGui.QBrush(gradient)
		painter.setBrush(brush)
		painter.drawRoundedRect(self.x, self.y, self.width, self.height, 10, 10)


		headerGradient = QtGui.QLinearGradient(self.boundingRect().center().x(), self.boundingRect().top() + 50, self.boundingRect().center().x(), self.boundingRect().top())
		headerGradient.setColorAt(0, QtGui.QColor(28,79,160))
		headerGradient.setColorAt(1, QtGui.QColor(39,103,206))

		headerBrush = QtGui.QBrush(headerGradient)
		painter.setBrush(headerBrush)
		painter.setPen(QtGui.QPen(Qt.NoPen))
		painter.drawRoundedRect(self.x, self.y, self.width, 30, 10, 10)

		#painter.setPen(QtGui.QPen(QtGui.QColor(255,0,0)))
		#painter.setBrush(QtGui.QBrush(Qt.NoBrush))
		#painter.drawRect(self.boundingRect())

		painter.setPen(QtGui.QPen(QtGui.QColor(255,255,255)))
		titleRect = QtCore.QRect(self.boundingRect().left() + 10, self.boundingRect().top() + 7, 200, 50)
		painter.drawText(titleRect, Qt.AlignLeft, self.title)

		painter.setPen(QtGui.QPen(QtGui.QColor(255,0,0)))
		painter.drawPoint(self.scenePos())

	def mousePressEvent(self, event):
		event.accept()
		self.isBeingDragged = True
		super(Node, self).mousePressEvent(event)

	def mouseReleaseEvent(self, event):
		event.accept()
		self.isBeingDragged = False
		super(Node, self).mouseReleaseEvent(event)

	def mouseMoveEvent(self, event):
		event.ignore()
		print("Dragging a node")

		currentMousePosition = event.scenePos()

		mousePosVector = currentMousePosition - self.previousMousePosition


		newX = event.scenePos().x()
		newY = event.scenePos().y()


		#self.setPos(self.scenePos() + mousePosVector)

		#self.recalculatePins()

		self.previousMousePosition = currentMousePosition

		super(Node, self).mouseMoveEvent(event)

	def hoverEnterEvent(self, event):
		event.accept()
		#print("Node is being hovered over, like a fearful mother")
		super(Node, self).hoverEnterEvent(event)

		


	def boundingRect(self):
		return QtCore.QRectF(self.x, self.y, self.width, self.height)

#################################
#################################

class IOPin(QtWidgets.QGraphicsItem):
	def __init__(self, name, x, y, orientation, parent=None):
		super(IOPin, self).__init__(parent)

		self.x = x
		self.y = y
		self.rect = QtCore.QRect(x, y, 20, 20)

		self.parent = parent

		self.name = name

		self.currentMode = "idle"

		self.fillColor_idle = QtGui.QColor(75, 75, 75)
		self.fillColor_hover = QtGui.QColor(125, 125, 125)

		self.orientation = orientation
		self.setAcceptHoverEvents(True)
		self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)


		self.isBeingClickedOn = False

		self.newConnection = None

		self.parent = parent
		self.setParentItem(self.parent)

	def paint(self, painter, option, widget):
		painter.setPen(QtGui.QPen(Qt.NoPen))

		if self.currentMode == "idle":
			painter.setBrush(QtGui.QBrush(self.fillColor_idle))
		elif self.currentMode == "hover":
			painter.setBrush(QtGui.QBrush(self.fillColor_hover))
		painter.drawRect(QtCore.QRect(self.x, self.y, self.boundingRect().width(), self.boundingRect().height()))
		#painter.drawRect(self.rect)

		painter.setBrush(QtGui.QBrush(Qt.NoBrush))
		painter.setPen(QtGui.QPen(QtGui.QColor(244,66,66)))
		#painter.drawRect(self.boundingRect())

		painter.setPen(QtGui.QPen(QtGui.QColor(255,255,255)))
		if self.orientation == "input":
			textRect = QtCore.QRect(self.boundingRect().x() + self.margin(), self.boundingRect().y(), 200, self.boundingRect().height())
			painter.drawText(textRect, Qt.AlignVCenter + Qt.AlignLeft, self.name)

		elif self.orientation == "output":

			textsize = painter.fontMetrics().size(Qt.TextSingleLine, self.name)
			textRect = QtCore.QRect(0, self.boundingRect().y(), 200, self.boundingRect().height())
			textRect.setRight(self.boundingRect().x() - (self.margin() - 20))
			painter.drawText(textRect, Qt.AlignVCenter + Qt.AlignRight, self.name)
		

	def margin(self):
		return ((self.boundingRect().width() / 2) + 20)

	def mousePressEvent(self, event):
		event.accept()
		print("Node is being clicked on")
		self.isBeingClickedOn = True

		self.newConnection = NodeConnection(QtCore.QPointF(self.x + 10, self.y + 10), event.scenePos(), parent=self)
		self.scene().addItem(self.newConnection)
		super(IOPin, self).mousePressEvent(event)

	def mouseReleaseEvent(self, event):
		event.accept()
		self.isBeingClickedOn = False
		super(IOPin, self).mouseReleaseEvent(event)

	def hoverEnterEvent(self, event):
		event.accept()
		
		self.currentMode = "hover"
		super(IOPin, self).hoverEnterEvent(event)

	def hoverLeaveEvent(self, event):
		event.accept()
		
		self.currentMode = "idle"
		super(IOPin, self).hoverLeaveEvent(event)

	def mouseMoveEvent(self, event):
		#event.accept()
		#print("moving over a pin")
		if self.newConnection:
			#print("make a new pin connection")
			self.newConnection.setTargetPos(event.pos())
			#self.newConnection.paint()
			#self.newConnection.updatePath()

		
		super(IOPin, self).mouseMoveEvent(event)

	def mouseReleaseEvent(self, event):
		event.accept()

		self.scene().removeItem(self.newConnection)
		self.newConnection = None
		super(IOPin, self).mouseReleaseEvent(event)

	def boundingRect(self):
		return QtCore.QRectF(self.x, self.y, 20, 20)

#################################
#################################

class NodeConnection(QtWidgets.QGraphicsLineItem):
	def __init__(self, sourcePos, targetPos, parent=None):
		super(NodeConnection, self).__init__(parent)

		self.sourcePos = sourcePos
		self.targetPos = targetPos

		self.connectionColor = QtGui.QColor(65,65,65)
		self.pen = QtGui.QPen()
		self.pen.setColor(self.connectionColor)
		self.pen.setWidth(10)

		self.setPen(self.pen)

	"""def paint(self, painter, option, widget):
		pen = QtGui.QPen(QtGui.QColor(255,0,0))
		brush = QtGui.QBrush(QtGui.QColor(0,0,0))
		pen.setWidth(10)
		#self.setPen(pen)

		painter.setPen(pen)
		#painter.drawLine(self.sourcePos, self.targetPos)

		self.setPen(pen)
		#self.setBrush(brush)
		self.setWidth(100)
		self.setLine(self.sourcePos.x(), self.sourcePos.y(), self.targetPos.x(), self.targetPos.y())
		print("painting the node connection - should be happening A LOT")
		print(self.targetPos)
		#super(NodeConnection, self).paint(painter, option, widget)"""

	def setTargetPos(self, newTargetPos):
		self.targetPos = newTargetPos
		self.setLine(QtCore.QLineF(self.sourcePos, self.targetPos))
		print(self.line())
		
#################################
#################################

if __name__ == '__main__':
    global app, window
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())

    
