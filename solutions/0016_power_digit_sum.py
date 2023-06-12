"""
title : 0016_power_digit_sum.py
create : @tarickali 23/06/12
update : @tarickali 23/06/12

Problem Description:
--------------------
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def solution(n: int) -> int:
    power = str(2**n)
    dsum = 0
    for i in power:
        dsum += int(i)
    return dsum


if __name__ == "__main__":
    sol = solution(1000)
    print(sol)
