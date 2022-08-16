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

    def __repr__(self):
        return f'Stack: {self.items}'

    # task 3
    def get_from_stack(self, element):
        for elem in self.items:
            if elem == element:
                self.items.remove(elem)
                return element
        else:
            raise ValueError('Element is not on the stack')


def reverse_(string: str | int) -> str:
    n = len(string)
    s = Stack()
    for i in range(0, n):
        s.push(string[i])
    string = ""
    for i in range(0, n):
        string += s.pop()
    return string


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



def main():
    print(reverse_('apple'))
    print(reverse_('123456'))

    print(balanced_brackets('(()))'))
    print(balanced_brackets('[{}]()'))

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack)
    stack.get_from_stack(2)
    print(stack)
    # stack.get_from_stack(2)




if __name__ == '__main__':
    main()
