def solution(files):
    answer = []
    arr = []
    n = len(files)

    modes = [0, 1, 2]
    j = 1

    for file in files:
        idx, s, tmp,  = 0, '', []
        for f in file:
            p = False
            if modes[idx] == 0 and not f.isnumeric():
                s += f.lower()
                p = True

            elif modes[idx] == 1 and f.isnumeric():
                s += f
                p = True

            elif modes[idx] == 2:
                s += f
                p = True

            if not p:
                if modes[idx] == 1:
                    z = 0
                    for l in range(len(s)):
                        if int(s[l]) != 0:
                            z = l
                            break

                    s = int(s[z:])
                idx += 1
                tmp.append(s)
                s = f

        if len(tmp) + 3 < 5:
            if modes[idx] == 1:
                z = 0
                for l in range(len(s)):
                    if int(s[l]) != 0:
                        z = l
                        break

                s = int(s[z:])
            idx += 1
            tmp.append(s)
            s = ''

        tmp.extend([s, j, file])
        arr.append(tmp)
        j += 1

    print()
    arr.sort(key=lambda x: (x[0], x[1], x[3]))

    for i in range(n):
        answer.append(arr[i][-1])

    return answer


# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print(solution(["img000000012", "img10.png", "img00002.png", "img1.png", "IMG01.GIF", "img2.JPG"]))

# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
