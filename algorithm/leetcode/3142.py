'''3142. 判断矩阵是否满足条件
已解答
简单
相关标签
相关企业
提示
给你一个大小为 m x n 的二维矩阵 grid 。你需要判断每一个格子 grid[i][j] 是否满足：

如果它下面的格子存在，那么它需要等于它下面的格子，也就是 grid[i][j] == grid[i + 1][j] 。
如果它右边的格子存在，那么它需要不等于它右边的格子，也就是 grid[i][j] != grid[i][j + 1] 。
如果 所有 格子都满足以上条件，那么返回 true ，否则返回 false 。
'''
from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if i + 1 < row and grid[i][j] != grid[i + 1][j]:
                    return False
                if j + 1 < col and grid[i][j] == grid[i][j + 1]:
                    return False

        return True


if __name__ == '__main__':
    print(Solution().satisfiesConditions([[1, 0, 2], [1, 0, 2]]))
