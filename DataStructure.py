# # # Bubble Sort

# # a = [1, 2, 6, 3, 1, 4]


# # cnt = 0
# # for i in range(0, len(a)):
# #     for j in range(i+1, len(a)):
# #         cnt = cnt+1
# #         if a[i] > a[j]:
# #             a[i], a[j] = a[j], a[i]
# #     print(a)
# # print('Bubble Sort:', a, cnt)

# # # Question1, How many numeber's are not present in ascending order
# # a = [1, 2, 6, 3, 1, 4, 6, 9, 7]
# # count = 1
# # for i in range(0, len(a)):
# #     for j in range(i+1, len(a)):
# #         if a[i] > a[j]:
# #             count = count+1
# #             break

# # print(count)
# # # print([1, 2, 6, 3, 1, 4])
# # nums = [2, 6, 4, 8, 10, 9, 15]
# # lst = []
# # for i in range(0, len(nums)-1):
# #     if nums[i] > nums[i+1]:
# #         # print(i)
# #         for j in range(len(nums)-1, i, -1):
# #             if nums[j-1] > nums[j]:
# #                 print(i, j)
# #                 print(nums[i:j+1])
# #                 break
# # print(lst)
# # # nums = [2, 6, 4, 8, 10, 9, 15]
# # nums = a = [1, 2, 6, 3, 0, 4]
# # res = [i for (i, (a, b)) in enumerate(zip(nums, sorted(nums))) if a != b]
# # print(res)
# # print(0 if not res else res[-1] - res[0] + 1)


# # # for i in enumerate(nums):
# # #     print(i)

# def heightChecker(heights) -> int:
#     expected = heights.copy()
#     l = len(expected)
#     for i in range(0, l):
#         for j in (i+1, l):
#             if expected[i] > expected[j]:
#                 expected[i], expected[j] = expected[j], expected[i]
#     # for i in range(0, l):
#     #     for j in range(i+1, l):
#     #         if expected[i] > expected[j]:
#     #             expected[i], expected[j] = expected[j], expected[i]

#     ans = 0
#     print(heights)
#     print(expected)
#     for i in range(0, l):
#         if heights[i] != expected[i]:
#             ans = ans+1
#     return ans


# heightChecker([1, 1, 4, 2, 1, 3])

# x = [1, 2, 3, 12, 20, 400]
# for i in x:
#     print('%10', i % 10)
# print('11%1', 11 % 1)
# num = 11
# while num:
#     if 11 % (num % 10) != 0 or num == 1 or num % 10 == 1:
#         print('true', num)
#         num = num//10
#     else:
#         print(False)
#         break
# n = 12
# if n < 2:
# #     print(0)
# n = 10000000
# s = [1] * n
# s[0] = s[1] = 0

# for i in range(2, int(n ** 0.5) + 1):
#     if s[i] == 1:
#         s[i * i:n:i] = [0] * len(s[i * i:n:i])
# print(sum(s))
if 110 % 11 and 110 % 5:
    print('Akshay')
