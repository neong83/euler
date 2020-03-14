# Q: Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

from typing import List

MAX_VALUE = 4_000_000


def calculate_fibonacci_sequence(max_value, sequence) -> List[int]:
    next_value = sequence[-2] + sequence[-1]
    if next_value < max_value:
        sequence.append(next_value)
        calculate_fibonacci_sequence(max_value, sequence)
    return sequence


if __name__ == "__main__":
    fs = calculate_fibonacci_sequence(MAX_VALUE, [1, 2])
    print(fs)
    print(sum(filter(lambda x: (x % 2 == 0), fs)))