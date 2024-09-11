import sys
from PyQt6.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt6.QtGui import QFont

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setGeometry(300, 300, 300, 220)
    w.setWindowTitle('提示框')
    QToolTip.setFont(QFont('SansSerif', 20))
    w.setToolTip('这是一个窗口\nA')
    btn = QPushButton('Button', w)
    btn.setToolTip('这是一个按钮\nB')
    btn.resize(btn.sizeHint())
    btn.move(50, 50)
    w.show()
    sys.exit(app.exec())
