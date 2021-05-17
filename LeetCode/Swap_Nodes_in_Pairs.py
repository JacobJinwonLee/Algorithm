# -*- coding: utf-8 -*-
"""
Created on Tue May 18 02:20:09 2021

@author: jinwo
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        # prev는 head보다 앞
        prev.next = head
        
        while head and head.next:

            # 처음 b 정의를 head가 가리키는 것으로 했다가
            # b가 head를 가리키고 head는 b의 다음을 가리키는 것으로 바꿈
            
            b = head.next
            head.next = b.next
            b.next = head
            
            # head의 이전인 prev가 b를 가리키게 함
            
            prev.next = b
            
            # move
            head = head.next
            prev = prev.next.next
        return root.next