# -*- coding: utf-8 -*-
"""
Created on Fri May  7 01:23:39 2021

@author: jinwo
"""

import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # sorting each element of strs, make a dictionary
        
        # if a key is not exist: keyerror --> need a default one 
        # --> defaultdict in collections library
        # defaultdict(list, {})
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            # sort -> dictionary: if word is 'eat' then 
            # {'ate': ['ate','eat','tea',...]}
            # sorted returns a list --> use ''.join()
            # sorted('ate') -> ['a','e','t'] -> 'aet'
            anagrams[''.join(sorted(word))].append(word)
            
        return list(anagrams.values())