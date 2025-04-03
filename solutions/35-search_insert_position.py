# ID: 35
# Title: Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/
# Difficulty: Easy
# Tags: Array, Binary Search
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Identical to a vanilla binary search, except for the return statement
        Why do we return left?
        Upon termination of the while loop, we only have 1 possible situation.
        The right pointer is 1 left of the left pointer.
        This could have happened due to 2 different situations.
        1. left == right, mid != target
        2. left + 1 == right, mid > target
        Remember, similar to firstBadVersion, we want to return the position of the first element which is greater than target.
        In both these situations, this is the left pointer.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
