from util import _validate_int

def gcd(a, b, checked = False):
    """
    Arguments:
        a (int): arbitrary integer
        b (int): arbitrary integer
        
    Returns:
        The greatest common divisor of ``a`` and ``b``

    Raises:
        TypeError: if ``a`` or ``b`` are not ints
        ValueError: if ``a`` or ``b`` are less than or equal to 0
    """

    if not checked:
        _validate_int(a)
        _validate_int(b)

    if a == b:
        return a
    elif a < b:
        a, b = b, a

    r = a % b

    if a % b == 0:
        return b
    
    return gcd(b, r, True)