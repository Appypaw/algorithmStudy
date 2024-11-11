#https://school.programmers.co.kr/learn/courses/30/lessons/181855
"""
문제 설명

문자열 배열 strArr이 주어집니다. 
strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.
"""
from collections import Counter

def solution(strArr):
    answer = 0
    temp = []
    for i in strArr:
        temp.append(len(i))

    cnt = Counter(temp)
    return max(cnt.values())

"""
def solution(strArr):
    a=[0]*31
    for x in strArr: 
        a[len(x)]+=1
    return max(a)
"""