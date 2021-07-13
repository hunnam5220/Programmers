def boom(stack):
    res = []
    while 1:
        chk = False
        for i in range(len(stack) - 1, 0, -1):
            rm_set = [i]
            for j in range(i - 1, -1 , -1):
                if stack[i] != stack[j]:
                    break
                else:
                    rm_set.append(j)
                    chk = True

            if chk:
                for r in rm_set:
                    stack.pop(r)
                res.extend(rm_set)

                break

        if not chk:
            return len(res)


def solution(board, moves):
    answer = 0
    n = len(board)
    stack= []

    for mv in moves:
        chk = False
        for i in range(n):
            if board[i][mv - 1] != 0:
                if board[i][mv - 1] in stack:
                    chk = True

                stack.append(board[i][mv - 1])
                board[i][mv - 1] = 0
                if chk:
                    answer += boom(stack)

                break

    return answer


# 4
print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))