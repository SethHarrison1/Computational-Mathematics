

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
  return(x**5 + x**3 + 3)

bisection(-10, 10, 100, 10**-10)

def secant(a, b, n , eps):
#a and b are your 2 endpoints
#n is the max number of steps to take
#eps is the largest error you want to allow
  fa = f(a)
  fb = f(b)
  count = 0
  for i in range(1, n+1):
    if abs(f(a)) > abs(f(b)):
      temp = a
      a = b
      b = temp
      temp = fa
      fa = fb
      fb = temp
    d = (b-a) / (fb - fa)
    d = d * fa
    b = a
    a = a - d
    fb = fa
    fa = f(a)
    count = count + 1
    if abs(d) < eps:
      print("solution found", a, "in", count, "steps with an error of", d)
      return


secant(-2, -.5, 100, 10**-10)