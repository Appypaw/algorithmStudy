#https://school.programmers.co.kr/learn/courses/30/lessons/181894
"""
문제 설명

정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.

단, arr에 2가 없는 경우 [-1]을 return 합니다.
제한사항

    1 ≤ arr의 길이 ≤ 100,000
        1 ≤ arr의 원소 ≤ 10
"""

def solution(arr):
    if 2 not in arr:
        return [-1]
    
    s = arr.index(2) #index 메소드는 인자가 있는 가장 처음 인덱스를 리턴함.
    e = len(arr) - 1 - arr[::-1].index(2)
    return arr[s:e+1]