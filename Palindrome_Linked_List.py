# -*- coding: utf-8 -*-
"""
Created on Tue May 11 00:11:53 2021

@author: jinwo
"""

import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = []
        
        if not head:
            return True
        
        # ListNode(linked list): Head -> value/next -> value/next -> ...
        node = head
        # covert to list
        while node is not None:
            q.append(node.val)
            node = node.next
            
        # palindrome?
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        
        return True
    
    def isPalindrome_ver2(self, head: ListNode) -> bool:
        # deque
        q = collections.deque()
        
        if not head:
            return True
        
        # ListNode(linked list): Head -> value/next -> value/next -> ...
        node = head
        # covert to deque
        while node is not None:
            q.append(node.val)
            node = node.next
            
        # palindrome?
        while len(q) > 1:
            # deque is faster than linked list -> list
            if q.popleft() != q.pop():
                return False
        
        return True