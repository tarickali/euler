"""
title : 0014_longest_collatz_sequence.py
create : @tarickali 23/06/11
update : @tarickali 23/06/11

Problem Description:
--------------------
The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatz(n: int) -> int:
    cnt = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        cnt += 1
    return cnt

def solution(N: int = int(1e6)) -> int:
    best_len = 0
    best_num = 0
    for n in range(1, N):
        cnt = collatz(n)
        if cnt > best_len:
            best_len = cnt
            best_num = n
    return best_num, best_len

if __name__ == "__main__":
    sol = solution()
    print(sol)
