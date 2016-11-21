import turtle
import sys
from PySide import QtCore, QtGui


class TurtleControl(QtGui.QWidget):

    def __init__(self, turtle):

        super(TurtleControl, self).__init__()
        self.turtle = turtle

        self.left_btn = QtGui.QPushButton('Left', self)
        self.right_btn = QtGui.QPushButton('Right', self)
        self.move_btn = QtGui.QPushButton('Move', self)

        self.distance_spin = QtGui.QSpinBox()

        self.controlLayout = QtGui.QGridLayout()
        self.controlLayout.addWidget(self.left_btn, 0, 0)
        self.controlLayout.addWidget(self.right_btn, 0, 1)
        self.controlLayout.addWidget(self.distance_spin, 1, 0)
        self.controlLayout.addWidget(self.move_btn, 1, 1)
        self.setLayout(self.controlLayout)

        self.distance_spin.setRange(0, 100)
        self.distance_spin.setSingleStep(5)
        self.distance_spin.setValue(20)

# Setup turtle
window = turtle.Screen()
babbage = turtle.Turtle()

# Create a Qt application
app = QtGui.QApplication(sys.argv)
control_window = TurtleControl(babbage)
control_window.show()

# Enter Qt application
app.exec_()
sys.exit()
