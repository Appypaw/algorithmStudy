#https://school.programmers.co.kr/learn/courses/30/lessons/181890
"""
문제 설명

문자열 리스트 str_list에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다. 
str_list에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면 해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를, 
먼저 나오는 문자열이 "r"이라면 해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

 "l"이나 "r"이 없다면 빈 리스트를 return합니다.

"""

def solution(str_list):
    for i,j in enumerate(str_list):
        if j == 'l':
            return str_list[:i]
        elif j == 'r':
            return str_list[i+1:]
    return []   #이게 elif랑 같은 블록에 있으면 l이나 r이 나오지 않는 그 즉시 바로 []를 반환함.