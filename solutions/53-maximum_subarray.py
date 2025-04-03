# ID: 53
# Title: Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium
# Tags: Array, Divide and Conquer, Dynamic Programming
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Enforces the recurrence relation
        maxSumEndingAt[i] = max(0, maxSumEndingAt[i-1]) + nums[i]
        The maximum sum of contiguous array elements which ends at an index depends only on the maximum sum of contiguous array elements which ends at the previous index
        Each step, we are choosing whether to include the previous sequence of contiguous elements or not.
        If the previous sequence of contiguous elements has a negative sum, then it is obviously not in the maximum sum.
        """
        maxSumEndingAt = [nums[0]]
        maxSub = nums[0]
        for i in range(1, len(nums)):
            maxSumEndingAt.append(max(0, maxSumEndingAt[-1]) + nums[i])
            maxSub = max(maxSub, maxSumEndingAt[-1])
        return maxSub

    def maxSubArray(self, nums: List[int]) -> int:
        """
        More space efficient than previous implementation.
        Instead of an array, we use just a single element to track the previous maximum sum
        """
        maxSumEndingAt = 0
        maxSub = nums[0]
        for num in nums:
            if maxSumEndingAt < 0:
                maxSumEndingAt = 0
            maxSumEndingAt += num
            maxSub = max(maxSub, maxSumEndingAt)
        return maxSub
