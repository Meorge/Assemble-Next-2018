import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
Qt = QtCore.Qt

class NodeView(QtWidgets.QGraphicsView):
	def __init__(self, parent=None):
		super(NodeView, self).__init__(parent)
		self.setRenderHints(self.renderHints() | QtGui.QPainter.Antialiasing  | QtGui.QPainter.SmoothPixmapTransform)

	def mousePressEvent(self, event):
		event.ignore()
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
		super(NodeScene, self).mousePressEvent(event)

	def mouseMoveEvent(self, event):
		event.ignore()
		#print("move the scene")
		super(NodeScene, self).mouseMoveEvent(event)

	def drawBackground(self, painter, rect):
		self.backgroundBrush = QtGui.QBrush(QtGui.QColor(50,50,50))
		painter.setBrush(self.backgroundBrush)
		painter.setPen(QtGui.QPen(Qt.NoPen))
		painter.drawRect(rect)

#################################
#################################

class Node(QtWidgets.QGraphicsItem):
	def __init__(self, parent=None):
		super(Node, self).__init__(parent)
		self.title = "Node"
		self.width = 0
		self.height = 0
		self.x = 0
		self.y = 0

		self.inputPinData = []
		self.outputPinData = []

		self.inputWidgetData = []
		self.inputWidgets = []

		self.inputNodes = []
		self.outputNodes = []

		self.setAcceptHoverEvents(True)
		self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
		self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)

		self.isBeingDragged = False

		self.previousMousePosition = QtCore.QPointF()

		self.dropShadow = QtWidgets.QGraphicsDropShadowEffect()
		self.dropShadow.setOffset(0,0)
		self.dropShadow.setColor(QtGui.QColor(0,0,0,180))
		self.dropShadow.setBlurRadius(30)
		self.setGraphicsEffect(self.dropShadow)
		self.dropShadow.setEnabled(True)

	def EstablishInputsOutputs(self):
		self.inputNodes = []
		PinY = self.boundingRect().top() + 35
		for inputData in self.inputPinData:
			print("start: place input pin at " + str(PinY))
			newInputPin = IOPin(inputData, self.boundingRect().x() - 20, PinY, "input", parent=self)

			self.inputNodes.append(newInputPin)
			PinY += 30

			self.scene().addItem(newInputPin)

		self.outputNodes = []
		PinY = self.boundingRect().top() + 35
		for outputData in self.outputPinData:
			newOutputPin = IOPin(outputData, (self.boundingRect().x() + self.boundingRect().width()), PinY, "output", parent=self)

			self.outputNodes.append(newOutputPin)
			PinY += 30

			self.scene().addItem(newOutputPin)


		self.inputWidgets = []
		PinY = self.boundingRect().top() + 35
		for data in self.inputWidgetData:
			if data["varType"] == "float":
				newFloatProxyWidget = FloatValueWidget(0, PinY, parent=self)
				self.scene().addItem(newFloatProxyWidget)


















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
		painter.setPen(QtGui.QPen(QtGui.QColor(40,40,40)))

		

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
	def __init__(self, data, x, y, orientation, parent=None):
		super(IOPin, self).__init__(parent)

		self.x = x
		self.y = y
		self.rect = QtCore.QRect(x, y, 20, 20)

		self.parent = parent

		self.viewerName = data["viewerName"]
		self.varType = data["varType"]
		self.varName = data["varName"]

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


		self.data = data

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
			textRect = QtCore.QRectF(self.boundingRect().x() + self.margin(), self.boundingRect().y(), 200, self.boundingRect().height())
			painter.drawText(textRect, Qt.AlignVCenter + Qt.AlignLeft, self.viewerName)

		elif self.orientation == "output":

			textsize = painter.fontMetrics().size(Qt.TextSingleLine, self.viewerName)
			textRect = QtCore.QRect(0, self.boundingRect().y(), 200, self.boundingRect().height())
			textRect.setRight(self.boundingRect().x() - (self.margin() - 20))
			painter.drawText(textRect, Qt.AlignVCenter + Qt.AlignRight, self.viewerName)
		

	def margin(self):
		return ((self.boundingRect().width() / 2) + 20)

	def mousePressEvent(self, event):
		event.accept()
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

#################################
#################################

class FloatValueWidget(QtWidgets.QGraphicsProxyWidget):
	def __init__(self, x, y, parent=None):
		super(FloatValueWidget, self).__init__(parent)
		self.widget = QtWidgets.QSpinBox()
		self.setWidget(self.widget)

		self.x = x
		self.y = y

		self.setPos(self.x, self.y)

		self.parent = parent
		self.setParentItem(self.parent)
		self.setZValue(5)









