import turtle
import sys
from PySide import QtGui


class TurtleControl(QtGui.QWidget):

    def __init__(self, turtle):

        super(TurtleControl, self).__init__()
        self.turtle = turtle
        self.turtle.color(100, 0, 0)

        self.left_btn = QtGui.QPushButton('Left', self)
        self.right_btn = QtGui.QPushButton('Right', self)
        self.move_btn = QtGui.QPushButton('Move', self)

        self.distance_spin = QtGui.QSpinBox()

        self.color_label = QtGui.QLabel('Red', self)

        self.controlLayout = QtGui.QGridLayout()
        self.controlLayout.addWidget(self.left_btn, 0, 0)
        self.controlLayout.addWidget(self.right_btn, 0, 1)
        self.controlLayout.addWidget(self.distance_spin, 1, 0)
        self.controlLayout.addWidget(self.move_btn, 1, 1)
        self.controlLayout.addWidget(self.color_label, 2, 0)
        self.setLayout(self.controlLayout)

        self.distance_spin.setRange(0, 100)
        self.distance_spin.setSingleStep(5)
        self.distance_spin.setValue(20)

        self.move_btn.clicked.connect(self.move_turtle)
        self.left_btn.clicked.connect(self.turn_turtle_left)
        self.right_btn.clicked.connect(self.turn_turtle_right)

    def turn_turtle_left(self):

        self.turtle.left(45)

    def turn_turtle_right(self):

        self.turtle.right(45)

    def move_turtle(self):

        self.turtle.forward(self.distance_spin.value())


# Setup turtle
window = turtle.Screen()
window.colormode(255)
babbage = turtle.Turtle()

# Create a Qt application
app = QtGui.QApplication(sys.argv)
control_window = TurtleControl(babbage)
control_window.show()

# Enter Qt application
app.exec_()
sys.exit()
