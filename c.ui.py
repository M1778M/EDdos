# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c.ui.py.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from lib import c_setter as C

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(587, 474)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../icons/icons/Batch Black/terminal-2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../../icons/icons/Batch Black/terminal-2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(185, 191, 223);\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(23, 32, 30, 255), stop:0.369318 rgba(26, 48, 93, 130), stop:0.505682 rgba(28, 28, 0, 69), stop:0.670455 rgba(56, 0, 108, 130), stop:0.784091 rgba(105, 28, 122, 167), stop:0.909091 rgba(3, 3, 2, 145));")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.MainLayout = QtWidgets.QGridLayout()
        self.MainLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.MainLayout.setSpacing(0)
        self.MainLayout.setObjectName("MainLayout")
        self.FrameMain = QtWidgets.QFrame(self.centralwidget)
        self.FrameMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameMain.setObjectName("FrameMain")
        self.Label_PORT = QtWidgets.QLabel(self.FrameMain)
        self.Label_PORT.setGeometry(QtCore.QRect(30, 100, 71, 51))
        self.Label_PORT.setStyleSheet("background-color:none;")
        self.Label_PORT.setObjectName("Label_PORT")
        self.Label_URL = QtWidgets.QLabel(self.FrameMain)
        self.Label_URL.setGeometry(QtCore.QRect(30, 20, 71, 51))
        self.Label_URL.setStyleSheet("background-color:none;")
        self.Label_URL.setObjectName("Label_URL")
        self.Label_ATC_NUM = QtWidgets.QLabel(self.FrameMain)
        self.Label_ATC_NUM.setGeometry(QtCore.QRect(30, 170, 171, 51))
        self.Label_ATC_NUM.setStyleSheet("background-color:none;")
        self.Label_ATC_NUM.setObjectName("Label_ATC_NUM")
        self.GET_URL = QtWidgets.QLineEdit(self.FrameMain)
        self.GET_URL.setGeometry(QtCore.QRect(120, 19, 281, 51))
        self.GET_URL.setStyleSheet("border:1px solid black;\n"
"color:rgb(38, 202, 57);")
        self.GET_URL.setObjectName("GET_URL")
        self.GET_PORT = QtWidgets.QLineEdit(self.FrameMain)
        self.GET_PORT.setGeometry(QtCore.QRect(120, 100, 281, 51))
        self.GET_PORT.setStyleSheet("border:1px solid black;\n"
"color:rgb(38, 202, 57);")
        self.GET_PORT.setObjectName("GET_PORT")
        self.GET_ATCN = QtWidgets.QSpinBox(self.FrameMain)
        self.GET_ATCN.setGeometry(QtCore.QRect(230, 170, 171, 51))
        self.GET_ATCN.setStyleSheet("border:1px solid black;\n"
"color:rgb(38, 202, 57);")
        self.GET_ATCN.setWrapping(True)
        self.GET_ATCN.setAlignment(QtCore.Qt.AlignCenter)
        self.GET_ATCN.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.GET_ATCN.setMinimum(10)
        self.GET_ATCN.setMaximum(999999)
        self.GET_ATCN.setProperty("value", 100)
        self.GET_ATCN.setDisplayIntegerBase(10)
        self.GET_ATCN.setObjectName("GET_ATCN")
        self.attack_btn = QtWidgets.QPushButton(self.FrameMain)
        self.attack_btn.setGeometry(QtCore.QRect(30, 250, 211, 81))
        self.attack_btn.setStyleSheet("border:1px solid black;\n"
"color:rgba(0, 0, 0, 161);\n"
"font-size:20px;")
        self.attack_btn.setObjectName("attack_btn")
        self.log = QtWidgets.QTextBrowser(self.FrameMain)
        self.log.setGeometry(QtCore.QRect(280, 260, 251, 161))
        self.log.setStyleSheet("border:1px solid black;\n"
"color:rgb(0, 0, 0);\n"
"background-color: rgba(255, 232, 232, 50);")
        self.log.setObjectName("log")
        self.lablel_log = QtWidgets.QLabel(self.FrameMain)
        self.lablel_log.setGeometry(QtCore.QRect(280, 230, 91, 21))
        self.lablel_log.setStyleSheet("background-color:none;\n"
"")
        self.attack_btn.clicked.connect(self.auto_parse)
        self.lablel_log.setObjectName("lablel_log")
        self.MainLayout.addWidget(self.FrameMain, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.MainLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.attack_btn.clicked.connect(self.log.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def auto_parse(self):
        self.c_do_attack(self.GET_URL.text(),self.GET_PORT.text(),self.GET_ATCN.value())
    def check_url(self,url:str):
        return C.is_true_url(url)
    def check_port(self,port:str):
        return C.is_true_port(port)
    def c_do_attack(self,url:str,port:str,_range:int):
        if self.check_url(url) and self.check_port(port):
            for i in range(_range):
                self.log.append(f"Attack[{i}] "+C.REQUEST(url,int(port))+'<br/>')
            return True
        else:
            msgbox = QtWidgets.QMessageBox()
            msgbox.critical(QtWidgets.QWidget(),"In:Do_Attack","URL or Port Is Not Valid")
            return False
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Label_PORT.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">PORT:</span></p></body></html>"))
        self.Label_URL.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">URL:</span></p></body></html>"))
        self.Label_ATC_NUM.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">ATTACK NUMBERS:</span></p></body></html>"))
        self.GET_ATCN.setSpecialValueText(_translate("MainWindow", "100"))
        self.attack_btn.setText(_translate("MainWindow", "ATTACK"))
        self.log.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lablel_log.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">LOGs:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

