# Based on https://www.youtube.com/watch?v=i7sm9dzFtEI
# m and n are cmd line args

import sys

m, n = (int(sys.argv[1]), int(sys.argv[2]))

# def ack(m, n):
    # if m == 0:
        # ans = n + 1
    # elif n == 0:
        # ans = ack(m-1, 1)
    # else:
        # ans = ack(m-1, ack(m, n-1))

    # return ans

# print(ack(m, n))


def power_of(number, power, original=None):
    """
    Number - base
    Power - power to raise to
    Original - original number we started with so we don't multiply exponentially
    """
    if not original:
        original = number
    n = number
    p = power
    o = original

    if p == 1:
        return n
    else:
        print(f"Calculating {n} x {original}")
        n = n*original
        return power_of_manual(n, p-1, original)
