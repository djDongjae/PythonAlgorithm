def count_by_value(array, x):
    length = len(array)
    a = first(array, x, 0, length-1)
    if a == None:
        return 0
    b = last(array, x, 0, length-1)
    return b-a+1

def first(array, target, start, end):
    if start > end:
        return None
    else:
        mid = (start+end)//2
        if (mid == 0 or target > array[mid-1]) and array[mid] == target:
            return mid
        elif target <= array[mid]:
            return first(array, target, start, mid-1)
        else:
            return first(array, target, mid+1, end)

def last(array, target, start, end):
    if start > end:
        return None
    else:
        mid = (start+end)//2
        if (mid == n-1 or target < array[mid+1]) and array[mid] == target:
            return mid
        elif target >= array[mid]:
            return last(array, target, mid+1, end)
        else:
            return last(array, target, start, mid-1)

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)
if count == 0:
    print(-1)
else:
    print(count)