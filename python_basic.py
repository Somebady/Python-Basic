# List


# Set
"""[In Python, Set is an unordered collection of data type that is iterable,
mutable and has no duplicate elements.
The order of elements in a set is undefined though it may consist of various elements.
The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.]
    """
from datetime import datetime
import copy
from functools import reduce
s = {1, 2, 3, 4, 5, 6, 6}
print(s)

# to add
s.add(7)
print(s)
s.update([9, 10, 11])
print(s)
"""[Set items cannot be accessed by referring to an index,
since sets are unordered the items has no index.
But you can loop through the set items using a for loop,
or ask if a specified value is present in a set, by using the in keyword.]
    """
# for i in set:
#     print(i)
# set is unordered set of list, so indexing is not
# possible in set

# Removeing element from set
s.remove(6)
print(s)
s.discard(4)
print(s)
s.clear()
print(s)


# Dictionary
dict = {'key': 'value'}


# Lamba Function
"""it is an anonymous function who has no name, it is genrally used to convert fn who has only one single statement.
       """


def addition(x, y, z):
    return x+y+z


print(addition(1, 2, 3))
# add = lambda a, b, c, d: a+b+c+d


def add(a, b, c, d): return a+b+c+d


# even = lambda a: a % 2 == 0
def even(a): return a % 2 == 0
# i don't know, but my vs code converting lambda functions into definition of fn


print(even(12))

print(add(1, 2, 3, 4))

# Map Function in Python
"""map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
    """
lst = [1, 2, 44, 43, 33]
lst1 = [1, 2, 44, 43, 33]
lst2 = [1, 2, 44, 43, 33]
print(list(map(even, lst)))
print(list(map(lambda a, b, c: a*b*c, lst, lst1, lst2)))

# map(passing value to function present here one by one, Getting one by one values from here)
# in second place, we can also provide multiple list by comma seprated, one -one value will get fetched from all
# list and passed to the function


# Filter Function
print(list(filter(even, lst)))

# Filter and Map same, the difference between map & filter is mapped will give all value , filter will give only values which
# true, filtering the value as its name suggest

print(list(filter(lambda a: a % 2 == 0, lst)))
"""They both return a new array. map returns a new array of elements where you have applied some function on the element so that it changes the original element (typically). filter returns a new array of the elements of the original array (with no change to the original values). filter will only return elements where the function you specify returns a value of true for each element passed to the function.

So map returns the same number of elements as the original, but the element value will be transformed in some way and filter will return the same or less number of elements than the original but not change the original elements’ values.

The map() method creates a new array with the results of calling a provided function on every element in the calling array.

The filter() method creates a new array with all elements that pass the test implemented by the provided function.
    """

# Reduce
l1 = [3, 2, 1]
l2 = [2]
print('reduce')
print(type(lst))
# print(list(map(lambda a, b, c: a*b*c, lst, lst1, lst2)))
print(reduce(lambda a, b: a*b, l1))
print(reduce(lambda a, b: a*a, l2))

"""At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.
    """

# Questions
print("Leader Veloite Question")
arr = [16, 17, 4, 3, 5, 2]

x = set()
for i in range(0, len(arr)):
    x.add(reduce(lambda a, b: a if a > b else b, arr[i:]))
print(x)


print("Duplicate checking")

arr1 = [2, 3, 3, 3, 6, 9, 9]

# using list comprehension
x = []
[x.append(i) for i in arr1 if i not in x]
print(x)


# =,Shallow_Copy & Deep Copy
a = [1, 2, 3, 4]
b = a
print('Normal Assignment')
print('Original List', id(a))
print('Copy list', id(b))

c = a.copy()
print('Shallow copy')
print('Original List', id(a))
print('Copy List', id(c))

a = [[1, 2, 3, 4], [9, 8, 7, 6]]
d = a.copy()
print('Nested List Shallow Copy')
print('Original List', id(a))
print('Copy List', id(d))

print('Original Nested List', id(a[0]))
print('Copy Nested List', id(d[0]))


f = copy.deepcopy(a)
print('Deep_copy')
print('Original List', id(a))
print('Copy List', id(f))

print('Original Nested List', id(a[0]))
print('Copy Nested List', id(f[0]))


# Explanation DeepCopy & Shallow Copy
# # list --> address
# a--1000
# b = a
# b--1000
# This is normal Assignment

# # Shallow Copy
# a--1000
# b = a.copy()

# b--2000
# # Differect address is assigned here

# # Nested List
# a = [[1, 2, 3], [4, 5, 6]]
# a--1000
# a[0]---1010
# a[1]--1020

# b = a.copy()

# b---2000
# b[0]--1010
# b[1]--1020

# # List is assigned to different address in shallow copy but nested list stll
# # Referencing to the address point of original nested list


# # Deep Copy
# a---1000
# b = a.copy()
# b--2000

# # In single normal list, shallow copy and Deep copy is same

# # Nested list
# a--1000
# a[0]--1010
# a[1]--1020

# b = copy.deepcopy(a)
# b---2000
# b[0]---20010
# b[1]--20202

# In deep copy nested list also assigned to new address like the oringal one,
# This is the difference between shallow copy and deep Copy


# Iterables vs Iterators
lst = []
for i in range(0, 10):
    lst.append(i)

start_time = datetime.now()
for i in lst:
    pass
# Here List is iterable--> we are able to iterate list.

# Iterators

lst1 = iter(lst)

for i in lst1:
    pass


# Assertion---Assert Statement
# Assert statement to check if logical expression is true or false,
# Program execute procees only if expressions true, else it will
# Raise Assertion Error when it is false

num = int(input())
try:
    assert num % 2 == 0
    # only program came here,if above statement is true, else it will raise exception
    print('it is even number')
except Exception as e:
    print('Please enter only even number')
