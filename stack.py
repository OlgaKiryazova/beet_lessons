# Task 1

class Stack:

    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        return bool(self.items)

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self) -> int:
        return len(self.items)

    def __repr__(self) -> str:
        return f'Stack: {self.items}'

    def reverse_(self) -> str:
        stack = []
        for i in self.items:
            stack.append(i)
        string = ''
        for i in range(0, self.size()):
            string += str(stack.pop())
        return string

    # task 3
    def get_from_stack(self, element):
        for elem in self.items:
            if elem == element:
                self.items.remove(elem)
                return element
        else:
            raise ValueError('Element is not on the stack')


##############################################################################
# Task 2

def balanced_brackets(string_: str) -> bool:
    stack: list = []
    is_good: bool = True
    for i in string_:
        if i in '[{(':
            stack.append(i)
        elif i in '}])':
            if not stack:
                is_good = False
                break
            bracket = stack.pop()
            if (bracket == '[' and i == ']' or bracket == '{' and i == '}'
                or bracket == '(' and i == ')'):
                continue
            is_good = False
            break
    if is_good == True and len(stack) == 0:
        return True
    else:
        return False


class Queue:
    def __init__(self) -> None:
        self._items = []

    def is_empty(self) -> bool:
        return bool(self._items)

    def enqueue(self, item) -> None:
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f'Queue: {self._items}'

    def get_from_queue(self, element):
        for elem in self._items:
            if elem == element:
                self._items.remove(elem)
                return element
        else:
            raise ValueError('Element is not on the queue')


def main():

    print(balanced_brackets('(()))'))
    print(balanced_brackets('[{}]()'))

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack)
    print(stack.reverse_())
    print(stack.get_from_stack(2))
    print(stack)
    # print(stack.get_from_stack(2))

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(5)
    queue.enqueue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(4)
    print(queue)
    print(queue.get_from_queue(3))
    print(queue)


if __name__ == '__main__':
    main()
