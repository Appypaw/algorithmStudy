#https://school.programmers.co.kr/learn/courses/30/lessons/181882
"""
문제 설명

정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱합니다. 
그 결과인 정수 배열을 return 하는 solution 함수를 완성해 주세요.
"""

def solution(arr):
    answer = []
    for i in arr:
        if i > 49 and i%2 == 0:
            answer.append(i/2)
        elif i < 50 and i%2 != 0:
            answer.append(i*2)
        else:
            answer.append(i)
    return answer