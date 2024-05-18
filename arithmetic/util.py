def _validate_int(n):
    if type(n) != int:
        raise TypeError(f"{n} is not an int!")
    elif n == 0 or n < 0:
        raise ValueError(f"{n} <= 0!")
