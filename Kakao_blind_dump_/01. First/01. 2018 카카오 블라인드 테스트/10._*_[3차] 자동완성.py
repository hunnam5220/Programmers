def solution(words):
    words.sort()
    trie = {}

    for word in words:
        cur_trie = trie
        for w in word:
            cur_trie.setdefault(w, [0, {}])
            cur_trie[w][0] += 1
            cur_trie = cur_trie[w][1]

    result = 0
    for word in words:
        cur_trie = trie
        for i in range(len(word)):
            if cur_trie[word[i]][0] == 1:
                break
            cur_trie = cur_trie[word[i]][1]
        result += 1 + i

    return result


# 7
print(solution(["go", "gone", "guild"]))

# 4
print(solution(["abc", "def", "ghi", "jklm"]))

# 15
print(solution(["word", "war", "warrior", "world"]))
