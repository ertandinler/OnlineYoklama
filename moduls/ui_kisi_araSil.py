# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kisi_araSil.ui'
#
# Created: Thu Oct  2 22:36:47 2014
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
        Form.resize(427, 357)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 351, 101))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_tc = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_tc.setFont(font)
        self.label_tc.setObjectName(_fromUtf8("label_tc"))
        self.verticalLayout.addWidget(self.label_tc)
        self.label_ad = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_ad.setFont(font)
        self.label_ad.setObjectName(_fromUtf8("label_ad"))
        self.verticalLayout.addWidget(self.label_ad)
        self.label_soyad = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_soyad.setFont(font)
        self.label_soyad.setObjectName(_fromUtf8("label_soyad"))
        self.verticalLayout.addWidget(self.label_soyad)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEdit_tc = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_tc.setObjectName(_fromUtf8("lineEdit_tc"))
        self.verticalLayout_2.addWidget(self.lineEdit_tc)
        self.lineEdit_ad = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_ad.setObjectName(_fromUtf8("lineEdit_ad"))
        self.verticalLayout_2.addWidget(self.lineEdit_ad)
        self.lineEdit_soyad = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_soyad.setObjectName(_fromUtf8("lineEdit_soyad"))
        self.verticalLayout_2.addWidget(self.lineEdit_soyad)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 130, 291, 111))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_Sad = QtGui.QLabel(self.layoutWidget1)
        self.label_Sad.setText(_fromUtf8(""))
        self.label_Sad.setObjectName(_fromUtf8("label_Sad"))
        self.verticalLayout_3.addWidget(self.label_Sad)
        self.label_Ssoyad = QtGui.QLabel(self.layoutWidget1)
        self.label_Ssoyad.setText(_fromUtf8(""))
        self.label_Ssoyad.setObjectName(_fromUtf8("label_Ssoyad"))
        self.verticalLayout_3.addWidget(self.label_Ssoyad)
        self.label_Stc = QtGui.QLabel(self.layoutWidget1)
        self.label_Stc.setText(_fromUtf8(""))
        self.label_Stc.setObjectName(_fromUtf8("label_Stc"))
        self.verticalLayout_3.addWidget(self.label_Stc)
        self.layoutWidget2 = QtGui.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(70, 280, 291, 51))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_ara = QtGui.QPushButton(self.layoutWidget2)
        self.pushButton_ara.setObjectName(_fromUtf8("pushButton_ara"))
        self.horizontalLayout_2.addWidget(self.pushButton_ara)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_sil = QtGui.QPushButton(self.layoutWidget2)
        self.pushButton_sil.setObjectName(_fromUtf8("pushButton_sil"))
        self.horizontalLayout_2.addWidget(self.pushButton_sil)
        self.label_tc.setBuddy(self.lineEdit_tc)
        self.label_ad.setBuddy(self.lineEdit_ad)
        self.label_soyad.setBuddy(self.lineEdit_soyad)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit_tc, self.lineEdit_ad)
        Form.setTabOrder(self.lineEdit_ad, self.lineEdit_soyad)
        Form.setTabOrder(self.lineEdit_soyad, self.pushButton_ara)
        Form.setTabOrder(self.pushButton_ara, self.pushButton_sil)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Kişi Sorgulama Ekranı", None))
        self.label_tc.setText(_translate("Form", "T.C. No", None))
        self.label_ad.setText(_translate("Form", "Adı        ", None))
        self.label_soyad.setText(_translate("Form", "Soyadı", None))
        self.pushButton_ara.setText(_translate("Form", "Kişi Ara", None))
        self.pushButton_sil.setText(_translate("Form", "Kişi Sil", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

