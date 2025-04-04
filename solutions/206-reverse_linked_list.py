# ID: 206
# Title: Reverse Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy
# Tags: Linked List, Recursion
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


if __name__ == "__main__":
    pass
