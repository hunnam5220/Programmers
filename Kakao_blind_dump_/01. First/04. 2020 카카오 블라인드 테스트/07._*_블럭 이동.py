from collections import deque

dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]


# 여기 조심해야 함
def get_next_pos(pos, new_board):
    next_pos = []
    pos = list(pos)
    pos_x1, pos_y1, pos_x2, pos_y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    for i in range(4):
        n_pos_x1, n_pos_y1, n_pos_x2, n_pos_y2 = pos_x1 + dx[i], pos_y1 + dy[i], pos_x2 + dx[i], pos_y2 + dy[i]
        if new_board[n_pos_x1][n_pos_y1] == 0 and new_board[n_pos_x2][n_pos_y2] == 0:
            next_pos.append({(n_pos_x1, n_pos_y1), (n_pos_x2, n_pos_y2)})

    if pos_x1 == pos_x2:
        for i in [-1, 1]:
            if new_board[pos_x1 + i][pos_y1] == 0 and new_board[pos_x2 + i][pos_y2] == 0:
                next_pos.append({(pos_x1, pos_y1), (pos_x1 + i, pos_y1)})
                next_pos.append({(pos_x2, pos_y2), (pos_x2 + i, pos_y2)})

    if pos_y1 == pos_y2:
        for i in [-1, 1]:
            if new_board[pos_x1][pos_y1 + i] == 0 and new_board[pos_x2][pos_y2 + i] == 0:
                next_pos.append({(pos_x1, pos_y1), (pos_x1, pos_y1 + i)})
                next_pos.append({(pos_x2, pos_y2), (pos_x2, pos_y2 + i)})

    return next_pos


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]

    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    pos = {(1, 1), (1, 2)}
    q = deque()
    visited = [pos]
    cost = 0
    q.append((pos, cost))

    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost

        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)


# 7
print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))