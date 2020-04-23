

def fibo(n):
   if n <= 1:
       return n
   else:
       return (fibo(n-1) + fibo(n-2))


def sumi(a, b):
    return a + b


def verify(n):
    d = {3:0, 4:0, 5:0}
    for i in range(1, n):
        if i % 3 == 0:
            d[3] = d[3] + 1
        if i % 4 == 0:
            d[4] = d[4] + 1
        if i % 5 == 0:
            d[5] = d[5] + 1
    return d
