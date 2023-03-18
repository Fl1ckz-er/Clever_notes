# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt5.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def review(self):
        title = self.listWidget.selectedItems()[0].text()
        with open(title+'.txt','r',encoding='utf-8')as file:
            self.plainTextEdit.setPlainText(file.read())
    def create(self):
        self.plainTextEdit.setPlainText('')
    def delete (self):
        if self.listWidget.selectedItems():
            title= self.listWidget.selectedItems()[0].text()
            os.remove(title+'.txt')
            self.plainTextEdit.setPlainText('')
            self.listWidget.selectedItems()[0].setHidden(True)
    def save(self):
        a = self.plainTextEdit.toPlainText()
        b = a.split("\n")[0]
        self.listWidget.addItem(b)
        print(b)
        with open(b + '.txt', 'w', encoding='utf-8') as file:
            file.write(a)
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1177, 904)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 40, 721, 781))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("color:rgb(85, 85, 255)")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(770, 60, 361, 231))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.clicked.connect(self.review)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(770, 300, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(0, 170, 0)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.create)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(960, 300, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 0, 0)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(770, 350, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 170, 0)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.save)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(780, 30, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(770, 390, 91, 31))
        self.label_2.setObjectName("label_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(770, 420, 361, 241))
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(770, 710, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:rgb(0, 170, 0)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(960, 710, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color:rgb(255, 0, 0)")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(770, 770, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color:rgb(170, 0, 255)")
        self.pushButton_6.setObjectName("pushButton_6")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(770, 670, 361, 31))
        self.textEdit.setStyleSheet("color:rgb(85, 85, 255)")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1177, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        dir = os.path.abspath(os.curdir)
        listfile = os.listdir(dir)
        for i in listfile:
            try:
                a = i.split('.')
                if a [1] == 'txt':
                    self.listWidget.addItem(a[0])
            except:
                pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        self.pushButton.setText(_translate("MainWindow", "Створити замітку"))
        self.pushButton_2.setText(_translate("MainWindow", "Видалити замітку"))
        self.pushButton_3.setText(_translate("MainWindow", "Зберегти замітку"))
        self.label.setText(_translate("MainWindow", "Список заміток"))
        self.label_2.setText(_translate("MainWindow", "Список тегів"))
        self.pushButton_4.setText(_translate("MainWindow", "Додати до замітки"))
        self.pushButton_5.setText(_translate("MainWindow", "Відкріпити від замітки"))
        self.pushButton_6.setText(_translate("MainWindow", "Шукати замітки по тегу"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Перший сніг</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
