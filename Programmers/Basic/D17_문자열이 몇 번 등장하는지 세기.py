#https://school.programmers.co.kr/learn/courses/30/lessons/181871
"""
문제 설명

문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.
"""

def solution(myString, pat):
    answer=0
    for i in range(len(myString)):
        if myString[i:i+len(pat)]==pat:
            answer+=1
    return answer