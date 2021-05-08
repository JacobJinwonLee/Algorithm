# -*- coding: utf-8 -*-
"""
Created on Sat May  8 23:10:07 2021

@author: jinwo
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        # to make it easier to compare i and i +- 1
        nums.sort()
        
        for i in range(len(nums)-2):
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # move. three numbers at i, left, right
            # left starts from i+1, right starts from len(nums)-1
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                
                # sorted -> sums < 0 then wanna be large, sums > 0 then wanna be small
                if sums < 0:
                    left += 1
                elif sums > 0:
                    right -= 1
                else:
                    # sum = 0 case
                    results.append([nums[i], nums[left], nums[right]])
                    
                    # at least three consecutive equal numbers? 
                    # [-4 2 2 2 2 1 3 5] then -4 2 2 is good, two '2' must be skipped
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
            
        return results