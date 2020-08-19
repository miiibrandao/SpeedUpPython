import time

def verifica(n):
  if n == 1:
    return "Sim"
  else:
    return "Não"

def procedure2(n):
  EhPrimo = 1
  d=2
  if (n <= 1):
    EhPrimo = 0

  while (EhPrimo == 1 and d <= n / 2):
      resto = n % d
      if (resto == 0):
        EhPrimo = 0
      d = d + 1
  return EhPrimo
def procedure3(n):
  d=3
  if (n <= 1 or (n != 2 and n % 2 == 0)):
    EhPrimo = 0   
  else:
    EhPrimo = 1       

  while (EhPrimo and (d <= n / 2)):
    if (n % d == 0):
      EhPrimo = 0
    d = d + 2       
    
  return EhPrimo
def procedure4(n):  
  d=3
  if (n <= 1 or (n != 2 and n % 6 == 1 and n % 6 == 5)):
    EhPrimo = 0
  else:
    EhPrimo = 1
  while (EhPrimo  and d <= n / 2):
    if (n % d == 0):
      EhPrimo = 0
    d = d + 2
        
  return EhPrimo
def procedure1(n):
  EhPrimo = 1 
  d=2
  if n <= 1:
    EhPrimo = 0
  
  while EhPrimo == 1 and d <= n / 2 :
    if n % d  == 0:
      EhPrimo = 0
    d = d + 1
  return EhPrimo


# measure process time
numeros = [7,27,8421]

print("==========ALGORITMO 1===============")
soma = 0
for i in range(len(numeros)):
  for j in range (30):
    t0 = time.process_time_ns()
    primo = procedure1(numeros[i])   
    soma += t0
  
  print("Numero: ",numeros[i],"\nCiclos: ",soma/30, "\nPrimo?",verifica(primo)," \nseconds process time \n")
soma1 = soma

print("\n==========ALGORITMO 2===============")
soma = 0
for i in range(len(numeros)):
  for j in range (30):
    t0 = time.process_time_ns()
    primo = procedure2(numeros[i])   
    soma += t0
 
  print("Numero: ",numeros[i],"\nCiclos: ",soma/30, "\nPrimo?",verifica(primo)," \nseconds process 2 time \nSpeedUp: ", soma1/soma, "\n")

print("\n==========ALGORITMO 3================")
soma = 0
for i in range(len(numeros)):
  for j in range (30):
    t0 = time.process_time_ns()
    primo = procedure3(numeros[i])   
    soma += t0
  print("Numero: ",numeros[i],"\nCiclos: ",soma/30, "\nPrimo?",verifica(primo)," \nseconds process 2 time \nSpeedUp: ", soma1/soma,"\n")
print("\n==========ALGORITMO 4===============")
soma = 0
for i in range(len(numeros)):
  for j in range (30):
    t0 = time.process_time_ns()
    primo = procedure4(numeros[i])   
    soma += t0
  
  print("Numero: ",numeros[i],"\nCiclos: ",soma/30, "\nPrimo?",verifica(primo)," \nseconds process 2 time \nSpeedUp: ", soma1/soma,"\n")
