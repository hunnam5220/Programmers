mv = [-2, -1, 0, 1, 2]


def rm_block(base, board, num):

    for a, b in base:
        idx = 0
        board[a][b] = '#'
        while 1:
            if a + idx >= len(board):
                break

            if board[a + idx][b] == num or board[a + idx][b] == 0:
                board[a + idx][b] = '#'
                idx += 1
            else:
                break


def check_block(board, block, n, answer):
    rere = False

    for num in block:
        for x in range(n - 1, -1, -1):
            for y in range(n):
                base = []
                if board[x][y] == num:
                    for k in mv:
                        if -1 < y + k < n and board[x][y + k] == num:
                            base.append((x, y + k))

                if len(base) < 2:
                    continue

                elif len(base) == 3:
                    tmp = []
                    for k in [-1, 1]:
                        if -1 < base[0][0] + k < n:
                            for a, b in base:
                                if board[base[0][0] + k][b] == '#' or board[base[0][0] + k][b] == num:
                                    tmp.append((base[0][0] + k, b))
                    base.extend(tmp)
                else:
                    tmp = []
                    for k in [-2, -1, 1, 2]:
                        if -1 < base[0][0] + k < n:
                            for a, b in base:
                                if board[base[0][0] + k][b] == '#' or board[base[0][0] + k][b] == num:
                                    tmp.append((base[0][0] + k, b))
                    base.extend(tmp)

                if len(base) == 6:
                    rere = True
                    rm_block(base, board, num)
                    answer += 1

    return rere, answer


def solution(board):
    answer = 0
    block = []
    for a in board:
        for b in a:
            if b != 0 and b not in block:
                block.append(b)

    block.sort()
    n = len(board)

    for x in range(n):
        for y in range(n):
            if board[y][x] == 0:
                board[y][x] = '#'

            elif board[y][x] == '#':
                continue

            else:
                break

    while 1:
        r, answer = check_block(board, block, n, answer)
        if not r:
            break

    return answer


# 2
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
                [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
                [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))

# 3
print(solution([[0, 2, 0, 0], [1, 2, 0, 4], [1, 2, 2, 4], [1, 1, 4, 4]]))

# 1
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 2, 0, 0, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))

# 2
print(solution([[0, 0, 0, 0, 0], [1, 0, 0, 2, 0], [1, 2, 2, 2, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]))

# 0
print(solution([[0, 0, 1, 1, 1], [0, 0, 0, 1, 0], [3, 0, 0, 2, 0], [3, 2, 2, 2, 0], [3, 3, 0, 0, 0]]))

# 1
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 2, 0, 0, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
