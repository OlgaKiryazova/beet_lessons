from random import randint
from time import perf_counter


def timer(function):
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        result = function(*args, **kwargs)
        print(f'{function.__name__} took {perf_counter() - t1} seconds')
        return result
    return wrapper

# Task1
@timer
def binary_search(list_, x, high, low=0):
    if low > high:
        return False
    else:
        middle = (low + high) // 2
        if x == list_[middle]:
            return f'binary search: number {x} is in {middle} index'
        elif x > list_[middle]:
            return binary_search(list_, x,  high, middle + 1)

        else:
            return binary_search(list_, x, middle - 1, low)


# Task 2
@timer
def fibonacci_search(list_, x):
    size = len(list_)
    start = -1
    f0 = 0
    f1 = 1
    f2 = 1
    while f2 < size:
        f0 = f1
        f1 = f2
        f2 = f1 + f0
    while f2 > 1:
        index = min(start + f0, size - 1)
        if list_[index] < x:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif list_[index] > x:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return f'fibonacci search: number {x} is in {index} index'
    if (f1) and (list_[size - 1] == x):
        return size - 1
    else:
        return False


# Task3



def main():
    arr = [2, 3, 4, 10, 40]
    x = 2
    t1 = perf_counter()
    print(binary_search(arr, x, len(arr)))
    print(perf_counter() - t1)

    t1 = perf_counter()
    print(fibonacci_search(arr, x))
    print(perf_counter() - t1)



if __name__ == '__main__':
    main()
