from itertools import permutations


def check(ban, usr):
    for i in range(len(usr)):
        if len(ban[i]) != len(usr[i]):
            return False

        for j in range(len(usr[i])):
            if ban[i][j] == '*':
                continue

            if ban[i][j] != usr[i][j]:
                return False

    return True


def solution(user_id, banned_id):
    answer = []

    for usr in list(permutations(user_id, len(banned_id))):
        if check(banned_id, usr):
            usr = set(usr)
            if usr not in answer:
                answer.append(usr)

    return len(answer)


# 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))

# 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))

# 3
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
