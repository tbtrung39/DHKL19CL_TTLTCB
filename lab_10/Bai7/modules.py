import random
import math


def create_list(n=20, max_value=100):
    result = []
    for i in range(n):
        result.append(random.randint(0, max_value))
    return result


def list_div7(lst):
    res = []
    for x in lst:
        if x % 7 == 0:
            res.append(x)
    return res


def list_odds(lst):
    res = []
    for x in lst:
        if x % 2 != 0:
            res.append(x)
    return res


def sum_list(numbers):
    total = 0
    for x in numbers:
        total += x
    return total


def list_squares(lst):
    res = []
    for x in lst:
        if x >= 0:
            r = int(math.sqrt(x))
            if r * r == x:
                res.append(x)
    return res


def show_report(lst):
    print('Dãy số:', lst)
    print('Số chia hết cho 7:', list_div7(lst))
    odds = list_odds(lst)
    print('Các số lẻ:', odds)
    print('Tổng số lẻ:', sum_list(odds))
    squares = list_squares(lst)
    if squares:
        print('Các số chính phương:', squares)
    else:
        print('Không có số chính phương trong dãy.')


if __name__ == '__main__':
    seq = create_list()
    show_report(seq)


