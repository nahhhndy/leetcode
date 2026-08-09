from functools import lru_cache

class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dfs(i, m):
            if i + 2 * m >= n:
                return suffix[i]

            ans = 0
            for x in range(1, 2 * m + 1):
                ans = max(ans, suffix[i] - dfs(i + x, max(m, x)))

            return ans

        return dfs(0, 1)