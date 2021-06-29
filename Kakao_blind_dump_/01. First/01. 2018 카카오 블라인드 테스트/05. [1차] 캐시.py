from collections import deque


def solution(cacheSize, cities):
    cache = []
    answer = 0
    LRU = {
    }
    for i in cities:
        i = i.lower()

        if i not in LRU:
            LRU[i] = 0

        if cacheSize != 0:
            if i not in cache:
                cache.append(i)
                answer += 5
            else:
                LRU[i] += 1
                answer += 1

            if len(cache) > cacheSize:
                rm = min(LRU)
                cache.remove(rm)
                LRU.pop(rm)
        else:
            answer += 5

    return answer


# 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

# 21
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))

# 60
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))

# 52
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))

# 16
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))

# 25
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

# 12
print(solution(2, ["Jeju", "Jeju", "Seoul", "Jeju"]))