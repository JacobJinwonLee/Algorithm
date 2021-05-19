# -*- coding: utf-8 -*-
"""
Created on Thu May 20 02:36:09 2021

@author: jinwo
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # exception
        if not head or left == right:
            return head
        
        root = start = ListNode(None)
        root.next = head
        # start, end
        for _ in range(left-1):
            start = start.next
        end = start.next
        
        # swap node
        for _ in range(right-left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        
        return root.next
