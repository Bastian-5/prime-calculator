import math

primes = [2]
wanted = 10000 #how many primes
x = 3 # number being checked if first prime not in list is unknown set to primes[len(primes)-1]+2

ratio = 1
leng = 1
split = 500




def primeCheck():

  for i in range(1,split):

    if x % primes[i] == 0 : return False

  for i in range(split,leng):
    
    pri = primes[i]

    if x % pri == 0 : return False

    if x < pri*pri : return True

    print(leng) #purely for fine tuning when the ratio change occures. second check is inefficient, so it should only occur once

  if ratio!=1 :
    print("length: "+(str)(leng))
    print("x: "+(str)(x))
  return True






while(leng < wanted):

  prime = True
  leng = len(primes)

  #changes % of prime list needed to check before switching to exit clause check
  if leng == 24 : ratio = 1/6
  elif leng == 240 : ratio = 1/20
  elif leng == 1800 : ratio = 1/60
  elif leng == 3120 : ratio = 1/80
  elif leng == 4700 : ratio = 1/100
  elif leng == 16400 :ratio = 1/200
  elif leng == 36400 : ratio = 1/300
  elif leng == 90000 : ratio = 1/500
  elif leng == 364000 : ratio = 1/1000

  split = math.floor(ratio*leng)

  prime = primeCheck()

  if prime : primes.append(x)
  x+=2

print(primes)