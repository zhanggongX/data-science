import sys
from PyQt6.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('第一个PyQt5应用')
    w.show()
    sys.exit(app.exec())
