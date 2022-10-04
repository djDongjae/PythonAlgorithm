from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))

def watch(x, y, direction):
    if direction == 0:
        while x>0:
            x-=1
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
        return False
    if direction == 1:
        while x<n:
            x+=1
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
        return False
    if direction == 2:
        while y>0:
            y-=1
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
        return False
    if direction == 3:
        while y<n:
            y+=1
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
        return False

def process():
    for x,y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

answer = True

for data in list(combinations(spaces, 3)):
    for x,y in data:
        board[x][y] = 'O'
    if process():
        answer = False
    else:
        answer = True
        break
    for x, y in data:
        board[x][y] = 'X'

if answer:
    print('YES')
else:
    print('NO')