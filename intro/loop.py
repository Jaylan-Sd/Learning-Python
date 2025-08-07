#for, while, do_while

to_loop = True
k = 0

#while condition

while to_loop:
    if k > 10:
        to_loop = False
        print("k is", k)
    k = k+1

#for 

for k in range (2,10):
    print("For loop is", k)

#from 10 to 2    

for k in range (10,2,-2):
    print("for loop", k)
