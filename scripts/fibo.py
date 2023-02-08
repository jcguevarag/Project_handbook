def fibo(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


if __name__ == '__main__':
    assert fibo(0) == 0  # assert yields error if false
    assert fibo(1) == 1
    assert fibo(2) == 1
    assert fibo(6) == 8
    assert fibo(40) == 102334155
    print("Tests passed")
