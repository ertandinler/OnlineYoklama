# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cihaz_test.ui'
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

class Ui_CihazTest(object):
    def setupUi(self, CihazTest):
        CihazTest.setObjectName(_fromUtf8("CihazTest"))
        CihazTest.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/cihaz_test.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CihazTest.setWindowIcon(icon)
        self.groupBox_test = QtGui.QGroupBox(CihazTest)
        self.groupBox_test.setGeometry(QtCore.QRect(10, 190, 381, 101))
        self.groupBox_test.setObjectName(_fromUtf8("groupBox_test"))
        self.label_cihaz = QtGui.QLabel(self.groupBox_test)
        self.label_cihaz.setGeometry(QtCore.QRect(10, 30, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_cihaz.setFont(font)
        self.label_cihaz.setStyleSheet(_fromUtf8("background : #fcc;\n"
"color : red;\n"
"border-radius : 10px;"))
        self.label_cihaz.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_cihaz.setFrameShadow(QtGui.QFrame.Plain)
        self.label_cihaz.setTextFormat(QtCore.Qt.AutoText)
        self.label_cihaz.setMargin(9)
        self.label_cihaz.setIndent(0)
        self.label_cihaz.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_cihaz.setObjectName(_fromUtf8("label_cihaz"))
        self.pushButton_test = QtGui.QPushButton(self.groupBox_test)
        self.pushButton_test.setGeometry(QtCore.QRect(269, 40, 101, 31))
        self.pushButton_test.setObjectName(_fromUtf8("pushButton_test"))
        self.groupBox_comport = QtGui.QGroupBox(CihazTest)
        self.groupBox_comport.setGeometry(QtCore.QRect(10, 10, 381, 171))
        self.groupBox_comport.setStyleSheet(_fromUtf8(""))
        self.groupBox_comport.setObjectName(_fromUtf8("groupBox_comport"))
        self.comboBox_cihaz = QtGui.QComboBox(self.groupBox_comport)
        self.comboBox_cihaz.setGeometry(QtCore.QRect(10, 20, 231, 20))
        self.comboBox_cihaz.setObjectName(_fromUtf8("comboBox_cihaz"))
        self.buttonBox_cihaz = QtGui.QDialogButtonBox(self.groupBox_comport)
        self.buttonBox_cihaz.setGeometry(QtCore.QRect(270, 100, 101, 71))
        self.buttonBox_cihaz.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox_cihaz.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_cihaz.setObjectName(_fromUtf8("buttonBox_cihaz"))

        self.retranslateUi(CihazTest)
        QtCore.QObject.connect(self.buttonBox_cihaz, QtCore.SIGNAL(_fromUtf8("accepted()")), CihazTest.accept)
        QtCore.QObject.connect(self.buttonBox_cihaz, QtCore.SIGNAL(_fromUtf8("rejected()")), CihazTest.reject)
        QtCore.QMetaObject.connectSlotsByName(CihazTest)

    def retranslateUi(self, CihazTest):
        CihazTest.setWindowTitle(_translate("CihazTest", "Cihaz Bağlantı Penceresi", None))
        self.groupBox_test.setTitle(_translate("CihazTest", "Cihaz Testi", None))
        self.label_cihaz.setText(_translate("CihazTest", "Bağlantı yok.\n"
"Lütfen cihaza kart okutun ", None))
        self.pushButton_test.setText(_translate("CihazTest", "Test", None))
        self.groupBox_comport.setTitle(_translate("CihazTest", "Bağlantı Noktası Seçin", None))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CihazTest = QtGui.QDialog()
    ui = Ui_CihazTest()
    ui.setupUi(CihazTest)
    CihazTest.show()
    sys.exit(app.exec_())

