#https://school.programmers.co.kr/learn/courses/30/lessons/181862
"""
문제 설명

임의의 문자열이 주어졌을 때 문자 "a", "b", "c"를 구분자로 사용해 문자열을 나누고자 합니다.

예를 들어 주어진 문자열이 "baconlettucetomato"라면 나눠진 문자열 목록은 ["onlettu", "etom", "to"] 가 됩니다.

문자열 myStr이 주어졌을 때 위 예시와 같이 "a", "b", "c"를 사용해 나눠진 문자열을 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

단, 두 구분자 사이에 다른 문자가 없을 경우에는 아무것도 저장하지 않으며, return할 배열이 빈 배열이라면 ["EMPTY"]를 return 합니다.
"""

def solution(myStr):
    answer = []
    a_splited = myStr.split('a')
    b_splited = []
    c_splited = []

    for i in a_splited:
        b_splited.extend(i.split('b'))

    for i in b_splited:
        c_splited.extend(i.split('c'))

    answer = [i for i in c_splited if i]

    if not answer:
        return ["EMPTY"]
    
    return answer

"""
def solution(myStr):
    answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x] #a,b,c를 괄호로 교체하고 그걸 나눠서 answer에 x로 순회하고 만약 값이 있으면 answer의 배열에 넣음
    return answer if answer else ['EMPTY']
"""