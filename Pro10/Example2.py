import time
def fib_decorator(func):
    def inner():
        starttime=time.time()
        value=func()
        endtime = time.time()
        runtime = endtime-starttime
        print("time taken=",runtime)
        return value
    return inner

@fib_decorator
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f=fib()
n=int(input("Enter value for Number:"))
for i in range(n):
    print(next(f))
