#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Hecho Por:
# Isaac López Procopio
# 07-41120
# Juan V. Rosas
# 07-41502
# Hancel L. Gonzalez
# 07-40983

def fila(a):
    return a % 9
    
def columna(a):
    return a / 9
    
def cuadro_H(a):
    return fila(a) / 3
    
def cuadro_V(a):
    return columna(a) / 3
    
def mismo_cuadro(a, b, c):
    return a == cuadro_H(c) and b == cuadro_V(c)
    
    

def main():

    distintos = []
    for celda in range(81):
        actual = []
        celda_fila = fila(celda)
        celda_columna = columna(celda)
        celda_cuadro_H = cuadro_H(celda)
        celda_cuadro_V = cuadro_V(celda)
        for comparando in range (81):
            if celda != comparando and \
            (fila(comparando) == celda_fila or \
            columna(comparando) == celda_columna or \
            mismo_cuadro(celda_cuadro_H, celda_cuadro_V, comparando)) :
                actual = actual + [comparando]
        distintos = distintos + [actual]
    
    print distintos
#    for i in range(81):
#        print i , distintos[i]
    
main()
