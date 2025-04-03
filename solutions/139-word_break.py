# ID: 139
# Title: Word Break
# Link: https://leetcode.com/problems/word-break/
# Difficulty: Medium
# Tags: Array, Hash Table, String, Dynamic Programming, Trie, Memoization
from typing import List
from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        maxlen = max(len(word) for word in wordDict)
        arr = [False for _ in range(len(s))]
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                arr[i] = True
            else:
                arr[i] = any(
                    arr[j-1] and s[j:i+1] in wordDict for j in range(i, max(0, i - maxlen), -1))
        return arr[-1]

    def wordBreak(self, s, wordDict) -> bool:
        wordDict = set(wordDict)
        q = deque([s])
        seen = set(q)
        while q:
            curr = q.popleft()
            if curr in wordDict:
                return True
            for i in range(len(curr)):
                start, end = curr[:i+1], curr[i+1:]
                if start in wordDict and end not in seen:
                    q.append(end)
                    seen.add(end)
        return False
