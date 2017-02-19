#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   BTC Wallet Sample
   Send class
   Created by chi on 2/17/2017
"""

import sys
from PyQt5.QtWidgets import (QLabel, QLineEdit, QGridLayout, QWidget, 
                             QApplication, QPushButton, QDesktopWidget, 
                             QTextEdit)

class Send(QWidget):

    def __init__(self, parent=None):
        super().__init__()

        #送金元アドレス
        address = "Enter BTC address"
        #送金先アドレス
        destination = "Enter BTC address"

        # self.fromaddress = QLineEdit()
        # self.fromaddress.setText(address)
        #self.fromaddress.setReadOnly(True)

        self.sendto = QLineEdit()
        self.sendto.setText(destination)
        #self.sendto.setReadOnly(True)

        self.transaction = QTextEdit()
        self.transaction.setReadOnly(True)

        sndTxBtn = QPushButton('Send', self)
        sndTxBtn.clicked.connect(self.createTx)

        grid = QGridLayout()
        grid.setSpacing(10)

        # grid.addWidget(QLabel('From'), 1,0)
        # grid.addWidget(self.fromaddress, 1,1)

        grid.addWidget(QLabel('Send to'), 2,0)
        grid.addWidget(self.sendto, 2,1)

        grid.addWidget(QLabel('Transaction'), 3,0)
        grid.addWidget(self.transaction, 3, 1, 1, 2)

        grid.addWidget(sndTxBtn, 4, 1)

        self.setLayout(grid)

        self.resize(320, 180)
        self.center()
        self.setWindowTitle('Create transaction demo')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def createTx(self):
        print("Send BTC!")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Transaction()
    sys.exit(app.exec_())

