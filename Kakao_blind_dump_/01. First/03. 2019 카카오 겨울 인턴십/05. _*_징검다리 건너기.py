# 이분법

def solution(stones, k):
    left, right = 1, 200000000

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for i in stones:
            if i - mid < 1:
                cnt += 1
            else:
                cnt = 0

            if cnt >= k:
                break

        if cnt >= k:
            right = mid - 1

        else:
            left = mid + 1

    return left


# 3
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
