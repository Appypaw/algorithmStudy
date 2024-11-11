#https://school.programmers.co.kr/learn/courses/30/lessons/181832
"""
문제 설명

양의 정수 n이 매개변수로 주어집니다. n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(n):
    answer = [[0] * n for _ in range(n)]

    num = 1  # 시작숫자
    x, y = 0, 0  # 시작좌표
    dx, dy = 0, 1  # 시작방향

    directions = [(0,1), (1,0), (0,-1), (-1,0)]  # 오, 아래, 왼, 위
    direction_index = 0  # 방향 인덱스 = 이걸로 방향 바꾸는걸 조절함

    for _ in range(n*n):
        answer[x][y] = num  # x,y 위치에 숫자 넣음
        num += 1

        nx, ny = x + dx, y + dy     # 다음위치 계산

        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            direction_index = (direction_index + 1) % 4
            dx, dy = directions[direction_index]
            nx, ny = x + dx, y + dy
        
        x, y = nx, ny

    return answer