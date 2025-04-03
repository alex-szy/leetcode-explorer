# Title: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Tags: Array, Hash Table

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
