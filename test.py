#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we select a file with a
QFileDialog and display its contents
in a QTextEdit.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QMainWindow, QGridLayout, QPushButton,
QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sys
import os

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        self.changeImgPath = QPushButton("Open Images Path", self)
        self.changeImgPath.resize(140, 30)
        self.changeImgPath.move(30, 30)
        self.changeImgPath.clicked.connect(self.changeImgPathFunc)
        
        self.changeSavePath = QPushButton("Change Save Path", self)
        self.changeSavePath.resize(140, 30)
        self.changeSavePath.move(30, 70)
        self.changeSavePath.clicked.connect(self.changeSavePathFunc)
        
        self.createRec = QPushButton("Create Rectangle", self)
        self.createRec.resize(140, 30)
        self.createRec.move(30, 110)
        
        self.setGeometry(300, 300, 1080, 720)
        self.setWindowTitle('LabelOCR')
        self.show()
    
    def changeImgPathFunc(self):
      self.ImgPath = str(QFileDialog.getExistingDirectory(self, 'Select images folder', './'))
      self.imgs = os.listdir(self.ImgPath)
      print(self.imgs)
      
    def changeSavePathFunc(self):
      self.SavePath = str(QFileDialog.getExistingDirectory(self, 'Select images folder', './'))
      print(self.SavePath)
        
        
     
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())