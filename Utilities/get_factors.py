import math

def isprime(n):
    """
    Determine whether or not `n` is prime.
    """
    if n in (2, 3, 5, 7, 11, 13, 17, 19):
        return(True)
    if (n<=1 or n%2==0 or n%3==0):
        return(False)
    # determine upper limit of test range.
    ulim = (int(math.ceil(math.sqrt(n)))+1)
    return(not any(n%k==0 for k in range(3, ulim, 2)))


def get_factors(n):
    """
    Return factors of n, including 1 and n.
    """
    if isprime(n):
        res = [1, n]
    else:
        ulim = (n // 2) + 1
        if n%2==0:
            res = [i for i in range(1, ulim, 1) if n%i==0] + [n]
        else:
            res = [i for i in range(1, ulim, 2) if n%i==0] + [n]
    return(res)