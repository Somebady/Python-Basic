# # OOPS in Python
# class Car():

#     # def __new__(self, doors, windows, engine):
#     #     print('Class Object is called')

#     def __init__(self, doors, windows, engine):
#         self.__doors__ = doors
#         self.windows = windows
#         self.engine = engine
#         print('Object Intialization is completed')

#     def get_details(self):
#         print(self.__doors__, self.windows, self.engine)


# car1 = Car(4, 5, 'Electric')
# print(type(car1))
# car1.get_details()
# print(car1.engine)
# print(car1.__doors__)


# # Magic Methods in classes
# print(dir(car1))  # All default __fn__ is called magic or dunker fn..
# print(car1.__sizeof__())


# # Class Methods and Class Variables
# class Bank_account():
#     roi = '10%'  # Class variable

#     def __init__(self, name, age, account_number):
#         self.name = name
#         self.age = age
#         self.account_number = account_number

#     @classmethod  # Class Method
#     def revised_roi(cls, roi):
#         cls.roi = roi


# person1 = Bank_account('Akshay Soni', 24, 99261)

# print(person1.name, person1.account_number)
# print(person1.roi)

# Bank_account.revised_roi('12%')
# print(person1.roi)

# print(Bank_account.roi)

# person1.revised_roi('13%')
# print(Bank_account.roi)

# # person1.roi = '20%'
# # print(person1.roi)

# print(Bank_account.roi)

# Bank_account.roi = '30%'
# print(Bank_account.roi)

# print(person1.roi)

# person3 = Bank_account('Akshay', 24, '9999')
# print(person3.roi)


# # Class variable exist even when the object is not created &
# # it is a class variable so it is same for all objects.

# # Class Method is called by both class & object of class, but it is standard or Genuine way to call
# # Class method only with class name


# # Access Specifier in python
# class Bank_account1():
#     roi = '10%'  # Class variable

#     def __init__(self, name, age, account_number, pin):
#         self.name = name  # By default it is public variable
#         self.age = age

#         # making Protected Variable
#         self._account_number = account_number  # Protected Variable

#         # making Private Varaible
#         self.__pin = pin

#     @classmethod  # Class Method
#     def revised_roi(cls, roi):
#         cls.roi = roi


# person4 = Bank_account1('Akshay Soni', 22, 9090, 123)
# print(dir(person4))
# print(person4._account_number)
# print(person4._Bank_account1__pin)

# person4._Bank_account1__pin = 456
# person4._account_number = 8080
# print(person4._account_number)
# print(person4._Bank_account1__pin)

# # Public -- It is accessible from all object of class
# # Protected -- it should only be accessible from object of inherited class only
# # Private -- it should never be directly accessible outside the class

# # Imp--In Python, Access specifier is not strongly mapped as in Java & C++, Here everything is accessible, even private variable
# # But as a sensible developer access specifier is indicate developer what is the accessibility of that variable
# # and he should follow this, but there is no restriction is present here, All of this is just a indication


# # Exception Handling
# a = 10
# b = 10
# try:
#     x = a+b
#     y = a/b
#     z = 22
# except ZeroDivisionError as e:
#     print('Can not divide by Zero')
# except NameError as e:
#     print('Variable is not define', e)
# except Exception as e:
#     print('Exception', e)
# else:
#     # Else block will execute only when there was no exception genrate in the try block
#     print(x)
#     print(y)
#     print(z)
# finally:
#     print('Execution is done')
#     # Finally will execute always, either code raise exception or not
#     # Practice use of finally is when you open connection to database, but later on code raise exception so in finally block you will be able to
#     # to close the database connection


# # Custom Exceptions
# # Defining Custom Exception
# class MyException(Exception):
#     pass


# try:
#     age = int(input())
#     if age > 20:
#         print('valid')
#     else:
#         raise MyException  # raise my custom exception
# except MyException as e:
#     print('Not Eligible to Apply')

# try:
#     age = int(input())
#     if age > 20:
#         print('valid')
#     else:
#         raise Exception
# except Exception as e:
#     print('Not Eligble to Apply', e)

# try:
#     age = int(input())
#     assert age > 20
#     print('valid')
# except AssertionError as e:
#     print('Not Eligble to Apply')


# Inheritance

import collections
import types
import keyword


