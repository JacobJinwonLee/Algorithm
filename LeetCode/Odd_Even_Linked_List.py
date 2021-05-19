# -*- coding: utf-8 -*-
"""
Created on Thu May 20 01:57:52 2021

@author: jinwo
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # exception
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next
        
        # keep going: odd-even-odd-even-...
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        
        # final odd -> even_head
        odd.next = even_head
        
        return head
