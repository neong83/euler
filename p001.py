# Q: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#    Find the sum of all the multiples of 3 or 5 below 1000.


def is_number_divide_by_three(value):
    return (value / 3).is_integer()


def is_number_divide_by_five(value):
    return (value / 5).is_integer()


def get_natural_numbers(max_value):
    natural_numbers = []
    for i in range(1, max_value):
        if is_number_divide_by_three(i) or is_number_divide_by_five(i):
            natural_numbers.append(i)

    return natural_numbers


if __name__ == "__main__":
    natural_numbers = get_natural_numbers(1000)
    print(sum(natural_numbers))
