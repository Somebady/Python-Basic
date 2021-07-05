# Modified by Personal Laptop
def makeGood(s) -> str:
    stack = []
    # x=reduce(lambda a,b: a+b if abs(ord(a)-ord(b)) == 32 else '',s)
    for i in range(0, len(s)-1):
        if stack is None:
            stack.append(s[i])
        else:
            print(stack[-1])
            if abs(ord(stack[-1])-ord(s[i])) == 32:
                stack.pop()
            else:
                stack.append(s[i])
    print(stack)


# makeGood('abc')
# stack = []
# if stack:
#     print(stack[-1])
# else:
#     print('Akshay')

s = ["0"]
print("1" if any(s) else "0")
