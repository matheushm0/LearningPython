n = 600851475143


def largestPrimeFactor(n):
    i = 2
    while n > 1:
        if n % i == 0:
            n /= i
        else:
            i += 1
    return i


print(largestPrimeFactor(n))
