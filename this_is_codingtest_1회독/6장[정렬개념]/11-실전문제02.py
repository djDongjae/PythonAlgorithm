#실전문제02[성적이 낮은 순서로 학생 출력하기] 181p
n = int(input())
array = []

for _ in range(n):
    name, score = input().split()
    array.append((name, int(score)))

def setting(data):
    return data[1]

array.sort(key=setting)

for i in range(n):
    print(array[i][0], end=" ")