#https://school.programmers.co.kr/learn/courses/30/lessons/181891
"""
문제 설명

정수 리스트 num_list와 정수 n이 주어질 때, 
num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠 n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 붙인 리스트를 return하도록 solution 함수를 완성해주세요.

"""

def solution(num_list, n):
    answer = []
    answer.append(num_list[n:])
    answer.append(num_list[:n])
    return sum(answer, [])

"""
def solution(num_list, n):
    return num_list[n:] + num_list[:n]
"""

#어차피 파이썬에서 +연산으로 배열 합치면 걍 1차원으로 뒤에 붙여준다