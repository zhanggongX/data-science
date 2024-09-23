'''
1014. 最佳观光组合

中等

提示
给你一个正整数数组 values，其中 values[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的 距离 为 j - i。

一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去 它们两者之间的距离。

返回一对观光景点能取得的最高分。
'''

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxI = values[0]
        ans = 0
        for j in range(1, len(values)):
            ans = max(ans, maxI + values[j] - j)
            maxI = max(maxI, values[j] + j)
        return ans


if __name__ == '__main__':
    print(Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]))
