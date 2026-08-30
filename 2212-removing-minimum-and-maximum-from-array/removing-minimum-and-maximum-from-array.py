class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = max_idx = 0

        # Find indices of min and max in one pass
        for i in range(1, n):
            if nums[i] < nums[min_idx]:
                min_idx = i
            elif nums[i] > nums[max_idx]:
                max_idx = i

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # 1. Both from front
        front = right + 1

        # 2. Both from back
        back = n - left

        # 3. One from each side
        both = (left + 1) + (n - right)

        return min(front, back, both)