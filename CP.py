
# Binary Exponential


def exp(base, exp):
    res = 1
    while exp > 0:
        if exp % 2:
            res = res*base
        base = base*base
        # exp >>= 1
        exp //= 2
    print(res)


exp(10, 1)
