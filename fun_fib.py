def fib_rec(n):
    if n == 1: return 0
    elif n == 2: return 1
    else: return fib_rec(n-1) + fib_rec(n-2)


if __name__ == '__main__':
    for i in range(1, 100):
        print(fib_rec(i))