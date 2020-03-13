def euler(a, b, x, n):
 h = (b-a)/n
 t=a
 print(t,x)
 for i in range(1, n+1):
   x = x + (h*f(t,x))
   t = a+(i*h)
 print(t,x)

def f(t, x):
  return(t * x + t**2 * x**2)

euler(2, 3, .5, 6)

def euler2(a,b,init,n):
  h = (b-a)/n
  t = a
  ans = init
  new_ans = init
  for i in range(1, n+1):
    for j in range(0, 2):
      new_ans[j] = ans[j] + h * g(j,t,ans)
    for j in range(0, 2):
      ans[j] = new_ans[j]
    t = a + i * h
  print(t, ans)

def g(j, t,ans):
  if j==0:
    return(ans[1])
  return(-ans[0])

euler2(0, 1,[-1, 2],1000)
euler2()