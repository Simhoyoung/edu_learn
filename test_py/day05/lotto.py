import random

# 로또 번호 데이터 필요
lotto = {8, 15, 19, 21, 32, 36}

# 집계틀
result = {i: 0 for i in range(7)}

# 몇 게임?
n = int(input())

# 랜덤번호
for _ in range(n):
    my = set(random.sample(range(1, 46), 6))
    cnt = len(lotto & my)
    result[cnt] += 1

print(result)