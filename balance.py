#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
   BTC Wallet Sample
   BTC Balance class
   Created by chi on 2/16/2017
"""

import sys
from PyQt5.QtWidgets import (QWidget,   QLabel, QLineEdit, 
                             QTextEdit, QGridLayout, 
                             QApplication)
from PyQt5.QtWidgets import QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
import decrypt, define, json

#btc wallet
from blockcypher import get_wallet_addresses
from blockcypher import get_address_overview

class Balance(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        #define widget
        self.importBtn = QPushButton("Create(Import) Wallet")
        self.walletName = QLabel('Wallet Name: ')
        self.WalletSelected = QLabel('testnet')
        self.balanceLabel = QLabel('BTC Balance: ')

        self.addresses = get_wallet_addresses(wallet_name='testnet', api_key="0b955a57f12548209b090dfc5a4c4a72", is_hd_wallet=True)
        address = self.addresses['chains'][0]['chain_addresses']
        if (len(address) == 0):
            self.balanceValue = QLabel('0.0000')
        else:
            print("not zero")
            amount = 0.0;
            for add in address:
                add_overview = get_address_overview(add["address"])
                print("overview: " , add_overview)
                balanceValue1 = add_overview["final_balance"]
                amount = amount + (float) (balanceValue1)

            self.balanceValue = QLabel(str(amount / 100000000))


        # data = json.loads(self.addresses)
        # print(data)
        self.historyLabel = QLabel('Transaction History: ')

        #add action
        self.importBtn.clicked.connect(self.importBtnPressed)

        #init transaction history table 
        self.createHistoryTable()

        #set layout
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.importBtn, 1, 0, 1, 2)
        grid.addWidget(self.walletName, 2, 0)
        grid.addWidget(self.WalletSelected, 2, 1)
        grid.addWidget(self.balanceLabel, 3, 0)
        grid.addWidget(self.balanceValue, 3, 1)
        grid.addWidget(self.historyLabel, 4, 0, 1, 2)
        grid.addWidget(self.historyTable, 5, 0, 1, 2)
        self.setLayout(grid) 
        
        #set main window
        self.setGeometry(400, 200, 800, 600)
        self.setWindowTitle('BTC Balance')    
        self.show()

    def createHistoryTable(self):
        self.historyTable = QTableWidget()
        self.historyTable.setRowCount(4)
        self.historyTable.setColumnCount(4)
        self.historyTable.setHorizontalHeaderLabels(("From", "To", "Balance", "Status"))

        self.historyTable.setColumnWidth(0, 170);
        self.historyTable.setColumnWidth(1, 170);
        self.historyTable.setColumnWidth(2, 100);
        self.historyTable.setColumnWidth(3, 80); 
        self.historyTable.setItem(0,0, QTableWidgetItem("Cell (1,1) Cell (1,1) Cell (1,1) Cell (1,1) Cell (1,1)"))
        self.historyTable.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.historyTable.setItem(0,2, QTableWidgetItem("Cell (1,3)"))
        self.historyTable.setItem(0,3, QTableWidgetItem("Cell (1,3)"))
        self.historyTable.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.historyTable.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.historyTable.setItem(1,2, QTableWidgetItem("Cell (2,3)"))
        self.historyTable.setItem(1,3, QTableWidgetItem("Cell (2,4)"))
        self.historyTable.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.historyTable.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.historyTable.setItem(2,2, QTableWidgetItem("Cell (3,3)"))
        self.historyTable.setItem(2,3, QTableWidgetItem("Cell (3,4)"))
        self.historyTable.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.historyTable.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.historyTable.setItem(3,2, QTableWidgetItem("Cell (4,3)"))
        self.historyTable.setItem(3,3, QTableWidgetItem("Cell (4,4)"))
        self.historyTable.move(0,0)

    @pyqtSlot()
    def importBtnPressed(self):
        self.decrypt = decrypt.Decrypt()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Balance()
    sys.exit(app.exec_())
