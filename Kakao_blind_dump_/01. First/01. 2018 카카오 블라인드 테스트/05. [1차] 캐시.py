import heapq


def solution(cacheSize, cities):
    answer = 0

    lru = {}

    for city in cities:
        city = city.lower()
        isin = False
        while lru:
            s, c = heapq.heappop(lru)
            if c == city:
                isin = True
                heapq.heappush(lru, (s + 1, c))
                break

        if not isin:
            heapq.heappush(lru, [0, city])
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