# -*- coding: utf-8 -*-
"""
Created on Thu May  6 01:59:46 2021

@author: jinwo
"""

import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # r: r 뒤의 문자열 그대로 반환
        # \w: 알파벳, 숫자, _ 중 하나
        # \w에 해당하지 않는 것은 공백으로 처리
        # 대소문자 구분 없고 소문자 출력
        # banned에 들어가면 안 됨
        words = [word for word in re.sub(r'[^\w]',' ', paragraph)
                 .lower().split() 
                 if word not in banned]
        
        counter = {}
        
        for word in words:
            if word not in counter:
                counter[word] = 0
            counter[word] += 1
        
        return max(counter, key=counter.get)
    
    def mostCommonWord_ver2(self, paragraph: str, banned: List[str]) -> str:
        # r: r 뒤의 문자열 그대로 반환
        # \w: 알파벳, 숫자, _ 중 하나
        # \w에 해당하지 않는 것은 공백으로 처리
        # 대소문자 구분 없고 소문자 출력
        # banned에 들어가면 안 됨
        words = [word for word in re.sub(r'[^\w]',' ', paragraph)
                 .lower().split() 
                 if word not in banned]
        
        # collections 라이브러리의 Counter 클래스. words에서 각 원소별로 몇 개 나오는지 딕셔너리로 돌려줌
        counts = collections.Counter(words)
        # most_common까지 하면 개수 순으로 정렬해서 주는데 [('a',3), ('b',2), ...] 이런 식
        # 1을 넣어주면 첫 번째 값으로 [('a',3)]. [0][0] 하면 'a'
        return counts.most_common(1)[0][0]