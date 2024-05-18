from arithmetic import sequences, factors
from config import settings

primes = sequences.primes(1000)
print(factors.gcd(primes[45], primes[57]))