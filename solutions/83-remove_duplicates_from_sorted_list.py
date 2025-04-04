# ID: 83
# Title: Remove Duplicates from Sorted List
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Difficulty: Easy
# Tags: Linked List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev, curr = head, head.next
        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            prev.next = curr
            prev = curr
            curr = curr.next
        return head
