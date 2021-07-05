def solution(record):
    answer, idx = [], 0
    status = ["님이 들어왔습니다.", "님이 나갔습니다."]
    visited = {}
    id_code = {}
    for r in record:
        r = r.split()

        if r[0] == 'Enter':
            if r[1] in visited:

                for i in visited[r[1]]:
                    i = int(i)
                    answer[i] = r[2] + "님이" + answer[i].split("님이")[1]

                id_code[r[1]] = r[2]
                visited[r[1]] += str(idx)
                answer.append(r[2] + status[0])
                idx += 1

            else:
                visited[r[1]] = ''
                visited[r[1]] += str(idx)

                id_code[r[1]] = r[2]

                answer.append(r[2] + status[0])
                idx += 1

        elif r[0] == 'Leave':
            answer.append(id_code[r[1]] + status[1])
            visited[r[1]] += str(idx)
            idx += 1

        elif r[0] == 'Change':
            for i in visited[r[1]]:
                j = int(i)
                answer[j] = r[2] + "님이" + answer[j].split("님이")[1]
                id_code[r[1]] = r[2]

    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
