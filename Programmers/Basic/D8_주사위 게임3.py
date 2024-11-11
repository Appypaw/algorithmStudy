#https://school.programmers.co.kr/learn/courses/30/lessons/181916

"""
문제 설명

1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

    네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
    세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
    주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
    어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
    네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.

네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
제한사항

    a, b, c, d는 1 이상 6 이하의 정수입니다.

입출력 예
a 	b 	c 	d 	result
2 	2 	2 	2 	2222
4 	1 	4 	4 	1681
6 	3 	3 	6 	27
2 	5 	2 	6 	30
6 	4 	2 	5 	2
"""

from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]
    cnt = Counter(dice)
    if len(cnt) == 1:
        return a*1111
    elif len(cnt) == 2:
        p, q = cnt.most_common()
        if p[1] == 3:
            return (10*p[0]+q[0]) ** 2
        else:
            return (p[0]+q[0]) * abs(p[0]-q[0])
    elif len(cnt) == 3:
        p ,q, r = cnt.most_common()
        return q[0] * r[0]
    elif len(cnt) == 4:
        return min(dice)