# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kisi_Ekle.ui'
#
# Created: Fri Oct  3 00:42:34 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(394, 204)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(32, 33, 331, 141))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_ad = QtGui.QLabel(self.layoutWidget)
        self.label_ad.setObjectName(_fromUtf8("label_ad"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_ad)
        self.lineEdit_ad = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_ad.setObjectName(_fromUtf8("lineEdit_ad"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_ad)
        self.label_soyad = QtGui.QLabel(self.layoutWidget)
        self.label_soyad.setObjectName(_fromUtf8("label_soyad"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_soyad)
        self.lineEdit_soyad = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_soyad.setObjectName(_fromUtf8("lineEdit_soyad"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_soyad)
        self.label_tc = QtGui.QLabel(self.layoutWidget)
        self.label_tc.setObjectName(_fromUtf8("label_tc"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_tc)
        self.lineEdit_tc = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_tc.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhHiddenText)
        self.lineEdit_tc.setObjectName(_fromUtf8("lineEdit_tc"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_tc)
        self.verticalLayout.addLayout(self.formLayout)
        self.pushButton_ekle = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_ekle.setObjectName(_fromUtf8("pushButton_ekle"))
        self.verticalLayout.addWidget(self.pushButton_ekle)
        self.label_ad.setBuddy(self.lineEdit_ad)
        self.label_soyad.setBuddy(self.lineEdit_soyad)
        self.label_tc.setBuddy(self.lineEdit_tc)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit_ad, self.lineEdit_soyad)
        Form.setTabOrder(self.lineEdit_soyad, self.lineEdit_tc)
        Form.setTabOrder(self.lineEdit_tc, self.pushButton_ekle)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Kişi Ekleme Sayfası", None))
        self.label_ad.setText(_translate("Form", "Adı       :", None))
        self.label_soyad.setText(_translate("Form", "Soyadı :", None))
        self.label_tc.setText(_translate("Form", "T.C No :", None))
        self.pushButton_ekle.setText(_translate("Form", "Ekle", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

