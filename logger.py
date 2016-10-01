import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from PyQt5.QtCore import QCoreApplication, Qt, QTimer

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        self.setWindowTitle('Piezo Logger')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mw = MainWidget()
    mw.show()
    sys.exit(app.exec_())