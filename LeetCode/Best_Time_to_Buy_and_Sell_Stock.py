# -*- coding: utf-8 -*-
"""
Created on Sun May  9 01:17:39 2021

@author: jinwo
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = 100000000000
        
        # update min_price. update profit
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)
            
        return profit