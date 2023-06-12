"""
title : 0015_lattice_paths.py
create : @tarickali 23/06/12
update : @tarickali 23/06/12

Problem Description:
--------------------
Starting in the top left corner of a 2x2 grid, and only being able to move
to the right and down, there are exactly routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""


def solution(m: int, n: int) -> int:
    m += 1
    n += 1
    memo = [[0] * n for _ in range(m)]

    for i in range(m):
        memo[i][0] = 1
    for j in range(n):
        memo[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

    return memo[m - 1][n - 1]


if __name__ == "__main__":
    sol = solution(20, 20)
    print(sol)
