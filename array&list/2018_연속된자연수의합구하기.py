#투포인터

n = int(input())

count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count = count + 1
        end_index = end_index + 1
        sum += end_index
    elif sum > n:
        start_index = start_index + 1
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(count)

# +=는 이해가 안가는 부분들과 구분하기 위해 설정.