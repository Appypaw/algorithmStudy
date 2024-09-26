#https://school.programmers.co.kr/learn/courses/30/lessons/181904
"""
문제 설명

문자열 my_string과 두 정수 m, c가 주어집니다. my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.
제한사항

    my_string은 영소문자로 이루어져 있습니다.
    1 ≤ m ≤ my_string의 길이 ≤ 1,000
    m은 my_string 길이의 약수로만 주어집니다.
    1 ≤ c ≤ m

"""

def solution(my_string, m, c):
    answer = []
    for i in range(0, len(my_string), m):
        answer.append(my_string[i + c -1])

    return ''.join(answer)

# 4(m)씩 쪼개서 2(c)번째
# 0 1 2 3  4 5 6 7  8 9 10 11...
# 1, 5, 9,, (c-1)+m*i