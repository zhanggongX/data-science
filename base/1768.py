class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j, x, y = 0, 0, len(word1), len(word2)
        res = ''
        while i < x or j < y:
            if i < x:
                res += word1[i]
                i += 1
            if j < y:
                res += word2[j]
                j += 1
        return res


if __name__ == '__main__':
    result = Solution.mergeAlternately(self='1768,'abc', 'pqr')
    print(result)
