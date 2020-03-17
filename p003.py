# Q: The prime factors of 13195 are 5, 7, 13 and 29.
# .  What is the largest prime factor of the number 600851475143 ?

import math


def find_factors(value):
    factors = []
    for i in range(2, int(math.sqrt(value) + 1)):
        for j in (i, value // i):
            if value % j == 0:
                factors.append(j)

    return set(factors)


def is_prime(num) -> bool:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def find_largest_factor(value):
    factors = []
    for num in find_factors(value):
        if is_prime(num):
            factors.append(num)

    print(factors)
    return max(factors)


if __name__ == "__main__":
    input_value = 600851475143
    factor = find_largest_factor(input_value)
    print(f"largest prime number: {factor}")
