#첫번째 줄에 시험을 본 과목의 개수 N, 해당 값은 1000보다 작거나 같음.
#두번째 줄에 성적. 100보다 작은 양의 정수이머 적어도 1개의 값은 0보다 크다.

subjects = input()
scores = input()

scores_list = [int(num) for num in scores.split(" ")]

sum = 0

for i in scores_list:
    sum = sum + i

output = sum/int(subjects)

print(output)