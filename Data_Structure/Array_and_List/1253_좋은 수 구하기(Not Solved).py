"""
문제

N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.

N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.

수의 위치가 다르면 값이 같아도 다른 수이다.


입력

첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000), 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)


출력

좋은 수의 개수를 첫 번째 줄에 출력한다.

"""
import sys

input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))

m.sort()

answer = 0
s = 0
e = len(m)-1

for i in m:
    while m[s] < m[e]:
        if m[s] + m[e] == m[i]:
            answer += 1
            s += 1
            e -= 1
        elif m[s] + m[e] < m[i]:
            s += 1
        else:
            e -= 1

print(answer)

"""
10
1 2 3 4 5 6 7 8 9 10
"""