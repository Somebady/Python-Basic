
# Binary Exponential Algorithm
from math import sqrt


def exp(base, exp):
    res = 1
    count = 0
    while exp > 0:
        # count += 1 -to check how many times loop is running--curocity purpose
        if exp & 1:  # bit wise method to check even odd--same as exp%2
            res = res*base
        base = base*base
        exp >>= 1  # but wise method same exp //= 2
    print(res, count)

# Fn calling
# exp(10, 10000)


# --------------------
# String
# Important String Questions
# 1 Get all sub strings
s = 'abc'
n = len(s)


def getSubStrings(s, n):
    result = []
    for i in range(n):
        for j in range(i+1, n+1):
            result.append(s[i:j])
    # print(result)
    return result


# getSubStrings(s, n)
# Get only count
# print(n*(n+1)//2)
# Get substring start with a and ends with b
# Instruction
# 1.first get the count of a, then --> ans=n*(n-1)//2
# 2.if want single entries as well then add count of a in ans whould be your final ans


# Permutations of String

result = []


def permute(data, i, length):
    if i == length:
        result.append(''.join(data))
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]  # BackTracking


# permute(list('aab'), 0, len(s))
# print(set(result)) --to get only unique combinations

# -----------------------------------
# Get the jsut net greater no
x = '218765'
x = [i for i in str(x)]
n = len(x)


def getNxtGreater(n):
    m1 = min(x)


print(x)


# GCD of Two Number's (EUCLID Therom)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# print(gcd(24, 600))


# Sieve of Eratosthenes --FInding prime numbers in range

def nPrime(n):
    isPrime = [True]*(n+1)
    isPrime[0] = isPrime[1] = False

    for i in range(2, int(sqrt(n))+1):
        # j = i << 1  # Bit wise method same as 2*i
        # while j <= n:
        #     isPrime[j] = False
        #     j = j+i
        if isPrime[i]:
            isPrime[i*i:n:i] = [False]*len(isPrime[i*i:n:i])
    for i in range(len(isPrime)):
        if isPrime[i]:
            print(i, end=",")


nPrime(222)

# No of prime or not


def chk_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # Every prime number is form of 6k+-1
    return True


# print(chk_prime(104729))
# print(78 % 6)
# -------------------------------------------------------------------
