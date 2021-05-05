# -*- coding: utf-8 -*-
"""
Created on Thu May  6 01:05:27 2021

@author: jinwo
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        s.reverse()
        
    def reverseString_ver2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        left = 0
        right = len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
    def reverseString_ver3(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]