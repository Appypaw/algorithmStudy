def solution(number, n, m):

    answer = 0

    if number%n == 0 and number%m == 0:
        return 1
    else:
        return 0
    return answer

#%와 &는 다르다. 나머지를 구하는건 %고 &는 비트 AND 연산을 수행한다. 잘좀 보자