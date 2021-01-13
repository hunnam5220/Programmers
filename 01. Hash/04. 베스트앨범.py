from collections import Counter as cc

def solution(genres, plays):
    answer = []

    gen_list = list(cc(genres))
    dict_k = {}

    for x in gen_list:
        dict_k[x] = 0

    for x, y in zip(genres, plays):
        dict_k[x] += y

    tmp_dict = sorted(dict_k.items(), reverse=True, key=lambda dict_k: dict_k[1])

    dict_k= []
    for step in range(len(tmp_dict)):
        dict_k.append(tmp_dict[step][0])

    genre_music = []

    for leng in range(len(dict_k)):
        tmp = []
        for x, y in zip(range(len(genres)), range(len(plays))):
            if genres[x] == dict_k[leng]:
                tmp.append(plays[y])

        genre_music.append(tmp)

    for x in range(len(dict_k)):
        if len(genre_music[x]) >= 2:
            a = sorted(genre_music[x], reverse=True)
            for y in range(2):
                list_val = [i for i, value in enumerate(plays) if value == a[y]]
                if len(list_val) >= 2:
                    for k in list_val:
                        if k in answer:
                            continue

                        if genres[k] == dict_k[x]:
                            answer.append(k)
                            break
                else:
                    answer.append(plays.index(a[y]))
        else:
            answer.append(plays.index(genre_music[x][0]))

    return answer

genres = ['classic', 'pop', 'classic', 'classic', 'pop']
# genres = ['classic', 'pop', 'classic', 'classic', 'classic']
# genres = ['classic', 'pop', 'classic', 'pop', 'pop']

plays = [500, 600, 150, 800, 2500]
print(solution(genres=genres, plays=plays))

plays = [500, 600, 150, 150, 2500]
print(solution(genres=genres, plays=plays))

plays = [500, 600, 800, 800, 2500]
print(solution(genres=genres, plays=plays))

plays = [500, 600, 150, 800, 2500]
print(solution(genres=genres, plays=plays))

plays = [500, 500, 150, 800, 2500]
print(solution(genres=genres, plays=plays))