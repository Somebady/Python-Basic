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

# Class variable exist even when the object is not created &
# it is a class variable so it is same for all objects.

# Class Method is called by both class & object of class, but it is standard or Geniune way to call
# Class method only with class name


# Access Specifier in python
