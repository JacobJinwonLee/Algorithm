# -*- coding: utf-8 -*-
"""
Created on Sun May  9 00:32:24 2021

@author: jinwo
"""


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # After sorting, when two pairs are held, the small value is in the even index
        nums.sort()
        sums = 0
        for i in range(0, len(nums), 2):
            sums += nums[i]
            
        return sums
    
    def arrayPairSum_ver2(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])