"""
title : 0010_summation_of_primes.py
create : @tarickali 23/03/28
update : @tarickali 23/03/28

Problem Description:
--------------------
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import math


def sieve(N: int) -> list[int]:
    A = [True] * (N + 1)
    m = int(math.sqrt(N))
    for i in range(2, m + 1):
        j = i**2
        while j <= N:
            A[j] = False
            j += i

    primes = [i for i in range(2, N + 1) if A[i]]
    return primes


def solution() -> int:
    N = 2000000
    primes = sieve(N)
    total = 0
    for prime in primes:
        total += prime
    return total


if __name__ == "__main__":
    sol = solution()
    print(sol)
