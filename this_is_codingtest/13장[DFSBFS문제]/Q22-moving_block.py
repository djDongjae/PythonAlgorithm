#Q22[블록 이동하기] 355p
from collections import deque

def get_new_pos(pos, board):
    available_next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    #평행이동
    for i in range(4):
        new_pos1_x, new_pos1_y, new_pos2_x, new_pos2_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        if board[new_pos1_x][new_pos1_y] == 0 and [new_pos2_x][new_pos2_y] == 0:
            available_next_pos.append({(new_pos1_x, new_pos1_y), (new_pos2_x, new_pos2_y)})
    #가로 -> 세로 회전
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                available_next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                available_next_pos.append({(pos2_x + i, pos2_y), (pos2_x, pos2_y)})
    #세로 -> 가로 회전
    if pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                available_next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                available_next_pos.append({(pos2_x, pos2_y + i), (pos2_x, pos2_y)})
    return available_next_pos

def solution(board):
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_new_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)
    return 0