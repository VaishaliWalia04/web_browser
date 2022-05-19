import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton, QToolBar, QLabel)
from PyQt5.QtWebEngineWidgets import *


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.toolBar = QToolBar(self)
        self.addToolBar(self.toolBar)

        self.setStyleSheet("background-color: black;")

        self.backBtn = QPushButton()
        self.backBtn.setEnabled(False)
        self.backBtn.clicked.connect(self.back)
        self.backBtn.setIcon(QIcon("./back.png"))
        self.backBtn.setIconSize(QSize(32, 32))
        self.backBtn.setStyleSheet("background: transparent;")
        self.toolBar.addWidget(self.backBtn)

        self.forBtn = QPushButton()
        self.forBtn.setEnabled(False)
        self.forBtn.clicked.connect(self.forward)
        #self.forBtn.setFont(QFont('Verdana'))
        self.forBtn.setIcon(QIcon("./front.png"))
        self.forBtn.setIconSize(QSize(32, 32))
        self.forBtn.setStyleSheet("background: transparent;")
        self.toolBar.addWidget(self.forBtn)

        self.reloadBtn = QPushButton()
        self.reloadBtn.clicked.connect(self.reload)
        self.reloadBtn.setIcon(QIcon("./reload.png"))
        self.reloadBtn.setIconSize(QSize(32, 32))
        self.reloadBtn.setStyleSheet("background: transparent;")
        #self.reloadBtn.setFont(QFont('Verdana'))
        self.toolBar.addWidget(self.reloadBtn)

        self.address = QLineEdit(self)
        self.address.returnPressed.connect(self.load)
        self.address.setFont(QFont("Century Gothic", 16))
        self.address.setStyleSheet("color:white")
        self.toolBar.addWidget(self.address)

        self.searchBtn = QPushButton()
        self.searchBtn.clicked.connect(self.load)
        #self.searchBtn.setFont(QFont('Verdana'))
        self.searchBtn.setIcon(QIcon("./search.png"))
        self.searchBtn.setIconSize(QSize(32, 32))
        self.searchBtn.setStyleSheet("background: transparent;")
        self.toolBar.addWidget(self.searchBtn)

        self.historyBtn = QPushButton()
        self.historyBtn.clicked.connect(self.history)
        #self.historyBtn.setFont(QFont('Verdana'))
        self.historyBtn.setIcon(QIcon("./history.png"))
        self.historyBtn.setIconSize(QSize(32, 32))
        self.historyBtn.setStyleSheet("background: transparent;")
        self.toolBar.addWidget(self.historyBtn)





        self.webEngineView = QWebEngineView(self)
        self.setCentralWidget(self.webEngineView)

        self.webEngineView.page().urlChanged.connect(self.onLoadFinished)

        self.setGeometry(200, 200, 1000, 700)

        self.setWindowTitle('Python Web Server')
        self.setWindowIcon(QtGui.QIcon("./1.png"))
        self.show()

    def onLoadFinished(self):
        if self.webEngineView.history().canGoBack():
            self.backBtn.setEnabled(True)
        else:
            self.backBtn.setEnabled(False)

        if self.webEngineView.history().canGoForward():
            self.forBtn.setEnabled(True)
        else:
            self.forBtn.setEnabled(False)

    def load(self):

        url = QUrl.fromUserInput(self.address.text())
        sub_search = ['.com', '.in', '.net', '.edu', '.org', '.mil', '.gov']
        self.browser = QWebEngineView()
        for i in sub_search:
            if i in self.address.text():
                self.webEngineView.load(url)
                break

        else:
            url = self.address.text()
            input_text = str(url)
            self.webEngineView.load(QUrl('https://www.google.com/search?q=' + input_text))

    def back(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    def reload(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload)

    def history(self):
       print(self.QWebEngineHistory.items())



def main():

    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()