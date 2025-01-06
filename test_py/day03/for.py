nums = [8, 1, 2, 5, 7, 9, 6]
ans = []

# for 변수 in 컨테이너 :
# indent 반복할 로직
for num in nums:
    if num % 2 == 1:
        ans.append(num)

print(ans, len(ans))

