# Task 1

def with_index(iterable, start=0):
    iterator = iter(iterable)
    next_element_exists = True

    while next_element_exists:
        try:
            from_iterator = next(iterator)
            print(f'{from_iterator} : {start}')
            start += 1
        except StopIteration:
            next_element_exists = False


##################################################################################
# Task 2

# def in_range(start, end, step=1):
#     iterator = start - step
#     while iterator+step != end:
#         iterator += step
#         print(iterator)
#     print('stop')


# def in_range(start, end, step=1):
#     if step > 0:
#         # num = start - step
#         while num < end:
#             print(num)
#             num += step
#
#     elif step < 0:
#         num = start + step
#         while num > end:
#             print(num)
#             num += step
#     print('stop')

def in_range(start, end, step=1):
    if step > 0:
        while start < end:
            print(start)
            start += step
    elif step < 0:
        while start > end:
            print(start)
            start += step
    print('stop')



def main():
    a = ['a','b', 'c', 't']
    with_index(a, 5)
    in_range(10, 1, -1)
    in_range(1, 10, 5)


if __name__ == '__main__':
    main()