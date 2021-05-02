# OOPS in Python
class Car():

    # def __new__(self, doors, windows, engine):
    #     print('Class Object is called')

    def __init__(self, doors, windows, engine):
        self.__doors__ = doors
        self.windows = windows
        self.engine = engine
        print('Object Intialization is completed')

    def get_details(self):
        print(self.__doors__, self.windows, self.engine)


car1 = Car(4, 5, 'Electric')
print(type(car1))
car1.get_details()
print(car1.engine)
print(car1.__doors__)


# Magic Methods in classes
print(dir(car1))  # All default __fn__ is called magic or dunker fn..
print(car1.__sizeof__())


# Class Methods and Class Variables
class Bank_account():
    roi = '10%'  # Class variable

    def __init__(self, name, age, account_number):
        self.name = name
        self.age = age
        self.account_number = account_number

    @classmethod  # Class Method
    def revised_roi(cls, roi):
        cls.roi = roi


person1 = Bank_account('Akshay Soni', 24, 99261)

print(person1.name, person1.account_number)
print(person1.roi)

Bank_account.revised_roi('12%')
print(person1.roi)

print(Bank_account.roi)

person1.revised_roi('13%')
print(Bank_account.roi)

# person1.roi = '20%'
# print(person1.roi)

print(Bank_account.roi)

Bank_account.roi = '30%'
print(Bank_account.roi)

print(person1.roi)

person3 = Bank_account('Akshay', 24, '9999')
print(person3.roi)


# Class variable exist even when the object is not created &
# it is a class variable so it is same for all objects.

# Class Method is called by both class & object of class, but it is standard or Genuine way to call
# Class method only with class name


# Access Specifier in python
class Bank_account1():
    roi = '10%'  # Class variable

    def __init__(self, name, age, account_number, pin):
        self.name = name  # By default it is public variable
        self.age = age

        # making Protected Variable
        self._account_number = account_number  # Protected Variable

        # making Private Varaible
        self.__pin = pin

    @classmethod  # Class Method
    def revised_roi(cls, roi):
        cls.roi = roi


person4 = Bank_account1('Akshay Soni', 22, 9090, 123)
print(dir(person4))
print(person4._account_number)
print(person4._Bank_account1__pin)

person4._Bank_account1__pin = 456
person4._account_number = 8080
print(person4._account_number)
print(person4._Bank_account1__pin)

# Public -- It is accessible from all object of class
# Protected -- it should only be accessible from object of inherited class only
# Private -- it should never be directly accessible outside the class

# Imp--In Python, Access specifier is not strongly mapped as in Java & C++, Here everything is accessible, even private variable
# But as a sensible developer access specifier is indicate developer what is the accessibility of that variable
# and he should follow this, but there is no restriction is present here, All of this is just a indication
