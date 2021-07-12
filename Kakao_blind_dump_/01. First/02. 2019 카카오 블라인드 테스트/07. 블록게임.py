mv1 = [-2, -1, 0]
mv2 = [0, 1, 2]


def fill(n, board):
    for x in range(n):
        for y in range(n):
            if board[y][x] == 0:
                board[y][x] = '#'

            elif board[y][x] == '#':
                continue

            else:
                break


# 블럭 지우자
def rm_block(floor, board):
    for a, b in floor:
        if board[a][b] != '#':
            board[a][b] = 0

    fill(len(board), board)


# 블럭 검사
def check_block(board, n, answer):
    rere = False
    ht = 0
    # 맨 아래부터 검사
    for x in range(n - 1, -1, -1):
        for y in range(n):
            # 맨 바닥을 긁어 세칸인지 두칸인지 검사
            floor = []

            # 맨 바닥이 0이 아니고 '#'이 아니면
            if board[x][y] != 0 and board[x][y] != '#':
                cnt = 0
                # 현재 칸 x 기준 x-2 ~ x 까지 검사
                for k in mv1:
                    if -1 < y + k < n and board[x][y + k] == board[x][y]:
                        floor.append((x, y + k))
                        cnt += 1

                # 위 검사에서 세칸 이상 안됐으면 우측을 검사
                # 현재 칸 x 기준 x ~ x + 2 까지 검사
                if cnt < 2:
                    cnt = 0
                    floor = []
                    for k in mv2:
                        if -1 < y + k < n and board[x][y + k] == board[x][y]:
                            floor.append((x, y + k))
                            cnt += 1

            # 바닥의 수가 2칸 미만이면 어차피 못깨뜨림
            if len(floor) < 2:
                continue

            # 바닥의 수가 3칸이면
            if len(floor) == 3:
                tmp = []
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
            else:
                tmp = []
                for k in [-2, -1, 1, 2]:
                    if -1 < floor[0][0] + k < n:
                        for a, b in floor:
                            if board[floor[0][0] + k][b] == '#':
                                tmp.append((floor[0][0] + k, b))
                                ht += 1

                            if board[floor[0][0] + k][b] == board[x][y]:
                                tmp.append((floor[0][0] + k, b))

            floor.extend(tmp)

            if len(floor) == 6:
                rere = True
                rm_block(floor, board)
                answer += 1

    return rere, answer


def solution(board):
    answer = 0
    n = len(board)

    # 0으로 된 빈공간을 위부터 떨어지는 형시으로 #으로 채워놓고
    fill(n, board)

    while 1:
        # 검사해서 지우기
        r, answer = check_block(board, n, answer)
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
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[4, 0, 7, 0, 0, 0, 0, 0, 0, 0],[4, 7, 7, 7, 0, 0, 0, 0, 0, 0],[4, 4, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 3, 0, 0, 0, 0, 0],[0, 0, 0, 2, 3, 0, 0, 0, 5, 5],[1, 2, 2, 2, 3, 3, 0, 0, 0, 5],[1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))
