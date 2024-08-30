'''
3153. 所有数对中数位不同之和
中等

提示
你有一个数组 nums ，它只包含 正 整数，所有正整数的数位长度都 相同 。
两个整数的 数位不同 指的是两个整数 相同 位置上不同数字的数目。
请你返回 nums 中 所有 整数对里，数位不同之和。
'''
from typing import List


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        res = 0
        digit_dict = [[0] * 10 for _ in range(10)]

        for i, num in enumerate(nums):
            did = 0
            while num > 0:
                digit = num % 10
                res += i - digit_dict[did][digit]
                digit_dict[did][digit] += 1
                did += 1
                num //= 10
        return res


if __name__ == '__main__':
    print(Solution().sumDigitDifferences([13, 23, 12]))
