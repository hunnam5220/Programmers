def get_idx(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            return i

    return cnt


def check_u(s):
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1

        else:
            if cnt == 0:
                return False
            cnt -= 1

    return True



def solution(p):
    answer = ''
    if p == '':
        return answer

    i = get_idx(p)
    u, v = p[:i + 1], p[i + 1:]

    if check_u(u):
        answer = u + solution(v)

    else:

        answer = '('
        answer += solution(v)
        answer += ')'

        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += ''.join(u)

    return answer


# "(()())()"
# print(solution("(()())()"))

# "()"
print(solution(")("))

# "()(())()"
print(solution("()))((()"))
