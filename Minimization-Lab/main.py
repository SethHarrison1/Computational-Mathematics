import math as m
#a is left point, b is right point, eps is max error
def goldenSelection(a, b, eps):
  r = (-1.0 + m.sqrt(5.0)) / 2.0
  x = a + r * (b - a)
  y = b - r * (b - a)
  u = f(x)
  v = f(y)
  count = 0
  while abs(b - a) >= eps:
    count = count + 1
    if u > v:
      b = x
      x = y
      u = v
      y = b - (r * (b - a))
      v = f(y)
    elif u <= v:
      a = y
      y = x
      v = u
      x = a + (r * (b - a))
      u = f(x)
  print((a + b) / 2, "and", f((a + b)/ 2), "in", count, "iterations")

def f(t):
  return(m.exp(-t)*m.cos(t))

goldenSelection(0, m.pi, 10**-10)

def f(t):
  return(t**2 + 10*t**6 - 2 - 3 * t)

goldenSelection(-2, 2, 10**-10)

