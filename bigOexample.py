#시간복잡도 = Big O 표기법 = 최악일 때의 연산 횟수를 나타낸 표기법.

import random
findNumber = random.randrange(1,101)

for i in range(1, 101):
    if i == findNumber:
        print(i)
        break

#시간 복잡도는 N번.

## 