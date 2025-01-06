nums = list(range(1,11))

for num in nums:
    if not num % 2:
        continue

    if not num % 3:
        continue

    print(num)