"""
수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.

즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.


입력

첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)
둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)


출력

첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.
"""

import sys
input = sys.stdin.readline

n,m= map(int, input().split())
num = list(map(int, input().split()))
prefix_num = []
C = [0] * n
answer = 0
temp = 0

for i in num:
    temp = temp+i
    prefix_num.append(temp) #일단 배열합 구함

for i in range(m):
    remain = prefix_num[i] % n
    if m == 0:
        answer += 1
        C[i] = 0
    else:
        C[i] = remain

for i in range(m):
    if C[i] > 1: #만약 나머지가 있는 배열이 1개 초과면
        answer += (C[i]*(C[i]-1) // 2) #Combination

print(answer)