"""
2414. 最长的字母序连续子字符串的长度

中等

提示
字母序连续字符串 是由字母表中连续字母组成的字符串。换句话说，字符串 "abcdefghijklmnopqrstuvwxyz" 的任意子字符串都是 字母序连续字符串 。

例如，"abc" 是一个字母序连续字符串，而 "acb" 和 "za" 不是。
给你一个仅由小写英文字母组成的字符串 s ，返回其 最长 的 字母序连续子字符串 的长度。
"""


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 1
        cnt = 1

        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.longestContinuousSubstring("abacaba"))
    print(s.longestContinuousSubstring("abcde"))
