# ID: 1753
# Title: Path With Minimum Effort
# Link: https://leetcode.com/problems/path-with-minimum-effort/
# Difficulty: Medium
# Tags: Array, Binary Search, Depth-First Search, Breadth-First Search, Union Find, Heap (Priority Queue), Matrix
from typing import List
import heapq
import math


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Modified dijkstra algorithm that calculates the minimum effort required to traverse from [0][0] to [-1][-1]
        The effort of a path is defined as the maximum change of elevation from 1 square to the next in that path
        """
        nrows, ncols = len(heights), len(heights[0])
        minimumEfforts = [[math.inf for _ in range(ncols)]
                          for _ in range(nrows)]
        minimumEfforts[0][0] = 0
        visited = [[False for _ in range(ncols)] for _ in range(nrows)]
        q = [(0, 0, 0)]
        while q:
            currMinEffort, r, c = heapq.heappop(q)
            visited[r][c] = True
            refHeight = heights[r][c]
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < nrows and 0 <= nc < ncols and not visited[nr][nc]:
                    nextMinEffort = max(currMinEffort, abs(
                        heights[nr][nc] - refHeight))
                    if nextMinEffort < minimumEfforts[nr][nc]:
                        minimumEfforts[nr][nc] = nextMinEffort
                        heapq.heappush(q, (nextMinEffort, nr, nc))
        return minimumEfforts[-1][-1]
