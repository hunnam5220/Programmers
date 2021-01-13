import itertools as itt
import collections

def solution(clothes):
    # 풀이 공식
    '''(A 옷 가짓수 + 1)*(B 옷 가짓수 + 1) ... -1(안입는 경우의 수)'''

    t_cl = [clothes[x][1] for x in range(len(clothes))]
    numofcl = list(collections.Counter(t_cl).values())
    no_cl = len(list(itt.combinations(t_cl, 0)))

    if len(numofcl) == 1:
        return numofcl[0]
    else:
        result = 1
        for step in numofcl:
            result *= step + 1

        return result - no_cl


if __name__ == '__main__':


    clothes = [
        [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']],
        [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]
    ]

    print(solution(clothes=clothes[0]))
    print(solution(clothes=clothes[1]))