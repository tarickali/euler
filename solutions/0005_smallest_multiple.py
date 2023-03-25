"""
title : 0005_smallest_multiple.py
create : @tarickali 23/03/25
update : @tarickali 23/03/25

Problem Description:
--------------------
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
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


def factor_decomposition(x: int, factors: list[int]) -> dict[int, int]:
    y = x
    decomposition = {}
    for f in factors:
        while y % f == 0:
            decomposition[f] = decomposition.get(f, 0) + 1
            y //= f
    return decomposition


def solution() -> int:
    N = 20
    primes = sieve(N)

    decompositions = {}
    for i in range(1, N + 1):
        factors = compute_factors(i, primes)
        decompositions[i] = factor_decomposition(i, factors)

    largest_factors = {}
    for i in decompositions:
        for factor, exponent in decompositions[i].items():
            largest_factors[factor] = max(largest_factors.get(factor, 0), exponent)

    best = 1
    for factor, exponent in largest_factors.items():
        best *= factor**exponent

    return best


if __name__ == "__main__":
    sol = solution()
    print(sol)
