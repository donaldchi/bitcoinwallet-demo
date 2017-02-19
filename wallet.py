#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
   BTC Wallet Sample
   BTC Wallet Main class
   Created by chi on 2/16/2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from balance import Balance
from send import Send
from receive import Receive
# import balance, receive, send
 
class Wallet(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = 'BTC Wallet'
        self.left = 400
        self.top = 200
        self.width = 800
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.mainWindow = MainWindow(self)
        self.setCentralWidget(self.mainWindow)
 
        self.show()
 
class MainWindow(QWidget):        
 
    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.balanceTab = QWidget()   
        self.sendTab = QWidget()
        self.receiveTab = QWidget()
        self.tabs.resize(800,600) 
 
        # Add tabs
        self.tabs.addTab(self.balanceTab, "Balance")
        self.tabs.addTab(self.sendTab, "Send")
        self.tabs.addTab(self.receiveTab, "Receive")
 
        # create balance tab
        self.balanceTab.layout = QVBoxLayout(self)
        self.balance = Balance()
        self.balanceTab.layout.addWidget(self.balance)
        self.balanceTab.setLayout(self.balanceTab.layout)

        #create send tab
        self.sendTab.layout = QVBoxLayout(self)
        self.send = Send()
        self.sendTab.layout.addWidget(self.send)
        self.sendTab.setLayout(self.sendTab.layout)

        #create receive tab
        self.receiveTab.layout = QVBoxLayout(self)
        self.receive = Receive()
        self.receiveTab.layout.addWidget(self.receive)
        self.receiveTab.setLayout(self.receiveTab.layout)
 
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
 
    @pyqtSlot()
    def importBtnPressed(self):
        print("\n")
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Wallet()
    sys.exit(app.exec_())