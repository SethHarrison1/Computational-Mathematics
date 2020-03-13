def add(x, y):
  return(x + y)

#raise x to power of y
def power(x, y):
  nx = x
  for i in range(1, y):
    x = x * nx
  print(x)


power(4, 3)

#lists

def fib(n):
  seq = [1 for i in range(n)][['']]
  for i in range(n - 2):
    seq[i+2] = seq[i + 1] + seq[i]
  print(seq[0])
  print(seq)

fib(10)

def Ax_mult(A,x):
  n = len(A)
  m = len(x)
  print(n,m)
  b= [0 for i in range(n)]
  for i in range(n):
    for j in range(m):
      b[i] += A[i][j] * x[j]
  print("Ax = ", b)
mat = [[1,2],[3,4], [5,6], [1,1]]
vec = [1,1]
Ax_mult(mat,vec)