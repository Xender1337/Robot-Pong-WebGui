
__author__ = 'Xender'

# -*- coding: utf-8 -*-
import serial
import re

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.open()

# Temp actuel : 25.1953125000.c
ligne_valide = re.compile(r'^(Temp\sactuel\s:\s)(?P<temperature>\d+\.\d+)(.{2})c(\s*)$')

try:
        while 1:
                response = ser.readline()
                res = ligne_valide.match(response)
                if res is None:
                        continue
                print res.group('temperature')
                break
except KeyboardInterrupt:
        ser.close()
