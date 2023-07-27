#첫번째 줄에 시험을 본 과목의 개수 N, 해당 값은 1000보다 작거나 같음.
#두번째 줄에 성적. 100보다 작은 양의 정수이머 적어도 1개의 값은 0보다 크다.
#자기 점수중 최댓값을 골라서 최댓값을 M이라 할 때 모든 점수를 점수 / M * 100으로 고쳤다. 
#이 때 평균을 구하는 코드를 작성하시오.

subjects = input()
scores = input()

scores_list = [int(num) for num in scores.split(" ")]

maxScore = max(scores_list)
sum = 0

for i in scores_list:
    sum = sum + i

output = (sum*100)/int(maxScore)/int(subjects)

print(output)