mv2 = [0, -1, -2]


def fill(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[y][x] == '#':
                continue

            if board[y][x] == 0:
                board[y][x] = '#'
            else:
                break


# 블럭 지우자
def rm_block(floor, board):
    for a, b in floor:
        if board[a][b] != '#':
            board[a][b] = 0

    fill(board)


# 블럭 검사
def check_block(board, n, answer):
    rere = False
    # 맨 아래부터 검사
    for x in range(n - 1, -1, -1):
        for y in range(n - 1, -1, -1):
            # 맨 바닥을 긁어 세칸인지 두칸인지 검사
            floor = []

            # 맨 바닥이 0이 아니고 '#'이 아니면
            if board[x][y] != 0 and board[x][y] != '#':
                # 위 검사에서 세칸 이상 안됐으면 우측을 검사
                # 현재 칸 x 기준 x ~ x + 2 까지 검사
                std = board[x][y]
                floor = []
                for k in mv2:
                    if -1 < y + k < n:
                        if board[x][y + k] == std:
                            floor.append((x, y + k))

            ht = 0
            tmp = []
            # 바닥의 수가 3칸이면
            if len(floor) == 3:
                # 위 아래로 2*3 여섯칸이 돠나요?
                for k in [-1, 1]:
                    if -1 < floor[0][0] + k < n:
                        for a, b in floor:
                            # 조건에 맞으면 tmp에 넣어라
                            if board[floor[0][0] + k][b] == '#':
                                tmp.append((floor[0][0] + k, b))
                                ht += 1

                            if board[floor[0][0] + k][b] == board[x][y]:
                                tmp.append((floor[0][0] + k, b))

            # 바닥 수 2
            elif len(floor) == 2:
                for k in [-1, -2]:
                    if -1 < floor[0][0] + k < n:
                        for a, b in floor:
                            # 검사 대상이 # 이면 추가
                            if board[floor[0][0] + k][b] == '#':
                                tmp.append((floor[0][0] + k, b))
                                ht += 1

                            if board[floor[0][0] + k][b] == board[x][y]:
                                tmp.append((floor[0][0] + k, b))

                if len(tmp) + len(floor) < 6:
                    tmp = []

            if ht == 2:
                floor.extend(tmp)

            # 블럭으로 추가한 블럭들이 6개라면 터트릴 수 있다
            if len(floor) == 6:
                rere = True
                rm_block(floor, board)
                answer += 1

    return rere, answer


def solution(board):
    answer = 0

    # 0으로 된 빈공간을 위부터 떨어지는 형시으로 #으로 채워놓고
    fill(board)

    while 1:
        # 검사해서 지우기
        r, answer = check_block(board, len(board), answer)
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

# 5
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 0, 7, 0, 0, 0, 0, 0, 0, 0],
                [4, 7, 7, 7, 0, 0, 0, 0, 0, 0], [4, 4, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 3, 0, 0, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
                [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))

# 0
board = [
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 2, 0],
    [1, 2, 2, 2]
]

print(solution(board))

# 1
board = [
    [2, 2, 0, 0],
    [1, 2, 0, 4],
    [1, 2, 0, 4],
    [1, 1, 4, 4]]

print(solution(board))