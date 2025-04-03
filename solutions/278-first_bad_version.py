# ID: 278
# Title: First Bad Version
# Link: https://leetcode.com/problems/first-bad-version/
# Difficulty: Easy
# Tags: Binary Search, Interactive

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
from typing import Callable


class Solution:
    def firstBadVersion(self, n: int, isBadVersion: Callable[[int], bool]) -> int:
        """
        In this version of binary search, since we do right = mid instead of right = mid - 1, and we use floor div, the 2 pointers will NEVER cross over.
        Upon algorithm termination, left always == right
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
