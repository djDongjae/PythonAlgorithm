'''from itertools import product

sets = [0, 1]

data = list(product(sets, repeat = 4))
print(data)
print(len(data))'''

from itertools import product


def solution(triangle):
    sets = [0, 1]
    data = list(product(sets, repeat=len(triangle) - 1))
    max_sum = 0
    for i in range(len(data)):
        index = 0
        sum = triangle[0][0]
        for j in range(len(triangle) - 1):
            index += data[i][j]
            sum += triangle[j + 1][index]
        max_sum = max(max_sum, sum)
    return max_sum


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
