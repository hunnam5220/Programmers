import heapq


def solution(food_times, k):
    n = sum(food_times)
    m = len(food_times)
    if n <= k:
        return -1

    q = []
    for i in range(m):
        heapq.heappush(q, (food_times[i], i + 1))

    pre, now = 0, 0

    while (q[0][0] - pre) * m <= k:
        now, fnum = heapq.heappop(q)
        k -= ((now - pre) * m)
        m -= 1
        pre = now

    q.sort(key=lambda x: x[1])
    return q[k % m][1]


# 1
print(solution([3, 1, 2], 5))

# 3
print(solution([3, 1, 3, 1, 3], 6))

# 2
print(solution([3, 1, 3, 1, 3], 1))

# 3
print(solution([3, 1, 3, 1, 3], 9))
