#!/usr/bin/env python
__author__ = 'Xender'

# -------------------------------------------------------------------------------------------------------------------- #

import os
import re
import serial

# -------------------------------------------------------------------------------------------------------------------- #

# set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pong.settings")

# -------------------------------------------------------------------------------------------------------------------- #

from ping.models import Raspberry

# -------------------------------------------------------------------------------------------------------------------- #
try:
    ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
    ser.close()
    while 1:
        for a_polling in Raspberry.objects.all():

            try:
                print a_polling.label

            except:
                pass

            #Configuration de la connection serie
            ser.close()
            ser.open()

            # "S1P30C100V34"
            ligne_valide = re.compile(r'^(Z(?P<status>\d)P(?P<programme>\d+)C(?P<cadence>\d+)V(?P<vitesse>\d+)$)')

            while 1:
                response = ser.readline()
                #response = "Z1P22C88V77"
                #response = "None"
                res = ligne_valide.match(response)
                if res is None:
                        continue
                print res.group('status')
                print res.group('programme')
                print res.group('cadence')
                print res.group('vitesse')

                a_polling.status = res.group('status')
                a_polling.programme = res.group('programme')
                a_polling.cadence = res.group('cadence')
                a_polling.vitesse = res.group('vitesse')
                a_polling.save()

                break
except KeyboardInterrupt:
    print '\n' , 'Fin de l\'ecoute sur le port serial'
    ser.close()



# -------------------------------------------------------------------------------------------------------------------- #