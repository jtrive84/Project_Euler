def fibonacci_seq(upto):
    """
    Return the Fibonacci sequence up to upto.
    """
    seq = [1, 2]
    while seq[-1] < upto:
        seq.append(seq[-1]+seq[-2])
    return(seq)
