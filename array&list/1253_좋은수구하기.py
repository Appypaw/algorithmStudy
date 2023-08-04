# 1번째 줄에 수의 개수 N(1 <= N <= 2,000), 2번째 줄에 N개의 수의 값(A)이 주어진다. (A < 1,000,000,000).

#주어진 N개의 수에서 다른 두 수의 합으로 표현되는 수가 있다면 그 수를 '좋은 수'라고 한다. N개의 수중 좋은 수가 총 몇 개인지 출력하시오.

import sys

N = int(input())#데이터 개수
input = sys.stdin.readline  #다시 보기
Result = 0#좋은 수 개수 저장 변수
A = list(map(int, input().split()))
A.sort      #이 메소드 써도 되나??

for k in range(N):
    find = A[k]
    i = 0
    j = N - 1
    while i < j:
        if A[i] + A[j] == find:
            if i != k and j !=k:
                Result += 1