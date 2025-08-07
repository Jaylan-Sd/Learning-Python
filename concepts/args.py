#args --> arguments


def greet(*args):
    for arg in args:
        print("Name is", arg)

greet("John","Samuel","Kubai","Jaylan","Musa","Ali")
greet(123,True,False,None,[1,2,3])


def sum(*args):
    ans=0
    for n in args:
        print(f"{ans}+ {n} = {ans}")
        ans = ans + n

        print("Ans is", ans)
    return ans

sum(100,200,300,400,500,600,700,800,900,1000)        
