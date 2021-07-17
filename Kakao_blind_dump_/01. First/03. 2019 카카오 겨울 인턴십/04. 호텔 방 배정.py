import sys
sys.setrecursionlimit(10**6)


def find_parent(parent, x):
    if x not in parent.keys():
        parent[x] = x + 1
        return x

    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def solution(k, room_number):
    answer = []

    parent = {}

    for room in room_number:
        answer.append(find_parent(parent, room))

    return answer


# 1,3,4,2,5,6
print(solution(10, [1, 3, 4, 1, 3, 1]))
print(solution(10, [1, 3, 1, 1]))