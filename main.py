import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 451, 538)
        self.setWindowTitle('Фокус')
        self.pushButton = QPushButton(self)
        self.pushButton.setText('Tap')
        self.pushButton.resize(70, 20)
        self.pushButton.move(208, 518)
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
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        rc = randint(0, 100)
        qp.drawEllipse(randint(0 + rc, 451 - rc), randint(0 + rc, 538 - rc), rc, rc)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
