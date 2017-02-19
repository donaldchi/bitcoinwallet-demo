#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
   BTC Wallet Sample
   Receive class : create receive address
   Created by chi on 2/16/2017
"""

import sys
from PyQt5.QtWidgets import (QWidget,   QLabel, QLineEdit, 
                             QTextEdit, QGridLayout, 
                             QApplication)
from PyQt5.QtWidgets import QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPixmap
import decrypt, define, json

#btc wallet
from blockcypher import get_wallet_addresses
from blockcypher import get_address_overview
from blockcypher import derive_hd_address

#qrcode
import qrcode

blockcypher_key = "0b955a57f12548209b090dfc5a4c4a72"

class Receive(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        #define widget
        self.addressQRCode = QLabel("qrcode")
        self.addressLabel = QLabel("address")

        #customize address label and qrcode
        self.addressLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
        # self.addressLabel.setStyleSheet('background-color : white; color: black')
        self.addressLabel.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)


        #get avaliable address by tx times and show it as label/qrcode format
        self.initAddress()

        #set layout
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.addressLabel, 1, 0)
        grid.addWidget(self.addressQRCode, 1, 1)
        self.setLayout(grid) 
        
        #set main window
        self.setGeometry(400, 200, 800, 600)
        self.setWindowTitle('Receive')    
        self.show()  

    def initAddress(self):
        addresses = get_wallet_addresses(wallet_name='testnet', api_key=blockcypher_key, is_hd_wallet=True)
        address = addresses['chains'][0]['chain_addresses']
        if (len(address) == 0):
            self.balanceValue = QLabel('0.0000')
            address = deriveAddress()
            self.addressLabel.setText(address)
        else:
            amount = 0.0;
            for add in address:
                add_overview = get_address_overview(add["address"])
                tx_time = add_overview['final_n_tx']
                if tx_time == 0 :
                    self.addressLabel.setText(add_overview['address']) 
                    img = qrcode.make(add_overview['address']) 
                    img.save('qr_img.png') 
                    pixmap = QPixmap('qr_img.png')
                    self.addressQRCode.setPixmap(pixmap) 
                    break
            if  self.addressLabel.text() == "":
                address = self.deriveAddress()
                print(address)
                self.addressLabel.setText(address)
                img = qrcode.make(address)   
                img.save('qr_img.png') 
                pixmap = QPixmap('qr_img.png')
                self.addressQRCode.setPixmap(pixmap)


    def deriveAddress(self):
        address = derive_hd_address(api_key=blockcypher_key, wallet_name='testnet', coin_symbol='btc')
        return address['chains'][0]['chain_addresses'][0]['address']

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Receive()
    sys.exit(app.exec_())
