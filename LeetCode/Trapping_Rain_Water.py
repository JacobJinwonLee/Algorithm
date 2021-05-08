# -*- coding: utf-8 -*-
"""
Created on Sat May  8 22:31:54 2021

@author: jinwo
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        volume = 0
        # two pointer
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            # update left_max, right_max
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
            # low side filled
            if left_max <= right_max:
                # update water height
                # Up to the maximum height point, add water height: 
                # difference between the maximum height and the current height of the left and right columns
                volume += left_max - height[left]
                # move
                left += 1
            else:
                volume += right_max - height[right]
                # move
                right -= 1
            
        return volume
    
    