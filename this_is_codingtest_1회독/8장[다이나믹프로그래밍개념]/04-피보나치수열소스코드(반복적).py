d = [0] * 101

d[1] = 1
d[2] = 1


def fibo(x):
    for i in range(3, x + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[x]


print(fibo(5))
