# ID: 792
# Title: Binary Search
# Link: https://leetcode.com/problems/binary-search/
# Difficulty: Easy
# Tags: Array, Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Note: the termination for a vanilla binary search is always when left == right
        left > right will never occur.
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
        return None
