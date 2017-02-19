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
                             QApplication, QComboBox, QScrollArea)
from PyQt5.QtWidgets import QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QColor
import decrypt, define, json

#btc wallet
from blockcypher import list_wallet_names
from blockcypher import get_wallet_addresses
from blockcypher import get_address_overview
from blockcypher import get_address_details
from blockcypher import get_address_full
from blockcypher import get_transaction_details

blockcypher_key = "0b955a57f12548209b090dfc5a4c4a72"

class Balance(QWidget):
    
    def __init__(self):
        super().__init__()
        self.wallet_name = ""
        self.initUI()
        
    def initUI(self):
        #define widget
        self.importBtn = QPushButton("Create(Import) Wallet")
        self.walletName = QLabel('Wallet Name: ')
        self.WalletSelected = QComboBox(self)
        self.balanceLabel = QLabel('BTC Balance: ')
        self.balanceValue = QLabel('')

        #customize WalletSelected
        wallets = list_wallet_names(blockcypher_key)
        length = len(wallets['wallet_names'])
        if(length==0):
            self.WalletSelected.addItem("No Wallet")
            print("No Wallet")
        else:
            self.WalletSelected.addItems(wallets['wallet_names'])
        
        self.wallet_name = self.WalletSelected.currentText()

        #set balance
        self.setWalletBalance()

        self.historyLabel = QLabel('Transaction History: ')

        #add action
        self.importBtn.clicked.connect(self.importBtnPressed)
        self.WalletSelected.currentIndexChanged.connect(self.walletSelectedPressed)

        #init transaction history table 
        self.createHistoryTable()
        self.tx_details()

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
        self.historyTable.setRowCount(0)
        self.historyTable.setColumnCount(4)
        self.historyTable.setHorizontalHeaderLabels(("From", "To", "Balance", "Status"))

        #set width
        self.historyTable.resizeRowsToContents();
        self.historyTable.setSizeAdjustPolicy(QScrollArea.AdjustToContents);

        # self.historyTable.setColumnWidth(0, 170);
        # self.historyTable.setColumnWidth(1, 170);
        # self.historyTable.setColumnWidth(2, 100);
        # self.historyTable.setColumnWidth(3, 80);

    #create transaction history table : insert row dynamically
    def insertRow(self, fromAddress, toAddress, value, isConfirm):
        rowPosition = self.historyTable.rowCount()
        self.historyTable.insertRow(rowPosition)

        color = None
        if isConfirm == 'confirmed' :
            color = QColor(0,0,0)
        else :
            color = QColor(100,100,150)

        #set value
        self.historyTable.setItem(rowPosition, 0, QTableWidgetItem(fromAddress))
        self.historyTable.setItem(rowPosition, 1, QTableWidgetItem(toAddress))
        self.historyTable.setItem(rowPosition, 2, QTableWidgetItem(value))
        self.historyTable.setItem(rowPosition, 3, QTableWidgetItem(isConfirm))

        #alignment
        self.historyTable.item(rowPosition, 2).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.historyTable.item(rowPosition, 3).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        self.historyTable.move(0,0)

    def setWalletBalance(self):
        print("name: " , self.wallet_name)
        self.addresses = get_wallet_addresses(wallet_name=self.wallet_name, api_key=blockcypher_key, is_hd_wallet=True)
        address = self.addresses['chains'][0]['chain_addresses']
        if (len(address) == 0):
            self.balanceValue.setText('0.0000')
        else:
            amount = 0.0;
            for add in address:
                add_overview = get_address_overview(add["address"])
                print("overview: " , add_overview)
                balanceValue1 = add_overview["final_balance"]
                amount = amount + (float) (balanceValue1)

            self.balanceValue.setText(str(amount / 100000000))

    @pyqtSlot()
    def importBtnPressed(self):
        self.decrypt = decrypt.Decrypt()

    def walletSelectedPressed(self, i):
        self.wallet_name = self.WalletSelected.currentText()
        self.setWalletBalance()

    def tx_details(self):
        print("tx_details")
        addresses = self.addresses['chains'][0]['chain_addresses']
        for add in addresses:
            detail = get_address_details(add['address'])
            confirmed = detail['txrefs']
            unconfirmed = detail['unconfirmed_txrefs']

            #unconfirmed tx
            if len(unconfirmed) !=0:
                for tx in unconfirmed:
                    value = tx['value'] / 100000000
                    tx_hash = tx['tx_hash']
                    tx_detail = get_transaction_details(tx_hash)
                    self.insertRow(tx_detail['addresses'][1], add['address'], str(value), "unconfirmed")

            #confirmed tx
            if len(confirmed)!=0:
                for tx in confirmed:
                    value = tx['value'] / 100000000
                    tx_hash = tx['tx_hash']
                    tx_detail = get_transaction_details(tx_hash)
                    self.insertRow(tx_detail['addresses'][0], add['address'], str(value), "confirmed")
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Balance()
    sys.exit(app.exec_())
