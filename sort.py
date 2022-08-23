from random import randint


# Task 1

def bubble_sort(array):
    start = 0
    end = len(array) - 1
    for item in range(start, end):
        already_sorted = True
        for j in range(start, end - item):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        for i in range(end - 1, start - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                already_sorted = False
        start = start + 1

        if already_sorted:
            break
    return array


# Task 2

def merge_sorted_list(left, right):
    i = 0
    j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += [left[item] for item in range(i, len(left))] + \
              [right[item] for item in range(j, len(right))]
    return merged


def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2

    return merge_sorted_list(
        left=merge_sort([array[item] for item in range(midpoint)]),
        right=merge_sort([array[item] for item in range(midpoint, len(array))]))


# Task 3

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
    return array


def quick_sort(array, l=10):
    if len(array) < 2:
        return array
    pivot = array[randint(0, len(array))]
    smaller = [i for i in array if i < pivot]
    bigger = [i for i in array if i > pivot]
    equal = [i for i in array if i == pivot]
    if len(bigger) < l:
        sort_bigger = insertion_sort(bigger)
    else:
        sort_bigger = quick_sort(bigger)
    if len(smaller) < l:
        sort_smaller = insertion_sort(smaller)
    else:
        sort_smaller = quick_sort(smaller)
    return sort_smaller + equal + sort_bigger


def main():
    random_array = [randint(1, 100) for _ in range(10)]
    print(random_array)
    print('bubble sort', bubble_sort(random_array))
    print('merge sort', merge_sort(random_array))
    print('quick sort', quick_sort(random_array))


if __name__ == '__main__':
    main()

