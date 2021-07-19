"겉에 두르는게 아니라 세배였음 ㅋㅋ 씨발"


def turn_key(l, key):
    new_key = [item[:] for item in key]

    for i in range(l):
        for j in range(l):
            new_key[i][j] = key[l - (j + 1)][i]

    return new_key


def check(lock, lock_l):
    for i in range(lock_l):
        for j in range(lock_l):
            if lock[i + lock_l][j + lock_l] != 1:
                return False
    return True


def solution(key, lock):
    key_l = len(key)
    lock_l = len(lock)
    new_lock = [[0] * (lock_l * 3) for _ in range(lock_l * 3)]

    new_len = len(new_lock)

    for i in range(lock_l):
        for j in range(lock_l):
            new_lock[i + lock_l][j + lock_l] = lock[i][j]

    for i in range(4):
        key = turn_key(key_l, key)

        for i in range(new_len - key_l):
            for j in range(new_len - key_l):

                for k in range(key_l):
                    for p in range(key_l):
                        new_lock[i + k][j + p] += key[k][p]

                if check(new_lock, lock_l):
                    return True

                else:
                    for k in range(key_l):
                        for p in range(key_l):
                            new_lock[i + k][j + p] -= key[k][p]

    return False


# true
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))
