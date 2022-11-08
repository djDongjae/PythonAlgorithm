def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = map(int, input('원소의 개수와 찾으려는 값을 입력하시오: ').split())
array = list(map(int, input('배열을 입력하시오: ').split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('찾으려는 값이 없습니다.')
else:
    print(str(result+1)+'번째 원소입니다.')