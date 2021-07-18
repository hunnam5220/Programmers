def solution(s):
    k = len(s)
    answer = k

    for idx in range(1, k + 1):
        std = ''
        checker = s[0: idx]
        std += checker
        start, end = 0, idx

        cnt = 1

        for i in range(idx, k + 1, idx):
            if i == k:
                if cnt <= 1:
                    break
                else:
                    std += str(cnt)
                break

            if checker == s[start + i:end + i]:
                cnt += 1

            elif cnt <= 1:
                std += s[start + i:end + i]
                checker = s[start + i:end + i]
                continue

            else:
                std += str(cnt)
                cnt = 1
                std += s[start + i:end + i]
                checker = s[start + i:end + i]

        answer = min(answer, len(std))

    return answer


# 7
print(solution("aabbaccc"))

# 9
print(solution("ababcdcdababcdcd"))

# 8
print(solution("abcabcdede"))

# 14
print(solution("abcabcabcabcdededededede"))

# 17
print(solution("xababcdcdababcdcd"))