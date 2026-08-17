from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pre = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(l, r):
            if l >= r:
                return 0

            ans = 0
            left = 0
            right = pre[r + 1] - pre[l]

            for k in range(l, r):
                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:
                    # This split can only give `left`.
                    # If even 2*left <= ans, it cannot improve ans.
                    if left * 2 <= ans:
                        continue
                    ans = max(ans, left + dfs(l, k))

                elif left > right:
                    # right is decreasing as k moves right.
                    # Once 2*right <= ans, all later right values
                    # are even smaller, so we can stop completely.
                    if right * 2 <= ans:
                        break
                    ans = max(ans, right + dfs(k + 1, r))

                else:
                    ans = max(
                        ans,
                        left + dfs(l, k),
                        right + dfs(k + 1, r)
                    )

            return ans

        return dfs(0, n - 1)