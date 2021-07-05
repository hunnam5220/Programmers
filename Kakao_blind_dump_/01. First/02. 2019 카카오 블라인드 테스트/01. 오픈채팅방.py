def solution(record):
    result = []
    answer = []
    status = ["님이 들어왔습니다.", "님이 나갔습니다."]
    id_code = {}

    for r in record:
        l = r.split()

        if l[0] == 'Enter':
            id_code[l[1]] = l[2]
            result.append([0, l[1]])

        elif l[0] == 'Leave':
            result.append([1, l[1]])

        else:
            id_code[l[1]] = l[2]

    for s, uid in result:
        answer.append(id_code[uid] + status[s])

    return answer


print(solution(
    ["Enter uid1234 Muzi",  "Leave uid1234", "Enter uid4567 Prodo", "Enter uid1234 Ryan", "Change uid4567 Prodo"]))
