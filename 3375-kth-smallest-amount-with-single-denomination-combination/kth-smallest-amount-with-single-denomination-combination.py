from math import gcd


class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:

        n = len(coins)

        # Precompute LCM for every subset.
        subsets = []

        for mask in range(1, 1 << n):
            lcm = 1
            bits = 0
            valid = True

            for i in range(n):
                if mask & (1 << i):
                    bits += 1

                    g = gcd(lcm, coins[i])
                    lcm = lcm // g * coins[i]

                    # LCM larger than our useful range
                    if lcm > k * min(coins):
                        valid = False
                        break

            if valid:
                subsets.append((lcm, bits))

        def count(x):
            total = 0

            for lcm, bits in subsets:
                amount = x // lcm

                if bits % 2 == 1:
                    total += amount
                else:
                    total -= amount

            return total

        # The answer cannot exceed k * smallest coin.
        left = 1
        right = k * min(coins)

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left