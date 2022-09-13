# Task 1

import threading


class Counter(threading.Thread):
    counter = 0
    rounds = 100_000

    def run(self) -> None:
        for _ in range(Counter.rounds):
            Counter.counter += 1


t1 = Counter()
t2 = Counter()

t1.start()
t2.start()

t1.join()
t2.join()

print(t1.counter, t2.counter)