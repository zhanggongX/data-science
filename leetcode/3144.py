from collections import defaultdict
from math import inf


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [0] + [inf] * n
        for i in range(n):
            cnt = defaultdict(int)
            max_cnt = 0
            for j in range(i, -1, -1):
                cnt[s[j]] += 1
                if cnt[s[j]] > max_cnt:
                    max_cnt = cnt[s[j]]
                if i-j+1 == len(cnt) * max_cnt and dp[j] + 1 < dp[i+1]:
                    dp[i+1] = min(dp[i+1], dp[j] + 1)
        return dp[n]


if __name__ == '__main__':
    print(Solution().minimumSubstringsInPartition(s="aaa"))
