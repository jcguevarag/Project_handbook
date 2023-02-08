def fib(x):
    cache = {}  # Use to avoid running many times

    def fib_inner(x):
        nonlocal cache
        if x in cache:
            return cache[x]
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            val = fib_inner(x - 1) + fib_inner(x - 2)
            cache[x] = val
            return val
    return fib_inner(x)


if __name__ == '__main__':
    assert fib(0) == 0  # assert yields error if false
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(6) == 8
    assert fib(40) == 102334155
    print("Tests passed")


""" def fibo(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


if __name__ == '__main__':
    assert fibo(0) == 0
    assert fibo(1) == 1
    assert fibo(2) == 1
    assert fibo(6) == 8
    assert fibo(40) == 102334155
    print("Tests passed")
"""
