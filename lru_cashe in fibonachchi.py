from functools import lru_cache
#Bu funcsiya ortiqcha cashlarni tozalab dastur tez ishlashiga yordam beradi
@lru_cache
def fib(n):
    #print(f'Calculating {n}')
    return 1 if n in [1, 2] else fib(n-1)+fib(n-2)
a=fib(500)
print(a)
