# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kart_tanimla.ui'
#
# Created: Thu Oct  2 22:36:20 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(465, 395)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../yoklama/simgeler/kart_tanimla.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(1.0)
        self.label_uyari = QtGui.QLabel(Dialog)
        self.label_uyari.setGeometry(QtCore.QRect(10, 70, 441, 81))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_uyari.setFont(font)
        self.label_uyari.setAlignment(QtCore.Qt.AlignCenter)
        self.label_uyari.setObjectName(_fromUtf8("label_uyari"))
        self.label_kisi = QtGui.QLabel(Dialog)
        self.label_kisi.setGeometry(QtCore.QRect(10, 160, 441, 121))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_kisi.setFont(font)
        self.label_kisi.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kisi.setObjectName(_fromUtf8("label_kisi"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 421, 28))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_tcBul = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_tcBul.setFont(font)
        self.label_tcBul.setObjectName(_fromUtf8("label_tcBul"))
        self.horizontalLayout.addWidget(self.label_tcBul)
        self.lineEdit_tcBul = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_tcBul.setFont(font)
        self.lineEdit_tcBul.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_tcBul.setMaxLength(11)
        self.lineEdit_tcBul.setPlaceholderText(_fromUtf8(""))
        self.lineEdit_tcBul.setObjectName(_fromUtf8("lineEdit_tcBul"))
        self.horizontalLayout.addWidget(self.lineEdit_tcBul)
        self.pushButton_kisiBul = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_kisiBul.setObjectName(_fromUtf8("pushButton_kisiBul"))
        self.horizontalLayout.addWidget(self.pushButton_kisiBul)
        self.pushButton_kartTanimla = QtGui.QPushButton(Dialog)
        self.pushButton_kartTanimla.setGeometry(QtCore.QRect(190, 320, 121, 31))
        self.pushButton_kartTanimla.setObjectName(_fromUtf8("pushButton_kartTanimla"))
        self.pushButton_iptal = QtGui.QPushButton(Dialog)
        self.pushButton_iptal.setGeometry(QtCore.QRect(360, 320, 71, 31))
        self.pushButton_iptal.setObjectName(_fromUtf8("pushButton_iptal"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_iptal, QtCore.SIGNAL(_fromUtf8("released()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Kart Tanımlama Ekranı", None))
        self.label_uyari.setText(_translate("Dialog", "Kart tanımlamak istediğiniz kişiyi bulun", None))
        self.label_kisi.setText(_translate("Dialog", "Kartı okutun", None))
        self.label_tcBul.setText(_translate("Dialog", "Tc No : ", None))
        self.pushButton_kisiBul.setText(_translate("Dialog", "Kişi Bul", None))
        self.pushButton_kartTanimla.setText(_translate("Dialog", "Kart Tanımla", None))
        self.pushButton_iptal.setText(_translate("Dialog", "İptal", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

