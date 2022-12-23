# Q24[안테나] 361p
n = int(input())
houses = list(map(int, input().split()))
houses.sort()
print(houses[(n-1)//2])