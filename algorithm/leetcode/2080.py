'''
2080. 区间内查询数字的频率

提示
请你设计一个数据结构，它能求出给定子数组内一个给定值的 频率 。
子数组中一个值的 频率 指的是这个子数组中这个值的出现次数。

请你实现 RangeFreqQuery 类：
RangeFreqQuery(int[] arr) 用下标从 0 开始的整数数组 arr 构造一个类的实例。
int query(int left, int right, int value) 返回子数组 arr[left...right] 中 value 的 频率 。
一个 子数组 指的是数组中一段连续的元素。arr[left...right] 指的是 nums 中包含下标 left 和 right 在内 的中间一段连续元素。

'''
from bisect import bisect, bisect_right, bisect_left
from collections import defaultdict
from typing import List


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        pos = defaultdict(list)
        for i, x in enumerate(arr):
            pos[x].append(i)
        self.pos = pos

    def query(self, left: int, right: int, value: int) -> int:
        pos_list = self.pos[value]
        return bisect_right(pos_list, right) - bisect_left(pos_list, left)


if __name__ == '__main__':
    range_query = RangeFreqQuery([3, 4, 5, 3, 3, 2, 2, 2, 5, 4])
    print(range_query.query(1, 6, 2))
