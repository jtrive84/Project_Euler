"""
You can pass either a function or a string statement to the
timeit.timeit() instance.
It seems functions with arguments cannot be passed to timeit.timeit(),
so construct the function to pass to timeit.timeit() with values
hard coded.
"""
#Assume:
def cf(): return(map(lambda x: pow(x, .99), range(5)))

#Pass cf to timeit.timeit() instance. Default is timeit.timeit(number=1000000)
timeit.timeit(<function_no_args>, number=1000000)

#A string argument will work as well:
timeit.timeit('for i in range(10): bin(i)')

#repeat a routine a given number of times:
timeit.repeat('for i in range(10): bin(i)',repeat=5)

#it can also be used on the command line by passing a string:
#<E:\> $ python -m timeit "'-'.join(str(n) for n in range(50))"
#100000 loops, best of 3: 13.2 usec per loop
