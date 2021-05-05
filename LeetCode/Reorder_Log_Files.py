# -*- coding: utf-8 -*-
"""
Created on Thu May  6 01:32:07 2021

@author: jinwo
"""


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letters = []
        digits = []
        
        for log in logs:
            # dig1 8 1 5 1 --> 8
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
            
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return letters + digits