from util import _validate_int

def squares(n):
    """
    Arguments:
        n (int): arbitray integer
        
    Returns:
        a list of squares up to the value of ``n``.

    Raises:
        TypeError: if ``n`` is not an int
        ValueError: if ``n`` is less than or equal to 0
    """
    _validate_int(n)
    
    return [ 
        i*i 
        for i in range(1, n+1) 
        if i*i < n 
    ]

def primes(n):
    """
    Generates a list of primes up to ``n`` using the Sieve of Erastothenes.

    Arguments:
        n (int): arbitrary integer

    Returns:
        A list of primes up to the values of ``n``

    Raises:
        TypeError: if ``n`` is not an int
        ValueError: if ``n`` is less than or equal to 0
    """
    _validate_int(n)

    sqs = squares(n) 
    sieve = {
        x: True
        for x in range(2,n+1)
    }

    # NOTE: len(sqs) + 2 gives the next closest root of a perfect square
    #           (because range(i, n) gives [i, i+1, ..., n - 2, n - 1])
    for i in range(2, len(sqs) + 2):
        if sieve[i]:
            for j in range(1+1, n // i + 1):
                sieve[i*j] = False

    return [ 
        k 
        for k,v 
        in sieve.items() 
        if v 
    ]
