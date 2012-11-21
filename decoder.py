import sys

def decoder(variables,file):
  sol = ""
  for j in range(81):
    offset = j * 9
    c = variables[offset : 9 + offset]
    i = [k for k in range(9) if int(c[k]) > 0][0] + 1
    sol = sol + str(i)
  file.write(sol + "\n")
  print ""
  pretty_print(sol)
  print ""
  print "" 

def pretty_print(solution):
  for i in range(9):
    print solution[i*9:i*9 + 9]

def read_sol_file(filename):
  file = open(filename,"r")

  variables = ""
  file.readline()
  variables = file.readline()
  
  variables = variables.split(" ")[:-1]

  file.close()
 
  return variables
