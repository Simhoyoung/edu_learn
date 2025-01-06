nums = [8, 1, 2, 5, 7, 9, 6]
cnt = 0 #count

for num in nums:
    if num % 2 == 1:
        cnt += 1

print(cnt)