"""
title : 0011_largest_product_in_a_grid.py
create : @tarickali 23/03/29
update : @tarickali 23/03/29

Problem Description:
--------------------
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:
    1: 1
    3: 1,3
    6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import math
from functools import reduce


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


def count_divisors(decomposition: dict[int, int]) -> int:
    return reduce(lambda p, q: p * (q + 1), decomposition.values(), 1)


def solution() -> int:
    m = 500
    N = 10000000
    primes = sieve(N)

    x = 0
    i = 1
    while True:
        x += i
        factors = compute_factors(x, primes)
        decomposition = factor_decomposition(x, factors)
        num_divisors = count_divisors(decomposition)
        print(x, num_divisors)
        if num_divisors > m:
            break
        i += 1
    return x


if __name__ == "__main__":
    sol = solution()
    print(sol)
