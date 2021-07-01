from collections import deque


def solution(cacheSize, cities):
    answer = 0
    buffer = deque()

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()

        if city in buffer:
            answer += 1
            buffer.remove(city)

        else:
            answer += 5

        buffer.append(city)

        if len(buffer) > cacheSize:
            buffer.popleft()

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