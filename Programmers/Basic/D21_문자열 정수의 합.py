#https://school.programmers.co.kr/learn/courses/30/lessons/181849
"""
문제 설명

한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.
"""

def solution(num_str):
    sum = 0
    for i in range(len(num_str)):
        sum += int(num_str[i])

    return sum

"""
def solution(num_str):
    return sum(map(int, list(num_str)))
"""