'''
2535. 数组元素和与数字和的绝对差
已解答
简单
相关标签
相关企业
提示
给你一个正整数数组 nums 。

元素和 是 nums 中的所有元素相加求和。
数字和 是 nums 中每一个元素的每一数位（重复数位需多次求和）相加求和。
返回 元素和 与 数字和 的绝对差。

注意：两个整数 x 和 y 的绝对差定义为 |x - y| 。
'''
from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        x = sum(nums)
        y = sum(int(i) for i in ''.join(str(i) for i in nums))
        return abs(x - y)


if __name__ == '__main__':
    nums = [1, 15, 6, 3]
    print(Solution().differenceOfSum(nums))
