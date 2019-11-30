from timeit import timeit

# naive approach, not caching
def fib_1(n):
    return fib_1(n-1) + fib_1(n-2) if n > 2 else 1

memo = {}
def fib_2(n):
    if n not in memo:
        memo[n] = fib_2(n-1) + fib_2(n-2) if n > 2 else 1
    return memo[n]

from functools import lru_cache
@lru_cache(maxsize=None)
def fib_3(n):
    return fib_3(n-1) + fib_3(n-2) if n > 2 else 1


def fib_4(n):
    fib = {1:1, 2:1}
    for i in range(3, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

print(fib_4(30))

print(fib_1(30), fib_2(30), fib_3(30))

print("Timings of fib_1:")
print(timeit('fib_1(29)', globals=globals(), number=1))
print(timeit('fib_1(30)', globals=globals(), number=1))
print(timeit('fib_1(31)', globals=globals(), number=1))
print(timeit('fib_1(32)', globals=globals(), number=1))

print("Timings of fib_2 (x1000):")
print(timeit('fib_2(29)', globals=globals(), number=1000))
print(timeit('fib_2(30)', globals=globals(), number=1000))
print(timeit('fib_2(31)', globals=globals(), number=1000))
print(timeit('fib_2(32)', globals=globals(), number=1000))

print("Timings of fib_3 (x1000):")
print(timeit('fib_3(29)', globals=globals(), number=1000))
print(timeit('fib_3(30)', globals=globals(), number=1000))
print(timeit('fib_3(31)', globals=globals(), number=1000))
print(timeit('fib_3(32)', globals=globals(), number=1000))
print(fib_3.cache_info())