class Emp():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Emp_Acc_info(Emp):
    def __init__(self, name, age, salary, account):
        super().__init__(name, age)  # Super is used to call fn of parent class
        self.salary = salary
        self.account = account


e1 = Emp('Akshay', 24)
print(e1.name, e1.age)
e2 = Emp_Acc_info('Akshay Soni', 27, 6000, 12837)
print(e2.name, e2.age, e2.salary, e2.account)


class A():
    def __init__(self):
        pass

    def assign(self, name):
        print(f'A:{name}')


class B(A):
    def __init__(self):
        pass

    def assign(self, name):
        print(f'B:{name}')


class C(A):
    def __init__(self):
        pass

    def assign(self, name):
        print(f'C:{name}')


class D(B, C):
    def __init__(self):
        pass

    def assign(self, name):
        print(f'D:{name}')
        super().assign(name)
        C.assign(self, name)
        A.assign(self, name)


d1 = D()
d1.assign('Akshay')


# Iterators & Genrators

list1 = [1, 2, 3, 4, 5, 8, 9, 0]
for i in list1:  # we are able to iterate the list,so list is an iteratble object
    print(i)

list2 = iter(list1)  # By using this iter() fn we create iterator object
print(type(list1))

#Iterator is also in iterable
for i in list1:
    print(i)

# another way to iterate iterator is using next() fn,
# Difference between iterator and iterable  is :
# 1. when we assign values to iterable object, all the values allocated at some memory location, so it stores in that memory location
# 2.but in iterator, values are not assigned to memory location untill it get called,
# 3. Iterator is more memory efficient , so when we have huge dataset then we use iterator instead of iterable object.

# Genrators


def square(x):
    for i in x:
        yield i*i
        yield i+i


x1 = square([5, 2, 3])
print(x1)
for i in x1:
    print(i)
# Difference Between Iterator & Generator
# 1. To create an iterator we use iter fn.
# 2. we create generator  we use fn along with yield keyword....
# 3. generator use yield keyword
# 4 generator in python helps us to write fast & compact Code
# 5.python iterator is much more memory efficient

print(issubclass(types.GeneratorType, collections.Iterator))

# Python Decorators & Closures
print('Python Decorators & Closures\n\n')


def welcome1():
    return 'welcome'


wel = welcome1()  # fn Copy

del welcome1
print(wel)

# Closures( fn inside a fn)
print("Closures\n")


def welcome():
    msg = 'WelcomeClass'

    def sub_welcome():
        print('welcome SubClass')
        print(msg)  # we use variable of parent fn here
    return sub_welcome()


welcome()
# Inner fn is able to access variables of parent fn


# Initial Decorators (instead of varaible we also use fn's)
print(" Initial Decorator's\n")


def welcome(func):  # pre-defined fn's
    msg = 'WelcomeClass'

    def sub_welcome():
        print('welcome SubClass')
        print(msg)  # we use variable of parent fn here
        func('Executing Passed Fn i.e fn')
    return sub_welcome()


welcome(print)
# Inner fn is able to access variables of parent fn

# Decorators (passing custom fn)
print("Decorator's\n")


def welcome(func):
    msg = 'WelcomeClass'

    def sub_welcome():
        print('welcome SubClass1')
        print(msg)  # we use variable of parent fn here
        func()
    return sub_welcome()


@welcome
def another_fn():
    print('Custom fn')


# Class Method & Static Method
class Hdfc():
    bank_id = 12345  # Class Varaible &  staticVariable--Both are same

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def revise_bank_id(cls, id):  # Class Method
        cls.bank_id = id

    @staticmethod
    def isadult(age):
        return age > 18  # it is used to create utility & static method is not able to change/modify variables of class


h1 = Hdfc('Akshay Soni', 23, 6000)
print(h1.name, h1.salary, h1.age, h1.bank_id)
Hdfc.revise_bank_id(98765)
print(h1.bank_id)
print(Hdfc.isadult(12))
print(h1.isadult(h1.age))


# Class variable or static variable same in python, both can be called with class name or object of that class
# class method is created using decorator @classmethod, while static method is created using @staticmethod
# Class method is able to change the variable of class, But static method won't be able to do that, we use static method as utility


# Self
self = 20
print(self)

print(keyword.kwlist)

x = frozenset({'a': 10, 'b': 20, 'b': 30})
for i in x:
    print(i, x)
