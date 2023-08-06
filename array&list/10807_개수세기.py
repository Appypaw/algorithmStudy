"""
첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어져있다. 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.
"""

numofArray = int(input())                    #배열 갯수
arr = list(map(int, input().split()))        # 배열
num = int(input())                         #원하는 수

count = 0

for i in arr:
    if i == num:
        count += 1

print(count)