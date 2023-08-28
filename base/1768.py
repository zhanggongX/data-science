def merge_alternate(word1: str, word2: str) -> str:
    i, j, x, y = 0, 0, len(word1), len(word2)
    res = ""
    while i < x or j < y:
        if i < x:
            res += word1[i]
            i += 1
        if j < y:
            res += word2[j]
            j += 1
    return res


if __name__ == '__main__':
    result = merge_alternate('abc', 'pqr')
    print(result)
