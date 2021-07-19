def check(answer):
    for x, y, a in answer:
        if a:
            # 보
            """보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다."""
            if y != 0 and([x + 1, y - 1, 0] in answer or [x, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)):
                continue
            else:
                return False
        else:
            # 기둥
            """기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다."""
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, a, b = frame

        if b:
            # install
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])
        else:
            # remove
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])

    return sorted(answer)


# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))

# [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
