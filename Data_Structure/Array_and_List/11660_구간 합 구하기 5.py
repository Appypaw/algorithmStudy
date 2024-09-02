"""
첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. 
(1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 
다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 
표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)
"""

import sys
input = sys.stdin.readline

size, query = map(int, input().split())
A = [[0] * (n+1)] #1차원 배열 선언. 나중에 append를 통해 2차원 배열로 확장
D = [[0] * (n+1) for _ in range(n+1)] #2차원 배열 선언 및 초기화

for i in range(size):
    A_row = [0]+[int(x) for x in input().split()] #[0] + [int(x) for x in input().split()] 부분에서 앞의 [0]은 리스트의 맨 앞에 0을 추가. 사용자가 1 2 3을 입력했다면 이 구문은 [0, 1, 2, 3]을 생성.
    A.append(A_row)

for i in range(1, size+1):
    for j in range(1, size+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(query):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]