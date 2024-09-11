import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QGuiApplication


class CenterWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 500)
        self.center()
        self.setWindowTitle('窗口居中')
        self.show()

    def center(self):
        # qr = self.frameGeometry()
        # desktop = app.desktop()
        screen = QGuiApplication.primaryScreen().availableGeometry()
        self.move(int((screen.width() - self.width()) / 2), int((screen.height() - self.height()) / 2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CenterWindow()
    sys.exit(app.exec())
