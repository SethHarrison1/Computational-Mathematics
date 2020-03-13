import math as m

def centralDeriv(x, n):
  h = 25
  for i in range(1, n+1):
    h = h/2
    y = (f(x+h) - f(x-h))/(2*h)
    print(i, h, y)

def f(x):
  return(m.sin(x))

centralDeriv(.5, 10)

def secDC(x, n):
  h = 25
  for i in range(1, n+1):
    h = h/2
    y = (f(x+2*h)-2*f(x) + f(x-2*h))/(4*h**2)
    print(i, h, y)

#secDC(.5, 10)