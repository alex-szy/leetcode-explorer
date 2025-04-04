# ID: 141
# Title: Linked List Cycle
# Link: https://leetcode.com/problems/linked-list-cycle/
# Difficulty: Easy
# Tags: Hash Table, Linked List, Two Pointers
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Tortoise and hare approach. Have 1 fast and 1 slow pointer.
        If the fast pointer catches up with the slow pointer, we have a cycle.
        """
        fast, slow = head, head
        while fast and fast.next and slow:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
