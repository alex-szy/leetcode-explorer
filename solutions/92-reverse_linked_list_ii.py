# ID: 92
# Title: Reverse Linked List II
# Link: https://leetcode.com/problems/reverse-linked-list-ii/
# Difficulty: Medium
# Tags: Linked List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create a dummy node to eliminate the edge case where the start of the list has to be reversed
        dummy = ListNode(0, head)

        # Find the left split point
        left_end, mid_start = dummy, head
        for _ in range(left - 1):
            left_end = mid_start
            mid_start = mid_start.next

        # Find the first node of the right segment
        mid_end = mid_start
        for _ in range(right - left):
            mid_end = mid_end.next
        right_start = mid_end.next

        # Split the list so we can reverse it
        mid_end.next = None

        # Reverse the middle part
        left_end.next = self.reverseList(mid_start)

        # mid_start is now mid_end, cat the tail onto this node
        mid_start.next = right_start
        return dummy.next
