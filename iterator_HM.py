# Task 1

def with_index(iterable, start=0):
    for i in iterable:
        yield i, start
        start += 1

##################################################################################
# Task 2


def in_range(start, end, step=1):
    if step > 0:
        while start < end:
            yield start
            start += step
    elif step < 0:
        while start > end:
            yield start
            start += step


#################################################################################
# Task 3

class Iterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable)-1:
            self.index += 1
            return self.iterable[self.index]
        else:
            raise StopIteration

    def __getitem__(self, item):
        return self.iterable[item]




def main():
    a = ['a','b', 'c', 't']
    for i in with_index(a, 5):
        print(i)
    generator = in_range(10, 1, -1)
    # generator = in_range(1, 10, 2)
    for i in generator:
        print(i)

    iterator = Iterator([1, 2, 3, 4, 5])
    for i in iterator:
        print(i)

    print(iterator[1])


if __name__ == '__main__':
    main()