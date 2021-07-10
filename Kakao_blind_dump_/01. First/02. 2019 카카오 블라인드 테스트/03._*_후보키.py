from itertools import combinations


def solution(relation):
    col = len(relation[0])
    row = len(relation)

    candidates = []

    # 전체 경우의 수
    for i in range(1, col + 1):
        # 1개 ~ N개 의 컬럼 수에 대한 경우의 수
        candidates.extend(combinations(range(col), i))

    # 유일성
    unique = []
    for candi in candidates:
        tmp = [tuple([item[i] for i in candi]) for item in relation]
        if len(set(tmp)) == row:
            unique.append(candi)

    # 최소성
    answer = set(unique)

    # 유일성이 확인된 경우의 수들의 개수만큼 반복
    for i in range(len(unique)):
        # 현재 유일성이 검증된 컬럼과 그 다음컬럼을 검사
        for j in range(i + 1, len(unique)):
            # 현재 유일성이 검증된 컬럼과 그 다음컬럼의 교집합이 현재 컬럼과 같으면 다음 컬럼을 삭제
            # set() & set() 교집합 구하는 방법
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                # answer list 에서 다음 컬럼 삭제
                # discard는 remove와는 다르게 에러가 안뜹니다
                answer.discard(unique[j])

    return len(answer)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
