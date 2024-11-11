#https://school.programmers.co.kr/learn/courses/30/lessons/181870
"""
문제 설명

문자열 배열 strArr가 주어집니다. 
배열 내의 문자열 중 "ad"라는 부분 문자열을 포함하고 있는 모든 문자열을 제거하고 남은 문자열을 순서를 유지하여 배열로 return 하는 solution 함수를 완성해 주세요.
"""

def solution(strArr):
    answer = strArr[:]
    for i in range(len(strArr)-1, -1, -1):
        if 'ad' in strArr[i]:
            answer.pop(i)
    return answer

"""
def solution(strArr):
    return [word for word in strArr if 'ad' not in word]
"""