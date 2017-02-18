#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
   BTC Wallet Sample
   Decrypt wallet class
   Created by chi on 2/16/2017
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLineEdit)
from PyQt5.QtCore import pyqtSlot

class Decrypt(QWidget):

    def __init__(self):
        super().__init__()
        self.passphrase = ""
        self.initUI()

    def initUI(self):
        self.passphraseEdit = QLineEdit();

        # OKボタンとCancelボタンの作成
        self.importBtn = QPushButton("Create(Import)")
        self.cancelBtn = QPushButton("Cancel")

        #add action
        self.importBtn.clicked.connect(self.importBtnPressed)
        self.cancelBtn.clicked.connect(self.cancelBtnPressed)

        # 水平なボックスを作成
        hbox = QHBoxLayout()
        # ボタンの大きさが変わらないようにする
        # ボタンの左側に水平方向に伸縮可能なスペースができるため、ボタンは右に寄る
        hbox.addStretch(1)
        hbox.addWidget(self.importBtn)
        hbox.addWidget(self.cancelBtn)

        # 垂直なボックスを作成
        vbox = QVBoxLayout()
        # 垂直方向に伸縮可能なスペースを作る
        vbox.addStretch(1)
        vbox.addWidget(self.passphraseEdit)
        # 右下にボタンが移る
        vbox.addLayout(hbox)

        # 画面に上で設定したレイアウトを加える
        self.setLayout(vbox)    

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Input passphrase of BTC Wallet')    
        self.show()

    @pyqtSlot()
    def importBtnPressed(self):
        self.passphrase = self.passphraseEdit.text()
        self.hide()
        print("passphrase: ", self.passphrase)

    def cancelBtnPressed(self):
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Decrypt()
    sys.exit(app.exec_())
