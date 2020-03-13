def mers(s,n):
  # This program prints out Mersenne primes
  # between 0 and 1
  # n = number of primes needed
  # s = seed
  k = 16807     #7^5
  j = 2147483647       #2^31-1
  for i in range(n):
    s = k * s % j
    x = s / j
    print(x)

mers(4, 10000)

def mersCheck(s,n):
  k = 16807     #7^5
  j = 2147483647       #2^31-1
  a = [1] * n
  count = 0
  for i in range(n):
    s = k * s % j
    x = s / j
    a[i] = x
    print(x)
  for i in range(1, n):
    if a[i] < a[i - 1]:
      count = count + 1
    else:
      count = count
  print("The random number generated is larger than the previous number", (count / n) * 100, "percent of the time")

mersCheck(4, 10000)

import random as rand

count = 0

def mersCheck2(s,n):
  #s is seed and n is number of samples
  rand.seed(4)
  a = [1] * n
  count = 0
  for i in range(n):
    x = rand.random()
    a[i] = x
    print(x)
  for i in range(1, n):
    if a[i] < a[i - 1]:
      count = count + 1
    else:
      count = count
  print("The random number generated is larger than the previous number", (count / n) * 100, "percent of the time")

mersCheck2(4, 10000)

def loaded(n):
  #n is number of samples(die rolls)
  count1 = 0; count2 = 0;count3 = 0; count4 = 0;count5 = 0;count6 = 0
  rand.seed(4)
  for i in range(n):
    x = rand.random()
    if x < .15:
      count1 = count1 + 1
    elif x < .35:
      count2 = count2 + 1
    elif x < .6:
      count3 = count3 + 1
    elif x < .75:
      count4 = count4 + 1
    elif x < .85:
      count5 = count5 + 1
    elif x < 1:
      count6 = count6 + 1
  print((count1 /n) * 100, "percent of the rolls were 1")
  print((count2 /n) * 100, "percent of the rolls were 2")
  print((count3 /n) * 100, "percent of the rolls were 3")
  print((count4 /n) * 100, "percent of the rolls were 4")
  print((count5 /n) * 100, "percent of the rolls were 5")
  print((count6 /n) * 100, "percent of the rolls were 6")

loaded(1500)

import math as m

def drunk(n):
  rand.seed(4)
  countT = 0
  for i in range(n):
    countN = 0; countS = 0;countE = 0; countW = 0
    for j in range(50):
      x = rand.random()
      if x < (1/6):
        countE = countE + 1
      elif x < ((1/6) + (1/4)):
        countN = countN + 1
      elif x < ((1/6) + (1/4) + (1/4)):
        countS = countS + 1
      elif x < 1:
        countW = countW + 1
    countHoriz = countE - countW
    countVert = countS - countN
    distance = m.sqrt(countHoriz**2 + countVert**2)
    if distance > 20:
      countT = countT + 1
      #print("The drunk is", distance, "from the origin, which is more than 20 units")
    else:
      countT = countT
      #print("The drunk is only", distance, "from the origin, which is not more than 20 units")
  print((countT / n)*100, "percent of the samples resulted in the drunk being more than 20 units from the origin")
drunk(100)
  