from time import perf_counter
import matplotlib.pyplot as plt


# 1 - n^2
def question1(first_list: list[int], second_list: list[int]) -> list[int]:
    res: list[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


# 2 - 1
def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n


# 3 - n^2
def question3(first_list: list[int], second_list: list[int]) -> list[int]:
    temp: list[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp


# 4 - n
def question4(input_list: list[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


# 5 - n^2
def question5(n: int) -> list[tuple[int, int]]:
    res: list[tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


# 6 - log n
def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n


def time_texting(number):

    x = []
    y = []

    for i in range(1, 1001):
        first = [i for i in range(i)]
        second = [i for i in range(i)]
        x.append(i)

        dict_function = {
            1: question1,
            2: question2,
            3: question3,
            4: question4,
            5: question5,
            6: question6
        }
        dict_arg = {
            1: (first, second),
            2: (i, ),
            3: (first, second),
            4: (first, ),
            5: (i, ),
            6: (i, )
        }

        t1 = perf_counter()
        dict_function.get(number)(*dict_arg.get(number))
        t2 = perf_counter()
        y.append(t2 - t1)

    fig, ax = plt.subplots()
    ax.plot(x, y, color='green')
    fig.savefig(f'time_complexity_{number}.png')

    print(f'{number} finished')


def main():
    for number in range(1, 7):
        time_texting(number)


if __name__ == '__main__':
    main()
