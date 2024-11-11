"""

문제

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
정점 번호는 1번부터 N번까지이다.


입력

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
입력으로 주어지는 간선은 양방향이다.

"""

import sys
from collections import deque

input = sys.stdin.readline

Node, Edge, Start = map(int, input().split())
A = [[] for _ in range(Node + 1)]   #인접리스트
visited = [False] * (Node + 1)

for i in range(Edge):   #인접리스트 받기
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for s in A:
    s.sort()

# def DFS(v):
#     print(v, end=' ')
#     if not visited[v]:
#         visited[v] = True
#         for i in A[v]:
#             DFS(i)

def DFS(v):
    if not visited[v]:  # 방문 여부 확인
        visited[v] = True
        print(v, end=' ')
        for i in A[v]:
            DFS(i)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

DFS(Start)
print()
visited = [False] * (Node + 1)
BFS(Start)