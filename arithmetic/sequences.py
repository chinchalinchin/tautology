from .util import _validate_int
from .factors import gcd

def squares(n):
    """
    Arguments:
        n (int): arbitrary integer
        
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

def gcds(b):
    """
    Arguments:
        b (int): arbitrary integer

    Returns:
        a list ``e`` where each element at index ``i``, ``e[i]``, corresponds to the GCD of that element and ``b``, i.e. gcd(``i``, ``b``) = ``e[i]``, for all values of i = 1, 2, ..., b - 1.
    """
    return [ 
        gcd(i, b) 
        for i 
        in [ 
            i 
            for i 
            in range(1, b) 
        ]
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

def pseudoprimes(x):
    pseudos = []

    for i in range(1,x):
        rel_primes = [ 
            j + 1 
            for j, p 
            in enumerate(
                gcds(i)
            ) 
            if p == 1 
        ]

        if len(rel_primes) == i -1:
            pseudos.append(i)

    return pseudos