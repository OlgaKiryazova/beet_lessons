import asyncio
import time
import multiprocessing

# Asynchronous execution
async def factorial_async(nums):
    res = []
    for n in nums:
        for i in range(n-1, 1, -1):
            n *= i
        res.append(n)
        await asyncio.sleep(0)
    return res


async def fibonacci_async(nums):
    res = []
    first = 1
    second = 1
    for n in nums:
        res.append(first)
        first, second = second, first + second
        await asyncio.sleep(0)
    return res


async def square_async(nums):
    res = []
    for n in nums:
        res.append(n ** 2)
        await asyncio.sleep(0)
    return res


async def cubic_async(nums):
    res = []
    for n in nums:
        res.append(n ** 3)
        await asyncio.sleep(0)
    return res


async def main_async():
    res = await asyncio.gather(factorial_async(numbers), fibonacci_async(numbers),
                               square_async(numbers), cubic_async(numbers))
    print(res)


################################################################
# Synchronous execution

def factorial(nums):
    res = []
    for n in nums:
        for i in range(n-1, 1, -1):
            n *= i
        res.append(n)
    return res


def fibonacci(nums):
    res = []
    first = 1
    second = 1
    for n in nums:
        res.append(first)
        first, second = second, first + second
    return res


def square(nums):
    res = []
    for n in nums:
        res.append(n ** 2)
    return res


def cubic(nums):
    res = []
    for n in nums:
        res.append(n ** 3)
    return res


def main():
    res = [factorial(numbers), fibonacci(numbers), square(numbers), cubic(numbers)]
    print(res)


#####################################################################
# Pool of processes


def main_mult():
    funcs = [factorial, fibonacci, square, cubic]
    with multiprocessing.Pool(4) as pool:
        results = [pool.apply_async(fn, (numbers,)) for fn in funcs]
        print([result.get() for result in results])



if __name__ == '__main__':

    numbers = [n for n in range(1, 11)]

    print('Asynchronous execution')
    start = time.perf_counter()
    asyncio.run(main_async())
    print(time.perf_counter() - start)

    print('\nSynchronous execution')
    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)

    print('\nPool of processes')
    start = time.perf_counter()
    main_mult()
    print(time.perf_counter() - start)


