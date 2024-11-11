#https://school.programmers.co.kr/learn/courses/30/lessons/181866
"""
문제 설명

문자열 myString이 주어집니다. "x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후 사전순으로 정렬한 배열을 return 하는 solution 함수를 완성해 주세요.

단, 빈 문자열은 반환할 배열에 넣지 않습니다.
"""

def solution(myString):
    answer = []
    temp = ''
    for i in myString:
        if i == 'x':
            if temp: #temp가 비어져있으면 안됨
                answer.append(temp)
            temp = ''
        else:
            temp += i

    if temp:  #마찬가지로 ㅇㅇ
        answer.append(temp)
    
    answer.sort()
    return answer