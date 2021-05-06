# -*- coding: utf-8 -*-
"""
Created on Fri May  7 01:59:45 2021

@author: jinwo
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # whole string is palindrome -> good!, 
        # length of string < 2 -> already a palindrome! 
        if len(s) < 2 or s == s[::-1]:
            return s
        
        # detect palindrome + expand two pointer
        # (i, i+1) palindrome -> i-1 == i+2 -> (i-1, i+2) palindrome -> ...
        # if while loop breaks, s[left+1 : right] is palindrome 
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]
        
        result = ''
        
        # move two pointer
        # start at the left end, [0,1] -> [1,2] -> [2,3] -> ...
        # start at the left end, [0,1,2] -> [1,2,3] -> ...
        for i in range(len(s)-1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
            
        return result