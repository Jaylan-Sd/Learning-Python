class User():

    def __init__(self,name,email,phone,password,user,discount = 0):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.discount = discount
        self.user = user
        self.is_locked = False
        

    def say_my_name(self):
        print (f"My name {self.name}")



    def print_details(self):
        print("----------------------------")
        print("Name", self.name)
        print("Email", self.email)
        print("Phone", self.phone)
        print("Password", self.password)
        print("Discount", self.discount)
        print("----------------------------")



    def login(self):

        if self.is_locked:
            print("Account already locked")
            return

        for i in range (0,3):
            password = input(f"Enter your password : Attempt {i}")
            if self.password==password:
                print ("Logged in succesfully")
                return

        self.is_locked = True        
        print ("Account is locked contact admin")


class Employee(User):

    def __init__(self, name, email, phone, password,salary):
        super().__init__( name=name, email=email, phone=phone, password=password, discount=10, user="employee")        
        self.salary = salary


class Customer(User):

    def __init__(self, name, email, phone, password):
        super().__init__(name=name, email=email, phone=phone, password=password, discount=0, user="customer")



emp1 = Employee(name="sam", email="samson@gmail,com", phone=8393893839, password=12344231 ,salary=20000)  

c1 = Customer(name="Jaylan", email="jaylan@gmail,com", phone=4784833839, password=87654321) 

emp1.say_my_name()
c1.say_my_name()

emp1.print_details()
c1.print_details()

emp1.login()