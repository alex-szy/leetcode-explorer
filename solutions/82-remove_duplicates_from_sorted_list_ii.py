# ID: 82
# Title: Remove Duplicates from Sorted List II
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Difficulty: Medium
# Tags: Linked List, Two Pointers
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr:
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
            if prev.next != curr:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
