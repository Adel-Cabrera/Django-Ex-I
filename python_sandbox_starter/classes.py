# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User:

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def toString(self):
        return f'{self.name} {self.email} {self.age}'
    
class Customer(User):

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance=0

    def set_balance(self, balance):
        self.balance = balance
    



brad = User('brad', 'email@email.com', 23)
jhon = Customer('Jhon', 'email@email.com', 32)
jhon.set_balance(333)
print(jhon.balance)

print(brad.name)
print(brad.toString())
