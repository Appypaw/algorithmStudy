#1번째 줄에 시험을 본 과목의 개수 N. 해당 값은 1,000보다 작거나 같다. 2번째 줄에 성적이 주어짐.
# 해당 값은 100보다 작거나 같은, 음이 아닌 정수이고, 적어도 1개의 값ㄷ은 0 보다 크다.

# 자기 점수중 최댓값을 고른 다음 최대값 M이라 할 때 모든 점수를 점수/M*100으로 고친다.

subjects = int(input())
score = list(map(int, input().split()))

m = max(score)
sum = 0

avg = 0

for i in score:
    i = i/m*100
    sum = sum + i

avg = sum/subjects

print(avg)