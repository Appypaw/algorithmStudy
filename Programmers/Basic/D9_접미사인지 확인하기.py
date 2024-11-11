#https://school.programmers.co.kr/learn/courses/30/lessons/181908
"""
문제 설명

어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
문자열 my_string과 is_suffix가 주어질 때, is_suffix가 my_string의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.

"""

def solution(my_string, is_suffix):
    suffix = []
    for i in range(len(my_string)):
        suffix.append(my_string[i:])
    
    for a in suffix: 
        if a == is_suffix:
            return 1
    return 0

"""
def solution(my_string, is_suffix):
    return 1 if my_string.endswith(is_suffix) else 0

my_string.endswith(is_suffix)는 my_string이 is_suffix로 끝나는지를 확인하는 함수
이 함수는 True나 False를 반환하므로, True일 경우 1을 반환하고, False일 경우 0을 반환하도록 삼항 연산자를 사용


"""

