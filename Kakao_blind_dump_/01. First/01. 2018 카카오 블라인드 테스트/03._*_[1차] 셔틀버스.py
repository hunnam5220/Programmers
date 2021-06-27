def solution(n, t, m, timetable):
    # 시간을 분단위로 변경 예) 10:00 => 600

    # int(time[:2]) == 시
    # int(time[3:5]) == 분
    timetable = [int(time[:2]) * 60 + int(time[3:5]) for time in timetable]

    # timetable을 정렬
    timetable.sort()

    # 마지막 배차의 시간표 (분단위)
    last_time = (60 * 9) + (n - 1) * t

    # 배차 횟수만큼 반복
    for i in range(n):

        # timetable의 길이가 태울 수 있는 인원보다 적으면
        if len(timetable) < m:
            return '%02d:%02d' % (last_time // 60, last_time % 60)

        # 마지막 배차일 경우
        if i == n - 1:

            # timetable에 마지막 배차 때 우선순위가 높은 크루가 있다면
            if timetable[0] <= last_time:

                # 마지막 탑승자보다 1초 빠르게 한다
                last_time = timetable[m - 1] - 1

            return '%02d:%02d' % (last_time // 60, last_time % 60)

        # del로 인한 index 변화에 영향을 주지 않기위해서 거꾸로 반복
        for j in range(m - 1, -1, -1):

            # 다음 배차 시간 (분단위)
            bus_arrive = (60 * 9) + i * t

            # 다음 배차시간보다 작거나 같은 시간을 가진 timetable 요소를 삭제
            if timetable[j] <= bus_arrive:

                # timetable에서 다음 배차를 못하는 크루를 삭제
                del timetable[j]


# "09:00"
print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))

# "09:09"
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))

# "08:59"
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))

# "00:00"
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))

# "09:00"
print(solution(1, 1, 1, ["23:59"]))

# "18:00"
print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
