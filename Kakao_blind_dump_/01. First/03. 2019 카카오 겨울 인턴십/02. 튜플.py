def sep_tuple(s):
    txt = s.replace('{{', '{').replace('}}', '}')
    res = []
    tmp = []
    num = ''

    ans = []

    for k in range(len(txt)):
        if txt[k] == '{':
            num = ''

        if txt[k].isnumeric():
            num += txt[k]

        if txt[k] == ',' and txt[k + 1] != '{':
            tmp.append(int(num))
            num = ''

        if txt[k] == '}':
            if num != '':
                tmp.append(int(num))

            res.append(tmp)
            tmp = []

    res.sort(key=lambda x: len(x))
    for r in res:
        for j in r:
            if j not in ans:
                ans.append(j)
    return ans


def solution(s):
    answer = sep_tuple(s)
    return answer


# [2, 1, 3, 4]
# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))

# [2, 1, 3, 4]
# print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))

# [111, 20]
print(solution("{{20,111},{111}}"))

# [123]
print(solution("{{123}}"))

# 3, 2, 4, 1
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))