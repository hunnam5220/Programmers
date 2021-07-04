from collections import deque


def solution(msg):
    answer = []

    base_dict = {}
    for i in range(97, 123):
        base_dict[chr(i).upper()] = i - 96

    dict_idx = 27
    q = deque()
    q.extend(list(msg))
    start = 0
    m_len = 1

    while q:
        b = False
        for i in range(m_len, 1, -1):
            if msg[start: start + i] in base_dict and len(msg[start: start + 2]) != 1:
                answer.append(base_dict[msg[start: start + i]])
                base_dict[msg[start: start + i + 1]] = dict_idx
                dict_idx += 1
                m_len += 1
                for i in range(len(msg[start: start + i])):
                    if q:
                        q.popleft()
                    start += 1
                b = True

                if b:
                    break

        else:
            now = q.popleft()
            answer.append(base_dict[now])
            base_dict[msg[start: start + 2]] = dict_idx
            dict_idx += 1
            start += 1
            m_len = max(len(msg[start: start + 2]), m_len)

    return answer





# [11, 1, 27, 15]
print(solution("KAKAO"))

# [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(solution("TOBEORNOTTOBEORTOBEORNOT"))

# [1, 2, 27, 29, 28, 31, 30]
print(solution("ABABABABABABABAB"))