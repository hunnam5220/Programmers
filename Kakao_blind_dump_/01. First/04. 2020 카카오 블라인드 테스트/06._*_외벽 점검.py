from itertools import permutations


def solution(n, weak, dist):
    answer = 1e9
    l = len(weak)
    new_weak = weak
    new_weak.extend([n + k for k in weak])
    new_weak.sort()

    for start in range(l):
        for f in permutations(dist, len(dist)):
            cnt = 1

            pos = weak[start] + f[cnt - 1]

            for idx in range(start, start + l):
                if pos < weak[idx]:
                    cnt += 1

                    if cnt > len(dist):
                        break

                    pos = weak[idx] + f[cnt - 1]
            answer = min(answer, cnt)

    if answer > len(dist):
        return -1
    return answer


# 2
print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))

# -1
print(solution(12, [1, 5, 6, 10], [1, 1]))

# 1
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
