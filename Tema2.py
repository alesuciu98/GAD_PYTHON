# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care
# reprezintă numere întregi sau reale.

def add_function(*arg):
    sum = 0
    for a in arg:
        if type(a) == int or type(a) == float:
            sum += a
    return sum


def verify_first_exercise():
    print(add_function(4, 3, -7, 0, 9, 'cuvant', ('x', 'y'), ))
    print(add_function(1, 5, -3, 'abc', [12, 56, 'cad']))
    print(add_function())
    print(add_function(2, 4, 'abc'))


# Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg,
# altfel returnează valoarea 0.

def read_from_keyboard():
    my_var = input('Introduceti un nr: ')
    try:
        my_int = int(my_var)
        return my_int
    except ValueError:
        return 0


# Să se scrie un modul care contine 3 funcții recursive care primesc ca parametru un număr întreg și returnează:
# ○ suma tuturor numerelor de la [0, n]

def sum_all_numbers(n):
    if n == 0:
        return 0
    return n + sum_all_numbers(n - 1)


# ○ suma numerelor pare de la [0, n]

def sum_even_numbers(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + sum_even_numbers(n - 1)
    return sum_even_numbers(n - 1)


# ○ suma numerelor impare de la [0. n]

def sum_odd_numbers(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return n + sum_odd_numbers(n - 1)
    return sum_odd_numbers(n - 1)


if __name__ == '__main__':
    # verify_first_exercise()
    print(read_from_keyboard())
    print(sum_all_numbers(9))
    print(sum_even_numbers(8))
    print(sum_odd_numbers(5))
