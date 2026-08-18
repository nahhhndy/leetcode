class Solution:
    def largestInteger(self, nums, k):
        count = {}

        for i in range(len(nums) - k + 1):
            for x in set(nums[i:i+k]):
                count[x] = count.get(x, 0) + 1

        ans = -1
        for x, c in count.items():
            if c == 1:
                ans = max(ans, x)

        return ans