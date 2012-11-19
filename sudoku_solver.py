#!usr/bin/env python
#-*- coding: utf-8 -*-

import subprocess
from restricciones import *

def main():
    entrada= [9*[0] for x in range(9) ]
    outfd = open('archivo_out', 'w')
    errfd = open('archivo_err', 'w')
    print entrada 
    files=open('entradas/sudoku_10k.txt','r')
    line=files.readline()
    # #while line!="":
    #     #print line
    for i in range(81):
        entrada[i/9][i%9]=line[i]
         #CALCULAR RESTRICCIONES
    agrega_rest(entrada)
    subprocess.call(["./walksat/walksat", "archivo_rest.cnf", "-out archivo_sol"], stdout=outfd, stderr=errfd)
    
#outfd.write(data)
    #outfd.close()
 #   outfd.close()
   # errfd.close()
    #     #SATSOLVER
    #     #DECODER
    # line=files.readline()

    print entrada

main()
