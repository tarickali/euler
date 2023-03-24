"""
title : 0003_largest_prime_factor.py
create : @tarickali 23/03/24
update : @tarickali 23/03/24

Problem Description:
--------------------
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
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


def compute_factors(N: int, candidates: list[int]) -> list[int]:
    factors = []
    for x in candidates:
        if N % x == 0:
            factors.append(x)
    return factors


def solution() -> int:
    N = 600851475143
    primes = sieve(int(math.sqrt(N)))
    factors = compute_factors(N, primes)
    return factors[-1]


if __name__ == "__main__":
    sol = solution()
    print(sol)
