import sys
import tokenize

def decoder(variables):
  sol = ""
  for j in range(81):
    offset = j * 9
    c = variables[offset : 9 + offset]
    i = [k for k in range(9) if int(c[k]) > 0][0] + 1
    sol = sol + str(i)
  print sol

def main():
  data = sys.argv[1]
  file = open(data,"r")
  
  variables = ""
  for line in file:
    line = line.strip("\n")
    variables = variables + line
  variables = variables.split(" ")[1:]
 
  decoder(variables)

main()
