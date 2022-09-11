class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, new_next):
        self.next = new_next


# Task 1
class UnorderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def pop(self):
        current = self.head
        previous = None
        if current is None:
            return "No item in list"
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        previous.set_next(None)
        return current.get_data()

    def insert_of_position(self, pos, item):
        current = self.head
        previous = None
        index = 0
        temp = Node(item)
        while current is not None and index < pos:
            previous = current
            current = current.get_next()
            index += 1
        if pos == 0:
            temp.set_next(self.head)
            self.head = temp
        else:
            if current is None:
                previous.set_next(temp)
            else:
                temp.set_next(current)
                previous.setNext(temp)

    def delete_from_position(self, pos):
        current = self.head
        previous = None
        index = 0
        if current is None:
            return "No item in list"
        while index < pos and current is not None:
            previous = current
            current = current.get_next()
            index += 1
        if current is None:
            return "No item in list"
        else:
            if previous is None:
                self.head = current.get_next()
            else:
                previous.setNext(current.get_next())
            return current.get_data()

    def insert(self, item):
        current = self.head
        previous = None
        temp = Node(item)
        if current is None:
            previous.set_next(temp)
        temp.set_next(self.head)
        self.head = temp
        return current.get_data()

    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current is not None and not found:
            if current.get_data() != item:
                index += 1
                current = current.get_next()
            else:
                found = True
        if found:
            return f'Element {item} has index {index}'
        else:
            return "Not Found"

    def generator_list(self):
        temp = self.head
        while temp is not None:
            yield temp.get_data()
            temp = temp.get_next()

    def slice(self, start=None, end=None):
        current = [i for i in self.generator_list()]
        if start is None or end is None:
            raise ValueError('Enter start and end')
        elif start < 0 or start > end or end > len(current)-1:
            raise ValueError('Wrong start or/and end')
        else:
            return current[start:end]

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self.head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"


# Task 2
class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def display(self):
        iter_node = self.head
        if self.is_empty():
            print("Stack Underflow")
        else:
            while iter_node is not None:
                print(iter_node.data, "->", end=" ")
                iter_node = iter_node.next
            return

    def __repr__(self):
        representation = "<Stack: "
        current = self.head
        while current is not None:
            representation += f"{current.data} "
            current = current.next
        return representation + ">"


# Task 3
class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def add_queue(self, item):
        temp = Node(item)

        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def del_queue(self):

        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

    def __repr__(self):
        representation = "<Queue: "
        current = self.front
        while current is not None:
            representation += f"{current.data} "
            current = current.next
        return representation + ">"


def main():
    my_list = UnorderedList()
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list)
    print(my_list.search(93))
    print(my_list.pop())
    print(my_list.insert(111))
    print(my_list.insert(103))
    print(my_list)
    print(my_list.pop())
    print(my_list)
    print(my_list.index(54))
    print(my_list.slice(2, 5))

########################################################################
    my_stack = Stack()
    my_stack.push(11)
    my_stack.push(22)
    my_stack.push(33)
    my_stack.push(44)
    print(my_stack)
    my_stack.display()
    print(f'\nTop element is {my_stack.peek()}')
    my_stack.pop()
    my_stack.pop()
    my_stack.display()
    print(f'\nTop element is {my_stack.peek()}')

########################################################
    q = Queue()
    q.add_queue(10)
    q.add_queue(20)
    q.add_queue(30)
    q.add_queue(40)
    q.add_queue(50)
    print(q)
    print(f'Queue Front: {q.front.data}')
    print(f'Queue Rear: {q.rear.data}')


if __name__ == '__main__':
    main()