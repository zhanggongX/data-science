from bisect import bisect, bisect_right, bisect_left
from collections import defaultdict
from typing import List

"""
2024. 考试的最大困扰度

中等

提示
一位老师正在出一场由 n 道判断题构成的考试，每道题的答案为 true （用 'T' 表示）或者 false （用 'F' 表示）。老师想增加学生对自己做出答案的不确定性，方法是 最大化 有 连续相同 结果的题数。（也就是连续出现 true 或者连续出现 false）。

给你一个字符串 answerKey ，其中 answerKey[i] 是第 i 个问题的正确结果。除此以外，还给你一个整数 k ，表示你能进行以下操作的最多次数：

每次操作中，将问题的正确答案改为 'T' 或者 'F' （也就是将 answerKey[i] 改为 'T' 或者 'F' ）。
请你返回在不超过 k 次操作的情况下，最大 连续 'T' 或者 'F' 的数目。

"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_t = self.calc_char(answerKey, k, 'T')
        max_f = self.calc_char(answerKey, k, 'F')
        return max(max_t, max_f)

    def calc_char(self, answerKey: str, k: int, ch: str) -> int:
        n = len(answerKey)
        res = 0

        l = 0
        r = 0
        sum = 0

        while r < n:
            if answerKey[r] != ch:
                sum += 1
            while sum > k:
                if answerKey[l] != ch:
                    sum -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1

        return res


if __name__ == '__main__':
    print(Solution().maxConsecutiveAnswers(answerKey="TTFF", k=2))
    print(Solution().maxConsecutiveAnswers(answerKey="TFFT", k=1))
    print(Solution().maxConsecutiveAnswers(answerKey="TTFTTFTT", k=1))
