import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

if __name__ == '__main__':
    participant = [
        ['leo', 'kiki', 'eden'],
        ['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
        ['mislav', 'stanko', 'mislav', 'ana']
    ]

    completion = [
        ['eden', 'kiki'],
        ['josipa', 'filipa', 'marina', 'nikola'],
        ['stanko', 'ana', 'mislav']
    ]

    print(solution(participant[0], completion[0]))
    print(solution(participant[1], completion[1]))
    print(solution(participant[2], completion[2]))