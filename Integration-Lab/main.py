def left(a, b, n):
  h = (b-a) / n
  int1 = 0.0
  for i in range(1, n):
    int1 += f(a+i*h)
  int1 *= h
  print(int1)

def right(a, b, n):
  h = (b-a) / n
  int1 = 0.0
  for i in range(1, n+1):
    int1 += f(a+i*h)
  int1 *= h
  print(int1)

def f(x):
   return(3*x + 10)

left(0,10,2)
right(0,10,2)

def trap(a, b, n):
  h = (b-a) / n
  trap = (f(a) + f(b))/2.0
  for i in range(1, n):
    trap += f(a+i*h)
  print(h*trap)

trap(0,10,1)

import math

def f(x):
   return(math.exp(-3*x**2))

left(0,5,100)
left(0,5,1000)
right(0,5,100)
right(0,5,1000)
trap(0,5,100)
trap(0,5,1000)

def f(x):
  return(math.sin(x)/x)

left(0,5,100)
left(0,5,1000)
right(0,5,100)
right(0,5,1000)
#trap(0,5,100)
#trap(0,5,1000)