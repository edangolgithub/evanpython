x=lambda a,b,c: a+b+c
print(x(1,2,3))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
