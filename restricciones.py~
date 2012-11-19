#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Hecho Por:
# Isaac López Procopio
# 07-41120
# Juan V. Rosas
# 07-41502
# Hancel L. Gonzalez
# Bla

from constantes import *


def rest_a(celda):
    salida = "\""
    for i in range(9):
        salida +=  str((celda * 9) + 1 + i) + " " 
    return salida + "0\""
    
def rest_b(celda):
    salida = "\""
    for i in range(9):
        for j in range(i + 1, 9):
            salida += str(-((celda * 9) + 1 + i)) + " " + str(-((celda * 9) + 1 + j)) + " 0 \\n\\\n"
        #salida += "\n"
    return salida + "\""
    
print "REST_B = [ "
for i in range(81):
    print rest_b(i) + ","
print "]"

print REST_B[0]
