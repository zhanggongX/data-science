'''
997. 找到小镇的法官

简单

小镇里有 n 个人，按从 1 到 n 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。

如果小镇法官真的存在，那么：

小镇法官不会信任任何人。
每个人（除了小镇法官）都信任这位小镇法官。
只有一个人同时满足属性 1 和属性 2 。
给你一个数组 trust ，其中 trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人。

如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 -1 。
'''
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_arr = [0] * (n + 1)
        out_arr = [0] * (n + 1)

        for i in trust:
            in_arr[i[1]] += 1
            out_arr[i[0]] += 1

        for i in range(n+1):
            if in_arr[i] == n - 1 and out_arr[i] == 0:
                return i

        return -1


if __name__ == '__main__':
    n = 2
    trust = [[1, 2]]

    print(Solution().findJudge(n, trust))
