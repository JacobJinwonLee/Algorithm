# -*- coding: utf-8 -*-
"""
Created on Tue May 18 01:44:31 2021

@author: jinwo
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # reverse linked list
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        
        return prev
    
    # linked list to python list
    def toList(self, node: ListNode) -> List:
        python_list = []
        
        while node:
            python_list.append(node.val)
            node = node.next
            
        return python_list

    # python list to linked list (+ reversed)
    def toReversedLinkedList(self, result: str) -> ListNode:
        # ListNode prev
        prev = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        
        return node
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        
        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))
        
        return self.toReversedLinkedList(str(resultStr))