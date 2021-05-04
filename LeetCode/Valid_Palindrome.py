# -*- coding: utf-8 -*-
"""
Created on Wed May  5 02:13:35 2021

@author: jinwo
"""

import re

class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        strs = []

        for char in s:
            # 영문, 숫자 판별 isalnum()
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            # 리스트 맨 앞, 맨 뒤 비교해서 같아야 됨. 뽑아서 비교하고 날려버릴 것 
            if strs.pop() != strs.pop(0):
                return False

        return True

    def isPalindrome_ver2(self, s: str) -> bool:
        s = s.lower()
        
        # 정규식으로 알파벳, 숫자 아닌 것을 날려버림
        s = re.sub('[^a-z0-9]', '', s)
        
        # s[::-1] : 뒤집어줌.
        # s[::1] : 그대로
        # s[::2]: 2칸씩 앞으로 이동
        return s == s[::-1]
