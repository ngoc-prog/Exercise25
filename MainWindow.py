# Form implementation generated from reading ui file 'D:\KTLT_NGUYENVONHUNGOC_EXERCISE\MODULE2\Exercise25\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 233)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.lineEditString = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditString.setGeometry(QtCore.QRect(20, 50, 471, 31))
        self.lineEditString.setText("")
        self.lineEditString.setObjectName("lineEditString")
        self.lineEditResult = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditResult.setGeometry(QtCore.QRect(20, 90, 471, 31))
        self.lineEditResult.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.lineEditResult.setObjectName("lineEditResult")
        self.pushButtonCheck = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonCheck.setGeometry(QtCore.QRect(30, 140, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonCheck.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\KTLT_NGUYENVONHUNGOC_EXERCISE\\MODULE2\\Exercise25\\image/299110_check_sign_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonCheck.setIcon(icon)
        self.pushButtonCheck.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonCheck.setObjectName("pushButtonCheck")
        self.pushButtonContinue = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonContinue.setGeometry(QtCore.QRect(170, 140, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonContinue.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\KTLT_NGUYENVONHUNGOC_EXERCISE\\MODULE2\\Exercise25\\image/3279059_continue_next_go on_keep on_move_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonContinue.setIcon(icon1)
        self.pushButtonContinue.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonContinue.setObjectName("pushButtonContinue")
        self.pushButtonExit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(360, 140, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonExit.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\KTLT_NGUYENVONHUNGOC_EXERCISE\\MODULE2\\Exercise25\\image/1790660_cancel_close_delete_discard_exit_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonExit.setIcon(icon2)
        self.pushButtonExit.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonExit.setObjectName("pushButtonExit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nguyễn Võ Như Ngọc"))
        self.label.setText(_translate("MainWindow", "Symmetric Strings"))
        self.lineEditString.setPlaceholderText(_translate("MainWindow", "Enter your string here"))
        self.pushButtonCheck.setText(_translate("MainWindow", "Check"))
        self.pushButtonContinue.setText(_translate("MainWindow", "Continue"))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit"))
