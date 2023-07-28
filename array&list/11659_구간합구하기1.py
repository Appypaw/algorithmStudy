#1번째 줄에 수의 개수 N(1 ≤ N ≤ 100,000), 합을 구해야 하는 횟수 M(1 ≤ M ≤ 100,000), 2번째 줄에 N개의 수가 주어진다.
#각 수는 1,000보다 작거나 같은 자연수다.
#3번째 줄 부터는 M개의 줄에 합을 구해야 하는 구간 i와 j가 주어진다.

#총 M개의 줄에 입력으로 주어진 i번째 수에서 j번째 수까지의 합을 출력한다.

firstline = list(map(int, input().split()))
numbers = list(map(int, input().split()))

numOfData = firstline[0]
questions = firstline[1]

for series in numbers:
    sum = 0
    series = series + sum

#조금 더 고민해보기,,,,,, 