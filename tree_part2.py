class MaxBinHeap:
    def __init__(self) -> None:
        self.heap_list: list[int] = [0]
        self.size: int = 0

    def build_heap(self, items: list[int]) -> None:
        i = len(items) // 2
        self.size = len(items)
        self.heap_list = [0] + items[:]
        while i > 0:
            self.perc_down(i)
            i -= 1

    def perc_up(self, i: int) -> None:
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = \
                    self.heap_list[i // 2], self.heap_list[i]
            i //= 2

    def perc_down(self, i: int) -> None:
        while i * 2 <= self.size:
            max_child = self.max_child(i)
            if self.heap_list[i] < self.heap_list[max_child]:
                self.heap_list[i], self.heap_list[max_child] = \
                    self.heap_list[max_child], self.heap_list[i]
            i = max_child

    def max_child(self, i: int) -> int:
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap_list[i*2] > self.heap_list[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

    def del_max(self) -> int:
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

    def insert(self, k: int) -> None:
        self.heap_list.append(k)
        self.size += 1
        self.perc_up(self.size)

    def __repr__(self):
        return f'Heap {self.heap_list[1:]} '


class PriorityQueue(MaxBinHeap):
    def __init__(self) -> None:
        super().__init__()

    def enqueue(self, item) -> None:
        self.insert(item)

    def dequeue(self) -> int:
        return self.del_max()


def main():
    # Task 1
    h = MaxBinHeap()
    h.build_heap([20, 3, 26, 25, 100, 22])
    print(h)
    h.insert(35)
    print(h)
    print(h.del_max())
    print(h)
    print('#'*80)


###############################################################
    # Task 2
    pq = PriorityQueue()
    print(pq)
    pq.enqueue(5)
    pq.enqueue(8)
    pq.enqueue(33)
    print(pq)
    print(pq.dequeue())
    print(pq)


if __name__ == '__main__':
    main()