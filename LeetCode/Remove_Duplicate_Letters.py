# -*- coding: utf-8 -*-
"""
Created on Thu May 27 01:35:25 2021

@author: jinwo
"""

import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = collections.Counter(s), []
        
        for char in s:
            counter[char] -= 1
            if char in stack:
                continue
            # Remove from stack if any characters remain to attach to the back
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            
            stack.append(char)
        
        return ''.join(stack)
            