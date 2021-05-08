# -*- coding: utf-8 -*-
"""
Created on Sun May  9 00:59:15 2021

@author: jinwo
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # do not use division
        # nums = [1,2,3,4]
        # p1 = [1, 1, 2, 6] : product from left end. 1*1, 1*2, 1*2*3
        # p2 = [24, 12, 4, 1] : product from right end. 1*4, 1*4*3, 1*4*3*2
        # p = [24, 12, 8, 6] : p1 * p2 elementwise
        
        out = []
        p = 1
        # left product
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        
        p = 1
        
        # right product
        # nums = [1,2,3,4] then p: 1 4 12 24
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        
        return out
        
        