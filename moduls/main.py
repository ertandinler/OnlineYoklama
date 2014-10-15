#!/usr/bin/python3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_yoklama import Ui_MainWindow
from ui_kisi_Ekle import Ui_Form
from ui_kisi_araSil import Ui_Form as KisiArasil
from ui_cihaz_test import Ui_CihazTest
from ui_kart_tanimla import Ui_Dialog
from seri_port import PortDinle, portSec
import sys
import sqlite3
from PyQt4.QtGui import QMessageBox
import serial
import serial.tools.list_ports

PORT = ''


class PortSecTest(QDialog, Ui_CihazTest):
    """This an device test"""

    def __init__ (self):
        super(PortSecTest, self).__init__ ()
        self.setupUi(self)
        ports = list(serial.tools.list_ports.comports ())
        for port in ports:
            p = port[0]

            self.comboBox_cihaz.addItem("{}".format (p))

    @pyqtSignature ("bool")
    def cihaz_test (self):
        prt = str(self.comboBox_cihaz.currentText ())
        global PORT
        if len(ptr) == 0:
            self.label_cihaz.setText ("Cihaz bağlı değil\nBaglayıp yeniden deneyin")
        if len(prt) == 4:
            ser = serial.Serial ()
            ser.port = prt
            ser.open()
            al = ser.read (12)
            veri = int(al[1:9].decode('utf-8'), 16)
            if ser.isOpen() and len(al) == 12:
                self.label_cihaz.setStyleSheet ("background: #9fc;\n" "color : #090;\n" "border-radius : 10px;")
                self.label_cihaz.setText ("Bağlantı başarılı: {} \n {} portuna bağlandınız ".format (veri, prt))
                PORT = prt
                ser.close ()


class KisiEkle (QWidget, Ui_Form):
    """This persons adding to database"""

    def __init__(self):
        super(KisiEkle, self).__init__ ()
        self.setupUi(self)

    @pyqtSignature("bool")
    def Kaydet(self):
        self.ad = str(self.lineEdit_ad.text())
        self.soyad = str(self.lineEdit_soyad.text())
        self.tc = str(self.lineEdit_tc.text())

        if self.ad.startswith("i"):
            self.ad = "İ" + ad[1:]
            self.ad = ad.title()
        else:
            self.ad = ad.title()
        if soyad.startswith("i"):
            self.soyad = "İ" + self.soyad[1:]
            self.soyad = self.soyad.title()
        else:
            self.soyad = self.soyad.title()
        if len(self.ad) == 0 or len(self.soyad) == 0 or len (self.tc) == 0:
            QMessageBox.Warning(self, "Hata", u"Lütfen Tüm Alanları Doldurunuz!", "Kapat")
        elif len(tc) != 11:
            QMessageBox.Warning(self, "Hata", u"Lütfen Tc no kısmına 11 haneli Tc kimlik numaranızı giriniz!", "Kapat")
        else:
            db=sqlite3.connect("..//database\\yoklama.db")
            imlec=db.cursor()
            imlec.execute("""SELECT k.tc FROM  kisiler AS k WHERE tc= '{}' """.format(self.tc))
            t = imlec.fetchall()
            self.m = ''
            for a in t:
                self.m = a[0]
            if self.m == tc:
                QMessageBox.Warning(self, "Hata", u"{} TC nolu kişi sistemde kayıtlıdır1.".format(self.tc), "Kapat")
            else:
                imlec.execute(""" INSERT INTO kisiler(tc,ad,soyad) VALUES('{}', '{}', '{}')""".format(self.tc, self.ad,self.soyad))
                db.commit()
                db.close()
                QMessageBox.Warning(self, "İşlem Tamam", u"Kişi kaydı yapılmıştır", "Kapat")
                self.lineEdit_ad.setText("")
                self.lineEdit_soyad.setText("")
                self.lineEdit_tc.setText("")


