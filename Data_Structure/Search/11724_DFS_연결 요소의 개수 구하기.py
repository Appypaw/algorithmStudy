"""

문제

방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.



입력

첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
(1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

"""
import sys
sys.setrecursionlimit(100000)                             #재귀 깊이 제한 해야함. BOJ 참조


node, edge = map(int, sys.stdin.readline().split())
A = [[] for _ in range (node+1)]                           #그래프 데이터 저장 인접 리스트
visited = [False] * (node+1)

for _ in range(edge):                                       #그래프 데이터 입력 받기
    s, e = map(int, sys.stdin.readline().split())
    A[s].append(e)                                          #양방향 엣지이므로 양쪽에 엣지 더하기
    A[e].append(s)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

cnt = 0

for i in range(1, node+1):
    if not visited[i]:
        cnt += 1
        DFS(i)

print(cnt)