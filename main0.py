import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_el(qp)
        qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_el(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        rc = randint(0, 100)
        qp.drawEllipse(randint(0 + rc, 451 - rc), randint(0 + rc, 538 - rc), rc, rc)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
