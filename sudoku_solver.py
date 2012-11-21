#!usr/bin/env python
#-*- coding: utf-8 -*-

import subprocess
import sys
from encoder import *
from decoder import *

def main():
    entrada= [9*[0] for x in range(9) ]
    outfd = open('archivo_out', 'w')
    errfd = open('archivo_err', 'w')
    
    filename = sys.argv[1]

    instance = open(filename,'r')

    output_file = "archivo_solucion"
    
    for sudoku in instance:
      for i in range(81):
          entrada[i/9][i%9]=sudoku[i]
      encoder(entrada)
      subprocess.call(["./walksat/walksat","-out","archivo_sol","archivo_rest.cnf"], stdout=outfd, stderr=errfd)
      variables = read_sol_file('archivo_sol')              
      decoder(variables)
   
    outfd.close()
    errfd.close()
    instance.close()
    output_file.close()

main()