class KisiAraSil (QWidget, KisiArasil):
    """This is delete persons of database"""

    def __init__(self):
        super(KisiAraSil, self).__init__()
        self.setupUi(self)

    @pyqtSignature("bool")
    def kisi_ara(self):
        if self.ad.startswith("i"):
            self.ad="İ" + ad [1:]
            self.ad=ad.title()
        else:
            self.ad=ad.title()
        if soyad.startswith("i"):
            self.soyad = "İ" + self.soyad [1:]
            self.soyad = self.soyad.title()
        else:
            self.soyad=self.soyad.title()
            db=sqlite3.connect("..//database\\yoklama.db")
            imlec=db.cursor()
            imlec.execute ("" "SELECT k.ad, k.soyad, k.tc FROM kisiler AS k WHERE ad LIKE '%{}%' AND soyad LIKE '%{}%' AND tc LIKE '%{}%' """.format (self.ad, self.soyad, self.tc))
            self.veriler=imlec.fetchall()
            db.close ()

        if len(self.veriler) > 1:
            self.label_Ssoyad.setText ("Aradığınız kriterde kayıtlı\nkullanıcı bulunamadı")
        for m in self.veriler:
            self.ad_ = m[0]
            self.soyad_= m[1]
            self.tc_= m[2]
        if len(self.veriler) == 1:
            self.label_Sad.setText("<br>İsim:</br>\t\t{}".format (self.ad_))
            self.label_Sad.setStyleSheet ("""background : red; color : blue; text-indent: 50px;	border-radius: 8px;border-width: 2px;border-style: solid;border-color: rgb(0, 0, 255);""")
            self.label_Ssoyad.setText("<br>Soyad: </br>\t{}".format(self.soyad_))
            self.label_Stc.setText("<br>T.C. No: </br>\t{}".format(self.tc_))

    @pyqtSignature("bool")
    def kisi_sil(self):
        """

        :type self: object
        """
        if len(self.veriler) == 1:
            uyari = QMessageBox.Question (self, "Uyarı", u"Silmek istedğinize emin misiniz?", QMessageBox.Yes | QMessageBox.No)
            if uyari == QMessageBox.Yes:
                db=sqlite3.connect("..//database\\yoklama.db")
                imlec=db.cursor()
                imlec.execute(
                    """ DELETE FROM kisiler WHERE ad='{}' AND soyad='{}' AND tc='{}'""".format (self.ad_, self.soyad_, self.tc_))
                db.commit()
                db.close()
                self.label_Ssoyad.setText("Silme işlemi başarılı bir şekilde uygulandı")
            else:
                self.label_Ssoyad.setText("Silme işlemi hatay uğradı")


class KartTanimla(QDialog, Ui_Dialog):


    def __init__(self):
        super(KartTanimla, self).__init__ ()
        self.setupUi(self)
        self.pd=PortDinle(PORT)
        self.pd.calistir = True
        self.pd.start()

    @pyqtSignature("bool")
    def kisi_bul(self):
        self.tc=str(self.lineEdit_tcBul.text ())
        self.kid_ = ""
        self.tc_ = ""
        self.ad_ = ""
        self.soyad_ = ""
        db=sqlite3.connect("..//database\\yoklama.db")
        imlec=db.cursor()
        imlec.execute("""SELECT * FROM kisiler WHERE tc='{}'""".format (self.tc))
        self.veriler = imlec.fetchall()

        if len (self.veriler) == 0:
            self.label_kisi.setText ("Kişi bulunamadı")
        for m in self.veriler:
            self.kid_= m[ 0 ]
            self.tc_= m[ 1 ]
            self.ad_= m[ 2 ]
            self.soyad_= m [ 3 ]
            self.label_kisi.setText ("Ad\t:{}\nTc\t:{}".format (self.ad_, self.soyad_, self.tc_))
        db.close()

    @pyqtSignature ("bool")
    def kart_format(self):
        global PORT
        if PORT == '':
            QMessageBox.Warning(self, "Uyarı", u"Lütfen önce vihazı Test edin", "Kapat")
            self.pd.calistir = False
            self.close()
        else:
            QMessageBox.Warning(self, "Uyarı", u"Lütfen okuyucuta kartı okutun", "Kapat")
            self.label_uyari.setText("{}".format (self.pd.text_veri))

            self.okunan_veri = self.pd.veri
            self.text_veri = self.str (okunan_veri)
            db = sqlite3.connect("..//database\\yoklama.db")
            imlec = db.cursor()
            imlec.execute("""INSER INTO kartlar (kart_no, kid) VALUES ('{}', '{}')""".format (self.okunan_veri, self.kid_))
            db.commit()
            db.close()
            self.pd.calistir=False


class AnaProgram (QMainWindow, Ui_MainWindow):


    def __init__ (self):
        super(AnaProgram, self).__init__()
        self.setupUi(self)
        self.statusBar().showMessage("Program hazır\n")
        self.port_SecTest = PortSecTest()

    @pyqtSignature("bool")
    def baglan(self):
        sys.exit()

    @pyqtSignature("bool")
    def iptal(self):
        sys.exit()

    @pyqtSignature("bool")
    def on_actioncikis_triggered(self):
        sys.exit()

    @pyqtSignature("bool")
    def on_actionYeni_Kisi_Ekle_triggered(self):
        self.kisi_Ekle = KisiEkle()
        self.kisi_Ekle.show()

    @pyqtSignature("bool")
    def on_actionKisi_Ara_triggered (self):
        self.kisi_araSil = KisiAraSil()
        self.kisi_araSil.show()

    @pyqtSignature("bool")
    def on_actionKisi_Sil_tiggered (self):
        self.kisi_araSil = KisiAraSil()
        self.kisi_araSil.show()

    @pyqtSignature("bool")
    def on_actionCihaz_Test_triggered (self):
        self.port_SecTest.show()

    @pyqtSignature("bool")
    def on_actionCihaz_Test_2_triggered (self):
        self.port_SecTest.show()


def main():
    app = QApplication(sys.argv)
    win = AnaProgram()
    win.show()
    return app.exec_()


if __name__ == '__main__':
    main()
#Son
