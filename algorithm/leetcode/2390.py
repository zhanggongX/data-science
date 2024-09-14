"""
2390. 从字符串中移除星号

中等

提示
给你一个包含若干星号 * 的字符串 s 。

在一步操作中，你可以：
选中 s 中的一个星号。
移除星号 左侧 最近的那个 非星号 字符，并移除该星号自身。
返回移除 所有 星号之后的字符串。

注意：
生成的输入保证总是可以执行题面中描述的操作。
可以证明结果字符串是唯一的。
"""


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == '*' and stack:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.removeStars("leet**cod*e"))
