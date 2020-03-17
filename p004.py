# Q: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# .  Find the largest palindrome made from the product of two 3-digit numbers.

from itertools import product


def find_lower_limit(digit):
    number_of_zeros = digit - 1
    return int(str(1) + (str(0) * number_of_zeros))


def find_uppper_limit(digit):
    return find_lower_limit(digit + 1) - 1


def get_all_pairs_in_reserved_order(digit):
    lower = find_lower_limit(digit)
    upper = find_uppper_limit(digit)

    pairs = range(lower, upper + 1)
    return list(reversed(list(product(pairs, pairs))))


def convert_to_palindrome_mode(num):
    return int(str(num)[::-1])


def is_palindrome(num):
    if num == convert_to_palindrome_mode(num):
        return True
    return False


if __name__ == "__main__":
    reversed_pairs = get_all_pairs_in_reserved_order(3)
    # palindromes_dict = {}
    palindromes = []
    for a, b in reversed_pairs:
        product = a * b
        if is_palindrome(product):
            # palindromes[product] = (a, b)
            palindromes.append(product)

    print(max(palindromes))
