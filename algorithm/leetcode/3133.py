# 3133 数组最后一个元素的最小值
# 中等

# 给你两个整数
# n 和 x。你需要构造一个长度为 n 的正整数数组 nums ，对于所有 0 <= i < n - 1 ，满足 nums[i + 1] 大于 nums[i] ，并且数组 nums 中所有元素的按位 AND
# 运算结果为 x 。

# 返回 nums[n - 1] 可能的最小值。

# 示例 1：
# 输入：n = 3, x = 4
# 输出：6
#
# 解释：
# 数组
# nums
# 可以是[4, 5, 6] ，最后一个元素为
# 6 。

class Solution:

    # x = 100100, n = 5, 则 0000 0001 0010 0011 0100
    # 即把 n - 1 的位放入 x 中为 0 的位
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        res = x
        for i in range(0, 31):
            if (x & (1 << i)) == 0:
                res |= ((n & 1) << i)
                n >>= 1
        res |= n << 31
        return res

if __name__ == '__main__':
    print(Solution().minEnd(3, 4))
