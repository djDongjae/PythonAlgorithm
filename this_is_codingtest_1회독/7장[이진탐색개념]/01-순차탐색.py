def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1
    return

n = int(input('n: '))
target = input('target: ')

array = input('array: ').split()
print(sequential_search(n, target, array))
