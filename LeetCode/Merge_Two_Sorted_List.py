# -*- coding: utf-8 -*-
"""
Created on Tue May 11 00:45:15 2021

@author: jinwo
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # No l1 or l2 exist + l1 > l2
        if (not l1) or (l2 and l1.val > l2.val):
            # smaller one -> left
            l1, l2 = l2, l1
        if l1:
            # next linked list 
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
