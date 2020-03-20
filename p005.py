# Q: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# . What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# https://stackoverflow.com/questions/19348430/project-euler-getting-smallest-multiple-in-python
from math import gcd
from functools import reduce


def lowset_common_divider(a, b) -> int:
    # gcd(4, 8) => 4
    # 4 * 8 = 32
    # 32 / 4 = 8 <- this is the lowest common divider from both 4 and 8

    return (a * b) // gcd(a, b)


if __name__ == "__main__":
    # test
    print("test")
    # reduce(func, seq)
    # this implies -> lowset_common_divider(lowset_common_divider(a, b), c)
    # taken the result and apply to another `lowset_common_divider` method as parameter
    print(reduce(lowset_common_divider, range(1, 10 + 1)))
    # actual
    print("result")
    print(reduce(lowset_common_divider, range(1, 20 + 1)))
