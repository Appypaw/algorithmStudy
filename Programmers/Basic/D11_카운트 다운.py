#https://school.programmers.co.kr/learn/courses/30/lessons/181899
"""
문제 설명

정수 start_num와 end_num가 주어질 때, start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

"""

def solution(start_num, end_num):
    answer = []
    while start_num >= end_num:
        answer.append(start_num)
        start_num -= 1

    return answer

print(solution(10,3))