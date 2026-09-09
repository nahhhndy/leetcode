class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        threshold = 1000
        commas = 1

        while threshold <= n:
            end = min(n, threshold * 1000 - 1)

            count = end - threshold + 1

            ans += count * commas

            threshold *= 1000
            commas += 1

        return ans