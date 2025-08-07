#Dictionary {key:value}

def greet (name, nationality):
    print("Name is", name)
    print("From", nationality)

greet(nationality="India", name="John")    

#Kwargs profile

def employee (**kwargs):
    print(kwargs)
    # print("Name is", kwargs["name"])
    for key,value in kwargs.items():
        print("For Key",key,"The value is", value)

employee(name= "Jaylan", age=18, degree="Engineering")
employee(name= "Yusuf", country="Kenya", degree="Doctor")
