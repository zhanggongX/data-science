def find_the_difference(s: str, t: str) -> str:
    for i in t:
        if t.count(i) - s.count(i) == 1:
            return i
    return ''


if __name__ == '__main__':
    result = find_the_difference('abc', 'abcd')
    print(result)
