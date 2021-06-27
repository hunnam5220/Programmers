def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    n = len(str1)
    m = len(str2)

    s1_list, s2_list = [], []

    for i in range(n - 1):
        if str1[i:i + 2].isalpha():
            s1_list.append(str1[i:i + 2])

    for j in range(m - 1):
        if str2[j:j + 2].isalpha():
            s2_list.append(str2[j:j + 2])

    total = len(s1_list) + len(s2_list)
    intersect = 0
    if total == 0:
        return 65536

    for i in s2_list:
        if i in s1_list:
            intersect += 1
            s1_list.remove(i)

    return int((intersect / (total - intersect)) * 65536)


# 16384
print(solution("FRANCE", "french"))

# 65536
print(solution("handshake", "shake hands"))

# 43690
print(solution("aa1+aa2", "AAAA12"))

# 65536
print(solution("E=M*C^2", "e=m*c^2"))

# 0
print(solution("AACCC", "A A A A A C C C C"))

# 7281
print(solution("ABDDD", "DDEFGHH"))