def solution(phoneBook):
    phoneBook.sort()

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

if __name__ == '__main__':

    phoneBook = [
        ['119', '97674223', '1195524421'],
        ['123', '456', '789'],
        ['12', '123', '1235', '567', '88']
    ]

    print(solution(phoneBook=phoneBook[0]))
    print(solution(phoneBook=phoneBook[1]))
    print(solution(phoneBook=phoneBook[2]))