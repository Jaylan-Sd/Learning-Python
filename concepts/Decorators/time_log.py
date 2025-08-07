#How long a function gets executed

import time

def time_fn(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        fn(*args,**kwargs)
        end_time = time.time()
        diff = end_time - start_time
        print("Time taken to run", diff)
    return wrapper

@time_fn
def counter():
    for n in range (0,100000):
        print(n)

counter()        

@time_fn
def counter2():
    for n in range (0,10000):
        print(n)

counter2()        

@time_fn
def sum(*args):
    ans=0
    for n in args:
        print(f"{ans}+ {n} = {ans}")
        ans = ans + n

        print("Ans is", ans)
    return ans

sum(100,200,300,400,500,600,700,800,900,1000)        

        

        