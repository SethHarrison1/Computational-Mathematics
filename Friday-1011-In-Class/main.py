def divisible(n):
  if n % 2 == 0:
    print(n, " is divisible by 2.")
  if n % 3 == 0:
    print(n, " is divisible by 3.")
  if n % 5 == 0:
    print(n, " is divisible by 5.")
  else:
    print(n, " is not divisible y 2, 3, or 5.")

divisible(15)

def add_half():
  t = 0
  while t != 3:
    t += 1/2
    print(t)

add_half()

def add_tenth():
  t = 0
  while t != 3:
    t += 1/10
    print(t)

#add_tenth()