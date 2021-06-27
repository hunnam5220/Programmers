def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    n = len(str1)
    m = len(str2)

    s1_list = []
    s2_list = []

    for i in range(n - 1):
        chk = True
        for k in str1[i:i + 2]:
            if 64 > ord(k) or ord(k) > 91:
                chk = False

        if chk:
            s1_list.append(str1[i:i + 2])

    for j in range(m - 1):
        chk = True
        for k in str2[j:j + 2]:
            if 64 > ord(k) or ord(k) > 91:
                chk = False

        if chk:
            s2_list.append(str2[j:j + 2])

    if s1_list in s2_list:
        gyo_val = len(s1_list)
        h_len = len(s2_list)

    elif s2_list in s1_list:
        gyo_val = len(s2_list)
        h_len = len(s1_list)

    elif n >= m:
        h_len = len(s2_list)
        gyo_val = 0

        for i in s1_list:
            if i not in s2_list:
                h_len += 1

            elif i in s2_list:
                gyo_val += 1

    else:
        h_len = len(s1_list)
        gyo_val = 0

        for i in s2_list:
            if i not in s1_list:
                h_len += 1

            elif i in s1_list:
                gyo_val += 1

    if gyo_val == 0 and h_len == 0:
        return 65536

    return int((gyo_val / h_len) * 65536)


# 16384
# print(solution("FRANCE", "french"))

# 65536
# print(solution("handshake", "shake hands"))

# 43690
# print(solution("aa1+aa2", "AAAA12"))

# 65536
# print(solution("E=M*C^2", "e=m*c^2"))

# 0
# print(solution("AACCC", "A A A A A C C C C"))

# 7281
# print(solution("ABDDD", "DDEFGHH"))

# 13107
print(solution("AAbbaa_AA", "BBB"))