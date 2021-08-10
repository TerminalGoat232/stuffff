from PyQt5 import (QtCore, QtGui, QtWidgets)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout,
                            QPushButton)
import time as t

d= 0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(576, 332)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-120, -90, 1001, 721))
       
        
        self.centralwidget.setStyleSheet("QFrame{\n"
" background-color: rgb(30, 30, 30);\n"
" border-radius: 15px"
"}\n")


        self.lbl = QtWidgets.QLabel(self.centralwidget)
        self.lbl2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl.setGeometry(QtCore.QRect(100, 130, 351, 91))
        self.lbl.move(50,50)
        self.lbl2.move(220,50)
        self.lbl3.move(450,175)
        self.lbl.setText('Clicker')
        self.lbl2.setText('GAME')
        self.lbl3.setText('reUI')
        self.lbl.setFont(QtGui.QFont("Consolas", 28))
        self.lbl2.setFont(QtGui.QFont("Consolas", 38))
        self.lbl3.setFont(QtGui.QFont("Small Fonts", 35))
        self.lbl.setStyleSheet('QLabel{color: rgb(139,255,255);  }')
        self.lbl2.setStyleSheet('QLabel{color: rgb(112,80,241); margin:50px;background-color:chim}')
        self.lbl3.setStyleSheet('QLabel{color: rgb(162,120,241);background-color:None }')

        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(210, 370, 401, 21))
        self.progressBar.setMaximumSize(QtCore.QSize(661, 41))
        self.btn = QtWidgets.QPushButton('▶', self.frame)
        self.btn.setFont(QtGui.QFont("Consolas", 58))

        self.btn.setGeometry(QtCore.QRect(310,300,200,60))
        self.btn.setStyleSheet("QPushButton{\n"
            "background-color:rgb(30,30,30);\n"
            "color:rgb(195,155,255);\n"
           
            "border:none;\n"
            "outline:none;\n"

            "}")
        #self.btn.setStyleSheet("background-image:url(ccccc.png);")

        self.progressBar.setStyleSheet("QProgressBar{\n"
"border-style:none;\n"
"border-radius: 5px;\n"
"color:rgb(79, 255, 244);\n"
"text-align:center;\n"
"\n"
"background-color:rgb(64, 88, 151);\n"
"}\n"
"QProgressBar::chunk{\n"
"border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0.216, y1:0.6135, x2:1, y2:0.602, stop:0.176136 rgba(85, 58, 255, 255), stop:0.971591 rgba(134, 228, 255, 255))\n"
"}")
        self.btn.clicked.connect(self.progressThing)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("chim", "chim"))
    def progressThing(self): 
        for x in range(101):
            t.sleep(0.05)
            self.progressBar.setValue(x)
            if x >=100:
                self.MainApp()
                self.frame.close()
                self.centralwidget.close()
                sys.exit()
                
################################################################################################################### MAIN ##############################################################
    def MainApp(self):
        import os
        direct = os.path.join(os.environ['USERPROFILE'],'Desktop','0000', 'ClickerGame.py')

       
        os.startfile(direct)
        os.system(direct)

        import subprocess
        subprocess.Popen([direct])
        subprocess.call(direct)

        

           
        # }




import sys
app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())