def fibo(x):
    if x == 1 or x == 2:
        return 1
    print('loading...')
    return fibo(x - 1) + fibo(x - 2)


print(fibo(100))