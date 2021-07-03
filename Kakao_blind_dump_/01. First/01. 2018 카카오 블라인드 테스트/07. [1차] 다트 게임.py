def get_calc(s):
    s = s.replace("S", "")
    s = s.replace("D", "**2")
    s = s.replace("T", "**3")

    if len(s) > 1:
        return eval(s)
    else:
        return int(s)


def solution(dartResult):
    answer = []
    stack = ''
    idx = 0

    for i in dartResult:
        if stack != '' and i.isdigit() and not stack[-1].isnumeric():
            answer.append(get_calc(stack))
            stack = '' + i

        elif i.isdigit():
            stack += i

        elif chr(96) < i.lower() < chr(123):
            stack += i

        elif i == '*':
            answer.append(get_calc(stack))
            for i in range(2):
                if idx - i < 0:
                    break
                answer[idx - i] *= 2

            stack = ''
            idx += 1

        elif i == '#':
            answer.append(get_calc(stack) * -1)
            stack = ''

        else:
            stack += i
            answer.append(get_calc(stack))
            idx += 1
            stack = ''

        idx = len(answer)

    if stack != '':
        answer.append(get_calc(stack))

    return sum(answer)


# 37
print(solution("1S2D*3T"))

# 9
print(solution("1D2S#10S"))

# 3
print(solution("1D2S0T"))

# 23
print(solution("1S*2T*3S"))

# 5
print(solution("1D#2S*3S"))

# -4
print(solution("1T2D3D#"))

# 59
print(solution("1D2S3T*"))
