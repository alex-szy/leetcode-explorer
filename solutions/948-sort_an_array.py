# ID: 948
# Title: Sort an Array
# Link: https://leetcode.com/problems/sort-an-array/
# Difficulty: Medium
# Tags: Array, Divide and Conquer, Sorting, Heap (Priority Queue), Merge Sort, Bucket Sort, Radix Sort, Counting Sort
from typing import List
import random


class Solution:
    def sortArray(self, nums: List[int], start=0, stop=None) -> List[int]:
        # quicksort
        if stop is None:
            stop = len(nums)
        if stop <= start + 1:
            return nums
        l = self.partition(nums, start, stop)
        self.sortArray(nums, start, l)
        self.sortArray(nums, l, stop)
        return nums

    def partition(self, nums, start, stop):
        pivot = nums[random.randrange(start, stop)]
        l, r = start, stop - 1
        while l <= r:
            if nums[l] < pivot:
                l += 1
            elif nums[r] > pivot:
                r -= 1
            else:  # nums[l] >= pivot and nums[r] <= pivot
                if nums[l] != nums[r]:
                    nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return l
