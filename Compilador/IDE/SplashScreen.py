# this is the module in charge of the splash screen
# using a QProgressBar and QPixmap to show the branch
import ctypes
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QTextEdit, QWidget, QProgressBar, QLabel
from PyQt5.QtGui import QIcon, QRegion, QPainter, QPalette
from PyQt5.QtCore import QRect, QBasicTimer, Qt
from PyQt5.QtGui import QPixmap
import sys
from Compilador.IDE.MainWindow import Window
# this is the config of the ProgressBar
DEFAULT_STYLE = """
QProgressBar{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center
}

QProgressBar::chunk {
    background-color: red;
    width: 10px;
    margin: 1px;
}
"""
# the main window


class Splash(QMainWindow):
    # constructor method
    def __init__(self):
        super().__init__()
        # Window first Configuration
        self.title = "Pura Vida Compilador"
        self.width = 872
        self.height = 490
        self.setMinimumSize(872, 490)
        self.setMaximumSize(872, 490)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # first declaration of attributes
        self.timer = QBasicTimer()
        self.step = 0
        # modify the background color
        self.setStyleSheet("background-color: #808080;")
        # Take the window into the center
        resolution = ctypes.windll.user32
        with_resolution = resolution.GetSystemMetrics(0)
        height_resolution = resolution.GetSystemMetrics(1)
        self.left = (with_resolution / 2) - (self.frameSize().width() / 2)
        self.top = (height_resolution / 2) - (self.frameSize().height() / 2)
        # calling procedures to display window Widgets
        self.InitWindowConfiguration()
        self.CreateProgressBar()
        self.show()

    # This is the Window advanced configuration
    def InitWindowConfiguration(self):
        self.setWindowIcon(QtGui.QIcon("Resources/Icon.png"))
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("Resources/PantallaCargando.jpg"))
        self.label.setGeometry(0,0,872,490)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    # Configure the ProgressBar
    def CreateProgressBar(self):
        self.loading = QProgressBar(self)
        self.loading.setGeometry(90,280,500,30)
        self.loading.setStyleSheet(DEFAULT_STYLE)
        self.loading.setPalette(QPalette(Qt.black))


    # Filling the progressBar with events
    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.OpenWindow()
        self.step = self.step + 1
        self.loading.setValue(self.step)

    # opening the next window
    def OpenWindow(self):
        self.window = Window()
        self.close()


# The main method that initialize the application
def main():
    App = QApplication(sys.argv)
    window = Splash()
    window.timer.start(100, window)
    sys.exit(App.exec())


main()