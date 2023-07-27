#N개의 숫자가 공백 없이 써 있다. 이 숫자를 모두 합해 출력하는 프로그램을 작성하시오.
#입력 : 1번째 줄에 숫자의 개수 N(1 <= N <= 100), 2번째 줄에 숫자 N개가 공백 없이 주어진다.

'''
n = input()
numbers = list(input())
sum = 0

for i in numbers:
    sum = sum + int(i)

print(sum)
'''

a = input()
numbers = list(a)
suma = 0

for i in numbers:
    suma = suma + int(i)

print(suma)

#굳이 첫번째줄에 숫자 크기만큼의 입력을 받는 이유를 모르겠음..