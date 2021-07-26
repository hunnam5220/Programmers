from collections import deque


def bfs(idx, nodes, keypad):
    q = deque()
    q.append((idx, 0))
    visited = [(idx, idx)]

    while q:
        n, cost = q.popleft()
        for node in nodes[n]:
            if (idx, node) not in visited:
                keypad[idx][node] = cost + 1
                keypad[node][idx] = cost + 1
                q.append((node, cost + 1))
                visited.append((idx, node))


def solution(numbers, hand):
    answer = ''
    keypad = [[-1] * 12 for _ in range(12)]

    for i in range(12):
        for j in range(12):
            if i == j:
                keypad[i][j] = 0

    nodes = [[8, 10, 11], [2, 4], [1, 3, 5], [2, 6], [1, 5, 7], [2, 4, 6, 8],
             [3, 5, 9], [10, 4, 8], [0, 5, 7, 8], [11, 6, 8], [0, 7], [0, 9]]

    for i in range(12):
        bfs(i, nodes, keypad)
    r, l = 10, 11
    mustl = [1, 4, 7]
    mustr = [3, 6, 9]

    for i in numbers:
        if i in mustr:
            r = i
            answer += 'R'
            continue

        if i in mustl:
            l = i
            answer += 'L'
            continue

        if keypad[r][i] == keypad[l][i]:
            if hand == 'right':
                r = i
                answer += 'R'
                continue

            if hand == 'left':
                l = i
                answer += 'L'
                continue

        elif keypad[r][i] > keypad[l][i]:
            l = i
            answer += 'L'

        else:
            r = i
            answer += 'R'


    return answer


"LRLLLRLLRRL"
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
