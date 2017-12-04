"""
From docs.

From array module =>
'b'	signed char	int	1
'B'	unsigned char	int	1
'u'	Py_UNICODE	Unicode character	2	(1)
'h'	signed short	int	2
'H'	unsigned short	int	2
'i'	signed int	int	2
'I'	unsigned int	int	2
'l'	signed long	int	4
'L'	unsigned long	int	4
'q'	signed long long	int	8	(2)
'Q'	unsigned long long	int	8	(2)
'f'	float	float	4
'd'	double	float	8
"""
import multiprocessing
import time
import sys
import math
import array
import numpy as np


def is_prime(n):
    """Determine whether or not `n` is prime."""
    if n in (2, 3, 5, 7, 11, 13, 17, 19): return(True)
    if (n<=1 or n%2==0 or n%3==0): return(False)
    # determine upper limit of test range =>
    ulimit = (int(math.ceil(math.sqrt(n)))+1)
    return(not any(n%k==0 for k in range(3, ulimit, 2)))


def p_func(n):
    if is_prime(n): return(n)
    else          : return(-1)


# parallel execution time (4 CPU's) chunksize=1000 lock=True   =>  49.893152952194214
# parallel execution time (4 CPU's) chunksize=100 lock=False   =>  44.0893669128418
# parallel execution time (4 CPU's) chunksize=100 lock=True    =>  48.39470863342285
# parallel execution time (4 CPU's) chunksize=1000 lock=False  =>  39.51719665527344
# parallel execution time (4 CPU's) chunksize=10000 lock=False =>  38.819742918014526


# sequential execution time (1 CPU) =>  72.84809112548828


if __name__ == "__main__":


    ti = time.time()

    # arr = array.array('L', range(1, 5000000))
    # pool_outputs = map(p_func, arr)
    # solution = len([i for i in pool_outputs if i!=-1])
    # print(solution)
    # print("Sequentially: {}".format(time.time()-ti))
    # sys.exit()

    #arr = multiprocessing.Array('L', range(1, 5000000))
    arr = multiprocessing.Array('L', np.array(range(1, 5000000)), lock=False)
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    pool_outputs = pool.imap(p_func, arr, chunksize=1000)
    pool.close(); pool.join()

    solution = len([i for i in pool_outputs if i!=-1])
    print(solution)
    print("In parallel: {}".format(time.time()-ti))
    sys.exit()
