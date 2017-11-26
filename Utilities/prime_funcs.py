import itertools
import math




def is_prime(n):
    """Determine whether or not `n` is prime."""
    if n in (2, 3, 5, 7, 11, 13, 17, 19): return(True)
    if (n<=1 or n%2==0 or n%3==0):        return(False)
    # determine upper limit of test range =>
    ulimit = (int(math.ceil(math.sqrt(n)))+1)
    return(not any(n%k==0 for k in range(3, ulimit, 2)))



def nth_prime(nth):
    """Return nth prime."""
    if nth<1:  return(None)
    if nth==1: return(2)
    if nth==2: return(3)
    if nth==3: return(5)
    if nth==4: return(7)

    # iterate until prime_cnt==nth =>
    prime_cnt = 4
    for iterval in itertools.count(11, 2):
        itertst = is_prime(iterval)
        prime_cnt+=(1 if itertst else 0)
        if prime_cnt==nth:
            res = iterval; break
    return(res)
