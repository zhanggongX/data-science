import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon

# 增加窗口图标
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setGeometry(300, 300, 300, 220)
    w.setWindowTitle('窗口图标')
    app.setWindowIcon(QIcon('python.png'))
    w.show()
    sys.exit(app.exec())
