n = int(input())
n_array = list(map(int, input().split()))
m = int(input())
m_array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

for target in m_array:
    result = binary_search(n_array, target, 0, n-1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')