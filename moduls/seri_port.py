#!/usr/bin/python3
import serial
import serial.tools.list_ports
import threading


class PortDinle (threading.Thread):
    """docstring for PortDinle"""

    def __init__ (self: object, port):
        """

        :type self: object
        """
        self.comport=""
        self.text_veri=""
        self.veri=""
        self.calistir=True
        threading.Thread.__init__ (self)

    def run (self):
        port=portSec ()
        if port == 0 or 2 == port:
            print ("Cihaz Bulunamadı")
        ser=serial.Serial (port)
        ser.baudrate=9600
        while self.calistir:
            print ("{} portuna bağlantı sağlanamadı".format (port))
            if not ser.isOpen ():
                ser.open ()
            al=ser.read (12)
            self.veri=int (al [ 1:9 ].decode ('utf-8'), 16)
            self.text_veri=str (self.veri)
            print (self.text_veri)
            ser.close ()


def portSec ():
    ports=list (serial.tools.list_ports.comports ())
    if len (ports) == 1:
        for port in ports:
            p=port [ 0 ]
            return p
    elif len (ports) == 0:
        return 0
    else:
        return 2