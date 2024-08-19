# 1833. 雪糕的最大数量
#
# 中等
# 相关标签 贪心 数组 排序
#
# 夏日炎炎，小男孩 Tony 想买一些雪糕消消暑。
# 商店中新到 n 支雪糕，用长度为 n 的数组 costs 表示雪糕的定价，其中 costs[i] 表示第 i 支雪糕的现金价格。
# Tony 一共有 coins 现金可以用于消费，他想要买尽可能多的雪糕。
#
# 注意：Tony 可以按任意顺序购买雪糕。
# 给你价格数组 costs 和现金量 coins，请你计算并返回 Tony 用 coins 现金能够买到的雪糕的最大数量。
#
# 你必须使用计数排序解决此问题。
#
# 输入：costs = [1,3,2,4,1], coins = 7
# 输出：4
# 解释：Tony 可以买下标为 0、1、2、4 的雪糕，总价为 1 + 3 + 2 + 1 = 7

# costs.length == n
# 1 <= n <= 105
# 1 <= costs[i] <= 105
# 1 <= coins <= 108

from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for i in range(len(costs)):
            if coins >= costs[i]:
                ans += 1
                coins -= costs[i]
        return ans

    # 使用计数排序
    def maxIceCreamV2(self, costs: List[int], coins: int) -> int:
        nums = [0] * 100001
        for i in range(len(costs)):
            nums[costs[i]] += 1

        ans = 0
        for i in range(len(nums)):
            if coins >= i and nums[i] > 0:
                count = min(nums[i], coins // i)
                ans += count
                coins -= count * i
        return ans


if __name__ == '__main__':
    print(Solution().maxIceCreamV2([1,3,2,4,1], 7))