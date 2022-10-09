def print_squares_of_numbers_upto(n):
    for i in range(1, n + 1):
        print(i * i)


print_squares_of_numbers_upto(10)


def print_square_of_even_numbers(n):
    for i in range(2, n + 1, 2):
        print(i * i)


print_square_of_even_numbers(10)


def print_numbers_in_reverse(n):
    for i in range(n, 0, -1):
        print(i)


print_numbers_in_reverse(10)

def sum_of_two_numbers(number1, number2):
    sum = number1 + number2
    # return sum


print(sum_of_two_numbers(5, 7))