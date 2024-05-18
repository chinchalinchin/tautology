from arithmetic import factors

import matplotlib.pyplot as plot

def gcd(b):
    """
    Displays a graph of the function ``gcd(x, b)`` where ``b`` is a fixed integer.

    Arguments:
        b (int): Number whose GCD is to be computed and displayed for all integer values up to ``b``.
    Returns:
        None
    """

    (_, axes) = plot.subplots()

    x = [ i for i in range(1, b+1) ]
    y = [ factors.gcd(i, b) for i in x ]

    axes.plot(x, y, linestyle='none', marker="o")

    plot.show()