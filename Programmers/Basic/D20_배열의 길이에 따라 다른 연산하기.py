#https://school.programmers.co.kr/learn/courses/30/lessons/181854
"""
문제 설명

정수 배열 arr과 정수 n이 매개변수로 주어집니다. 
arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을, arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(arr, n):
    answer = []
    if len(arr) % 2 != 0:
        for i in range(len(arr)):
            if i % 2 == 0:
                arr[i] += n
    else:
        for i in range(len(arr)):
            if i % 2 != 0:
                arr[i] += n

    return arr

"""
def solution(arr, n):
    N=len(arr)
    if N%2:
        for i in range(0,N,2): arr[i]+=n
    else:
        for i in range(1,N,2): arr[i]+=n
    return arr
"""