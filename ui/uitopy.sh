#!/usr/bin/bash

pyuic4 -x /ui/cihaz_test.ui > ui/ui_cihaz_test.py
pyuic4 -x /ui/cihaz_test.ui > ui/ui_cihaz_test.py
pyuic4 -x /ui/cihaz_test.ui > ui/ui_cihaz_test.py
pyuic4 -x /ui/kisi_Ekle.ui > ui/ui_kisi_Ekle.py
pyuic4 -x /ui/yoklama.ui > ui/ui_yoklama.py

pyrcc4 /icons/icons.qrc > icons_rc.py
cp /icons/icons_rc.py /moduls/

#Created by Mehmet Nuri ÖZTÜRK mnozturk2@gmail.com
