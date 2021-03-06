#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Hecho Por:
# Isaac López Procopio
# 07-41120
# Juan V. Rosas
# 07-41502
# Hancel L. Gonzalez
# 07-40983

import os
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
    
def rest_c(celda):
    salida = "\""
    for comparacion in VECINOS[celda]:
        for numero in range(9):
            salida = salida + str(-((celda*9 + 1) + numero)) + " " + str(-((comparacion*9 + 1) + numero)) + " 0 \\n\\\n"
    return salida + "\""
            
def encoder(entrada):
    n_lines=0
    salida = open('archivo_rest', 'w')
    for i in range(9):
        for j in range(9):
            if entrada[i][j] == ".":
                salida.write(REST_A[i*9 + j] + "\n")
                salida.write(REST_B[i*9 + j])
                salida.write(REST_C[i*9 + j])
                n_lines+=217
            else:
                salida.write(str(((i*9 + j)*9 + int(entrada[i][j]))) + " 0\n")
                for comparacion in VECINOS[i*9 + j]:
                    salida.write(str(-((comparacion*9) + int(entrada[i][j]))) + " 0\n")
                n_lines+=21
    salida.close()

    salida = open('archivo_rest', 'r')
    imp = open('archivo_rest.cnf', 'w')

    imp.write("p cnf 729 "+str(n_lines) + "\n") 
    for l in salida.readlines():
        imp.write(l)
    
    salida.close()
    os.remove('archivo_rest')
    imp.close()
    print "Numero de Restricciones: " + str(n_lines)
