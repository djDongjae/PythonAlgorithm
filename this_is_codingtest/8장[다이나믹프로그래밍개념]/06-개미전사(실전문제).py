n = int(input())

array = list(map(int, input().split()))

# d[i] = max(d[i-1], d[i-2] + array[i])
d = [0] * 100
d[0] = array[0]
d[1] = max(d[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i-2] + array[i])
print(d[n-1])
