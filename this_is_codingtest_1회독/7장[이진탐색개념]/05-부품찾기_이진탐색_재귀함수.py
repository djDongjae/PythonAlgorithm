n = int(input())
n_array = list(map(int, input().split()))
m = int(input())
m_array = list(map(int, input().split()))

n_array.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for target in m_array:
    result = binary_search(n_array, target, 0, n-1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')