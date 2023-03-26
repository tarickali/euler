"""
title : 0006_sum_square_difference.py
create : @tarickali 23/03/26
update : @tarickali 23/03/26

Problem Description:
--------------------
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

import math


def sieve(N: int, k: int) -> list[int]:
    A = [False] * (N + 1)
    m = int(math.sqrt(N))
    c = 0
    for i in range(2, m + 1):
        if not A[i]:
            c += 1
        if c == k:
            break
        j = i**2
        while j <= N:
            A[j] = True
            j += i

    primes = [i for i in range(2, N + 1) if not A[i]]
    return primes


def solution() -> int:
    N = int(1e6)
    k = 10001
    primes = sieve(N, k)
    return primes[k - 1]


if __name__ == "__main__":
    sol = solution()
    print(sol)
