"""
title : 0018_maximum_path_sum_I.py
create : @tarickali 23/06/13
update : @tarickali 23/06/13

Problem Description:
-------------------
By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

# from __future__ import annotations
# from typing import Optional
# from dataclasses import dataclass


# @dataclass
# class TreeNode:
#     val: int
#     left: Optional[TreeNode]
#     right: Optional[TreeNode]


def parse_input(s: str) -> list[list[int]]:
    levels = []
    for level in s.strip().splitlines():
        levels.append([int(num) for num in level.split()])
    return levels


def maximum_path_sum(levels: list[list[int]]) -> int:
    memo = {}

    m = len(levels)
    for j in range(len(levels[m - 1])):
        memo[(m - 1, j)] = levels[m - 1][j]

    for i in reversed(range(m - 1)):
        for j in range(len(levels[i])):
            memo[(i, j)] = max(memo[i + 1, j], memo[i + 1, j + 1]) + levels[i][j]

    return memo[(0, 0)]


def solution(s: str) -> int:
    levels = parse_input(s)
    return maximum_path_sum(levels)


if __name__ == "__main__":
    s = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

    sol = solution(s)
    print(sol)
