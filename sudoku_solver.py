#!/usr/bin/env python
#-*- coding: utf-8 -*-

import subprocess
import sys, os
import re, time
from encoder import *
from decoder import *

def main():
    if (len(sys.argv) == 1 or len(sys.argv) >=2):
      print "execute: sudoku_solver <sudoku_instances_file>"
      exit(1)
 
    entrada= [9*[0] for x in range(9) ]
    outfd = open('archivo_out', 'w')
    errfd = open('archivo_err', 'w')
    
    filename = sys.argv[1]

    instance = open(filename,'r')

    output_file = open("archivo_solucion","w")
    
    time_ = 0.0
    game = 0
 
    for sudoku in instance:
      game = game + 1
      print "Juego #" + str(game)
      for i in range(81):
          entrada[i/9][i%9]=sudoku[i]
      encoder(entrada)
     
      start = time.time()
      subprocess.call(["./minisat/minisat","archivo_rest.cnf","-no-luby","-rinc=1.5","-phase-saving=0","-rnd-freq=0.02","archivo_sol"],stdout=outfd, stderr=errfd)
      end = time.time()
      time_ = (end - start) + time_
                    
      try:
        # Se intenta abrir y cerrar el archivo solo para verificar que se ha conseguido una solucion al sudoku
        o = open("archivo_sol","r")
        o.close()
      except:
        print "No se consiguio solucion para esta instancia del juego."
        print sudoku
        continue
 
      variables = read_sol_file("archivo_sol")
      decoder(variables,output_file)

    print "Tiempo promedio de resolucion: " + str(time_/game)
    os.remove('archivo_sol')

    outfd.close()
    errfd.close()
    instance.close()
    output_file.close()
    os.remove('archivo_err')
    os.remove('archivo_out')    
    os.remove('archivo_rest.cnf')

main()
