#BigO notation

import time

def calculate_sum(n):
    
    sum = 0
    for num in range (1,n):
        print (f"Sum = {sum} ,  num = {num}")
        sum = sum + num

    return sum    


start_time = time.time()
calculate_sum (500000)
end_time = time.time()
diff = end_time - start_time
print (f"Speed {diff}")