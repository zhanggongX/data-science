from typing import List


# 2576. 求出最多标记下标
# 中等

# 给你一个下标从 0 开始的整数数组 nums 。
#
# 一开始，所有下标都没有被标记。你可以执行以下操作任意次：
#
# 选择两个 互不相同且未标记 的下标 i 和 j ，满足 2 * nums[i] <= nums[j] ，标记下标 i 和 j 。
# 请你执行上述操作任意次，返回 nums 中最多可以标记的下标数目。

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        for j in range((n + 1) // 2, n):
            if nums[i] * 2 <= nums[j]:
                i += 1
        return i * 2


if __name__ == '__main__':
    s = Solution()
    print(s.maxNumOfMarkedIndices([42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40]))
