def gcd(a, b):
    if a == b:
        return a
    elif a < b:
        a, b = b, a

    r = a % b

    if a % b == 0:
        return b
    
    return gcd(b, r)