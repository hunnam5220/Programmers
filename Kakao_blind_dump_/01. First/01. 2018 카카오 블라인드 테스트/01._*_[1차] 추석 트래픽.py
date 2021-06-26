def get_value(start, times):
    res = 0
    end = start + 1000 - 1
    for time in times:
        if start <= time[1] and end >= time[0]:
            res += 1
    return res


def solution(lines):
    times = []

    answer = 0

    for t in lines:
        arr = t.split()
        tmp = list(map(float, arr[1].split(':')))
        complete_time = tmp[0] * 3600 * 1000 + tmp[1] * 60 * 1000 + tmp[2] * 1000
        start_time = complete_time - (float(arr[2][:-1]) * 1000) + 1
        times.append((start_time, complete_time))

    for time in times:
        start, end = time
        answer = max(get_value(start, times), answer)
        answer = max(get_value(end, times), answer)

    return answer


print(solution([
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))

print(solution([
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))

print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]))