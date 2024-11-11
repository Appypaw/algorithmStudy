#https://school.programmers.co.kr/learn/courses/30/lessons/181873
"""
문제 설명

영소문자로 이루어진 문자열 my_string과 영소문자 1글자로 이루어진 문자열 alp가 매개변수로 주어질 때,
my_string에서 alp에 해당하는 모든 글자를 대문자로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string, alp):
    answer = ''
    for i in my_string:
        if i == alp:
            answer += alp.upper()
        else:
            answer += i
    return answer