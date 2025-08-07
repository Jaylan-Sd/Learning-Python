import time
import platform

def logger (func):
    def wrapper (*args,**kwargs):
        start_time = time.time()
        func (*args,**kwargs)
        end_time = time.time()
        diff = end_time - start_time
        f_name = "logger.txt"
        txt = f"function:{func.__name__} time taken {diff} seconds"
        write_file(f_name=f_name, txt=txt)
    return wrapper    


def write_file (f_name, txt):
    with open (f_name,'a') as file:
        file.write (f"{txt} \n")

write_file (f_name="logger.txt", txt="Awesome work")        



@logger
def counter():
    for n in range (0,10000):
        print(n)

# counter()    

print()