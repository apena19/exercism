def square_of_sum(number):
    return sum(range(1, number+1)) ** 2


def sum_of_squares(number):
    a = 0
    for x in range(1, number+1):
        a += x**2
    return a


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
