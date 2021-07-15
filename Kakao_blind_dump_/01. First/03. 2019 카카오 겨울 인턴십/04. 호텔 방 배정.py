def solution(k, room_number):
    answer = []

    # 부모 노드 정하는 리스트
    # 초기화는 자기 자신으로 초기화
    parent = [x for x in range(k + 2)]

    # 방이 비었는지 체크할 수 있게 0은 비었음 -1은 안비었음
    room = [0 for _ in parent]

    # 손님이 요구하는 방 번호를 하나씩 가져옴
    for i in room_number:

        # 손님이 요구하는 방번호가 비어있는 방이면?
        if room[i] == 0:
            # 방 배정
            answer.append(i)

            # 배정한 방 번호의 부모노드를 다음 방 번호로
            parent[i] = i + 1

            # 더 이상 빈 방이 아님
            room[i] = -1

        # 방이 찼네?
        else:

            # 방문했던 노드를 담을 리스트
            visited = [i]

            # 반복
            while 1:
                # 가려고 했던 방의 부모노드로 가서 방이 비었는지 확인

                # 비었네?
                if room[parent[i]] == 0:

                    # 이제 이 방은 비어있지 않음
                    room[parent[i]] = -1

                    # 배정됐으니 넣어주고
                    answer.append(parent[i])

                    # 배정된 방의 부모노드를 다음 방 번호로 변경
                    parent[parent[i]] = parent[i] + 1

                    # 방문했던 노드들도 배정된 방의 부모노드를 다음 방 번호로 변경
                    # 중복이 있으면 더 길어지니까 set으로 중복제거 후 리스트 변환
                    if list(set(visited)):
                        for j in visited:
                            parent[j] = parent[parent[i]]

                    # 멈춰!
                    break

                # 안비었네?
                else:
                    # 방문했던 노드에 기록
                    visited.append(i)

                    # 부모노드 번호로 변경
                    i = parent[i]

    return answer


# 1,3,4,2,5,6
print(solution(10, [1, 3, 4, 1, 3, 1]))
print(solution(10, [1, 3, 1, 1]))