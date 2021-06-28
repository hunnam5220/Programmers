# 블럭 내리기
def down_block(visited, board):
    for crashed in visited:
        a, b = crashed
        board[a][b] = 0

    m, n = len(board), len(board[0])

    for i in range(m - 1, -1, -1):
        for j in range(n):
            if board[i][j] == 0:
                chaneged = False
                for k in range(i - 1, -1, -1):
                    if board[k][j] != 0:
                        board[i][j], board[k][j] = board[k][j], board[i][j]
                        chaneged = True

                    if chaneged:
                        break


# 주변 블럭 탐색
def find_2x2(x, y, board):
    if board[x][y] == 0:
        return

    crash_blocks = [[False] * 2 for _ in range(2)]

    for i in range(2):
        for j in [0, 1]:
            if board[x][y] == board[i + x][y + j]:
                crash_blocks[i][j] = (i + x, y + j)

    for i in crash_blocks:
        if False in i:
            return

    res = set()
    for i in crash_blocks:
        res |= set(i)

    return res


def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])

    visited = set()

    answer = 0

    ag = False

    while 1:
        # 1 for문으로 블럭 하나씩 다 돌기
        for a in range(m - 1):
            for b in range(n - 1):
                f = find_2x2(a, b, board)
                if f is not None:
                    visited |= f
                    ag = True

        if ag:
            # 2 블럭 내리기
            down_block(visited, board)
            ag = False
            answer += len(visited)
            visited = set()

        else:
            return answer


# 14
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))

# 15
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

# 4
print(solution(7, 2, ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]))

# 32
print(solution(6, 6, ['AABBEE', 'AAAEEE', 'VAAEEV', 'AABBEE', 'AACCEE', 'VVCCEE']))

# 12
print(solution(6, 2, ["DD", "CC", "AA", "AA", "CC", "DD"]))

# 8
print(solution(8, 2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"]))
