import ctypes
import os
import webbrowser
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QAction, QTextEdit, QMessageBox, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon
from Compilador.IDE import SyntaxColor
from Compilador.IDE.SyntaxColor import *


class Window(QMainWindow):
    # constructor method
    def __init__(self):
        super().__init__()
        self.title = "Pura Vida Compilador"
        # dimensions
        self.width = 800
        self.height = 700
        self.setMinimumSize(800, 700)
        self.setMaximumSize(800, 700)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # modify the background color
        self.setStyleSheet("background-color: #808080;")
        # center the window
        resolution = ctypes.windll.user32
        with_resolution = resolution.GetSystemMetrics(0)
        height_resolution = resolution.GetSystemMetrics(1)
        self.left = (with_resolution / 2) - (self.frameSize().width() / 2)
        self.top = (height_resolution / 2) - (self.frameSize().height() / 2)
        # calling the configuration procedures
        self.InitWindowConfiguration()
        self.Create_ToolBar()
        self.Create_TextEdit()
        self.show()

    # the window config
    def InitWindowConfiguration(self):
        # here we have to set the window icon
        self.setWindowIcon(QtGui.QIcon("Resources\Icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    # configuration of ToolBar menu
    def Create_ToolBar(self):
        # creating the action buttons and icons
        exitAction = QAction(QIcon("Resources/cancel.png"), "Close Program", self)
        exitAction.triggered.connect(self.Close_App)

        openAction = QAction(QIcon("Resources/folder.png"), "Open a existing file", self)
        openAction.triggered.connect(self.Open_Code)

        compiAction = QAction(QIcon("Resources/check.png"), "Compile the code", self)
        compiAction.triggered.connect(self.OnClickCompileButton)

        infoAction = QAction(QIcon("Resources/info.png"), "About Us", self)
        infoAction.triggered.connect(self.OpenGitHub)

        newAction = QAction(QIcon("Resources/new.png"), "New File", self)
        newAction.triggered.connect(self.Code_New)

        saveAction = QAction(QIcon("Resources/save.png"), "Save this code", self)
        saveAction.triggered.connect(self.Save_Code)

        # adding the actions to the ToolBar
        self.toolbar = self.addToolBar("ToolBar")
        self.toolbar.addAction(newAction)
        self.toolbar.addAction(openAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(compiAction)
        self.toolbar.addAction(infoAction)
        self.toolbar.addAction(exitAction)
        self.toolbar.setMovable(False)

    # this the Widget in charge of the text area where the code is written
    def Create_TextEdit(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        self.textEdit.setStyleSheet("background-color: #003153;")
        # change the text font
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setAcceptRichText(False)
        # Linking the textEdit with the Syntax Color beast module
        self.highlight = SyntaxColor.PythonHighlighter(self.textEdit.document())

    # procedure in charge of the program exit
    def Close_App(self):
        self.close()

    # procedure that validate the compile button, at now, it does nothing but is waiting for the logic
    def OnClickCompileButton(self):
        print(self.textEdit.toPlainText())

    # when user clicks info button
    def OpenGitHub(self):
        url = "https://github.com/OscarAraya18/CE3104_LedCube8"
        webbrowser.open(url)

    # when user clicks save
    def Save_Code(self):
        filename = QFileDialog.getSaveFileName(self,"Save Code", os.getenv('Home'))
        if filename[0]:
            f = open(filename[0], 'w')
            with f:
                code = self.textEdit.toPlainText()
                f.write(code)
                #using QMessageBox
                mb = QMessageBox()
                mb.setWindowTitle("Save File")
                mb.setText("Your file was saved successfully")
                mb.setIcon(QMessageBox.Information)
                x = mb.exec()

    # when user wants to open an existing file.txt
    def Open_Code(self):
        filename = QFileDialog.getOpenFileName(self,"Choose the file", os.getenv('Home'))
        if filename[0]:
            f = open(filename[0], 'r')
            with f:
                open_code = f.read()
                self.textEdit.setText(open_code)

    # this procedure delete the actual code and create a new file to code
    def Code_New(self):
        mb = QMessageBox()
        mb.setWindowTitle("New File")
        mb.setText("Are you sure that you want to create a new file,")
        mb.setIcon(QMessageBox.Information)
        mb.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        mb.buttonClicked.connect(self.popup_button)
        x = mb.exec()

    #validating the Yes|No option in the MessageBox
    def popup_button(self, i):
        print(i.text())
        if i.text() == "&Yes":
            self.textEdit.clear()