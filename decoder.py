import sys
import tokenize

def decoder(variables):
  for j in range(27):
    offset = j * 9
    c = variables[offset : 9 + offset]
    i = [k for k in range(9) if int(c[k]) > 0][0] + 1 

data = sys.argv[1]

file = open(data,"r")

variables = ""

for line in file:
  line = line.strip("\n")
  variables = variables + line

variables = variables.split(" ")[1:]

decoder(variables)
