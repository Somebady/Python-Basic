# # Genrate all Binary Strings for n lengths
from math import sqrt
# n = int(input())

# x = ''
# lst = []
# for i in range(0, n):
#     pass


# print(divmod(29, 10))

# for i in range(100, 110):
#     print(i)
#     # i = list(i)
#     # print(len(i))

# def superpalindromesInRange(left: str, right: str) -> int:
#     count = 0
#     left = int(sqrt(int(left)))
#     right = int(sqrt(int(right)))
#     print(left, right)
#     for i in range(left, right+1):
#         if str(i) == str(i)[::-1]:
#             square = i*i
#             if str(square) == str(square)[::-1]:
#                 count=count+1
#     return count


# superpalindromesInRange(4, 1000)
# superpalindromesInRange(43143, 7072263972576)

def base3(n: int) -> str:
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))


# print(base3(12))

# print(divmod(121, 3))
# print(sqrt(7072263972576))
# 2659372.853244915
# 100000

# for i in range(1, 100):
#     s1 = str(i)
#     s2 = s1[-2::-1]
#     print(s1+s2)
# for i in range(1, 100):
#     s1 = str(i)
#     s2 = s1[::-1]
#     print(s1+s2)

# list1 = ['1', '2', '3', '4', '5']
# print(min(list1))


list2 = []
# for a, b in zip(list1, list2):
#     print(a, b)
print(list2[-1])
# print(ord('a')-ord('A'))
# print(ord('X')-ord('x'))

# x = 'Akshay'
# x = ''
# for i in list1:
#     x = x + ''.join(i)
# print(x)

# # x = ''

# head = 3
# print(type(head))
# print(type(head,))
# x = []
# x.append(head)
# print(x)


# vals = []
# i = 3
# while i:
#     vals += head,
#     i = i-1
# print(vals)
