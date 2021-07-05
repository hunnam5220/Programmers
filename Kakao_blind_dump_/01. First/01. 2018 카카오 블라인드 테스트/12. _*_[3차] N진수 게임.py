def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def solution(n, t, m, p):
    answer = ''
    numbers = ''
    idx = p - 1
    i = 0

    while len(numbers) < t * m * p:
        numbers += convert(i, n)
        i += 1

    for _ in range(t):
        answer += numbers[idx]
        idx += m

    return answer


print(solution(11, 5, 4, 1))
print(solution(12, 5, 4, 1))
print(solution(13, 5, 4, 1))
print(solution(14, 5, 4, 1))
print(solution(15, 5, 4, 1))
print(solution(16, 5, 4, 1))
