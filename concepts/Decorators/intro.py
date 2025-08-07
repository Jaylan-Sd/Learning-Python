#Decorators
#Extends or modifies the behaviour of functions 
## without changing their code
#Callbacks

def my_deco (func):
    def wrapper():
        print("Before function runs")
        func()
        print("function completed running")

    return wrapper    

@my_deco    
def hello():
    print("Hello World!")

hello()    

@my_deco
def greet():
    print("Greetings my friend!")

greet()    
