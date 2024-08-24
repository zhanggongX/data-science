# 给你两个字符串 s 和 t，每个字符串中的字符都不重复，且 t 是 s 的一个排列。
#
# 排列差 定义为 s 和 t 中每个字符在两个字符串中位置的绝对差值之和。
#
# 返回 s 和 t 之间的 排列差 。
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        char_dict = {i: [0,0] for i in range(26)}
        for i in range(len(s)):
            char_dict[ord(s[i])-ord('a')][0] = i
            char_dict[ord(t[i])-ord('a')][1] = i

        ans = 0
        for i in range(26):
            ans += abs(char_dict[i][0]-char_dict[i][1])

        return ans

if __name__ == '__main__':
    print(Solution().findPermutationDifference("abcde","edbac"))