import math as m

def quadRoot(a, b, c):
  if a == 0 and b == 0:
    if c==0:
      print("y = 0 everywhere")
      return
    else:
      print("there is no solution")
      return
  elif a == 0:
    print("the solution is", -c/b)
    return
  discr = (b * b) - (4.0 * a * c)
  if discr < 0:
    print("No real numbers")
    return
  elif b > 0:
    x = -b - m.sqrt(discr)
    print("the solutions are", x/(2*a), "and",(2*c)/x)
    return
  else:
    y = -b + m.sqrt(discr)
    print("the solutions are", y/(2*a), "and", (2*c)/y)

quadRoot(0,0,0)
quadRoot(0,0,5)
quadRoot(0,4,4)
quadRoot(-2,-2,-2)
quadRoot(1,4,3)

def bisection(a,b,n,eps):
  fa = f(a)
  fb = f(b)
  if fa*fb > 0:
    print("no root between a and b")
    return
  error = b - a
  count = 0
  for i in range(1, n+1):
    error = error/2
    m = a + error
    count += 1
    fm = f(m)
    if abs(error) < eps or abs(fm) < eps:
      print("solution found", m, "in", count, "steps with an error of", error)
      return
    elif fa*fm > 0:
      a = m
      fa = fm
    else:
      b = m
      fb = fm

def f(x):
  return(x**3 * m.cos(x))

bisection(1, 2, 50, 10 ** -10)

def f(x):
  return(m.exp(-.01*x) * m.sin(0.2*x))
  
bisection(1, 6, 50, 10 ** -10)

def f(x):
  return(x**10 - 8*x**3 + 2*x -.25)

bisection(-1, 1, 50, 10 ** -10)