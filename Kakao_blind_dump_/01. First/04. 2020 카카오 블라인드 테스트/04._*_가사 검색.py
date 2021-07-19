from bisect import bisect_left, bisect_right


def get_index(a, left, right):
    rid = bisect_right(a, right)
    lid = bisect_left(a, left)
    return rid - lid


def solution(words, queries):
    answer = []
    reverse_arr = [[] for _ in range(10001)]
    arr = [[] for _ in range(10001)]

    for w in words:
        arr[len(w)].append(w)
        reverse_arr[len(w)].append(w[::-1])

    for i in range(10001):
        arr[i].sort()
        reverse_arr[i].sort()

    for q in queries:
        if q[0] != '?':
            chk = get_index(arr[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            chk = get_index(reverse_arr[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(chk)

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
