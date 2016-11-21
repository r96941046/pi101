import turtle
import sys
from PySide import QtCore, QtGui


import ipdb; ipdb.set_trace();

class TurtleControl(QWidget):

    def __init__(self, turtle):

        super(TurtleControl, self).__init__()
        self.turtle = turtle
