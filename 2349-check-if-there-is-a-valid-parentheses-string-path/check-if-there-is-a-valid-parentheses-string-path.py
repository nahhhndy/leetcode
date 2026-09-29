from functools import cache
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # Quick impossible cases
        if (m + n - 1) % 2 == 1:
            return False

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        @cache
        def dfs(i, j, balance):
            # Add current cell
            if grid[i][j] == '(':
                balance += 1
            else:
                balance -= 1

            # Invalid prefix
            if balance < 0:
                return False

            # Not enough cells left to close all '('
            remaining = (m - 1 - i) + (n - 1 - j)

            if balance > remaining:
                return False

            # Reached destination
            if i == m - 1 and j == n - 1:
                return balance == 0

            # Move down
            if i + 1 < m and dfs(i + 1, j, balance):
                return True

            # Move right
            if j + 1 < n and dfs(i, j + 1, balance):
                return True

            return False

        return dfs(0, 0, 0)