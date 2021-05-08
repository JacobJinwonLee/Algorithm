# -*- coding: utf-8 -*-
"""
Created on Sat May  8 21:55:09 2021

@author: jinwo
"""


class Solution:
    
    # Brute Force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
    
    def twoSum_ver2(self, nums: List[int], target: int) -> List[int]:
        
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            # switch key, value to return index 
            nums_map[num] = i
    