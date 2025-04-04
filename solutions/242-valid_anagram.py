# ID: 242
# Title: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Tags: Hash Table, String, Sorting
from collections import Counter, defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
        for char in t:
            if counts[char] == 0:
                return False
            counts[char] -= 1
        return True
