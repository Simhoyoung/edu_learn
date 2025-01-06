# 다음의 리스트에서 소숫점을 제외한 평균값을 구하시오. ex) 3.1724일 경우 3을 출력
nums = [1, 7, 2, 3, 6, 1, 2, 5, 3, 4, 8, 7]

a=b=0
for i in nums:
    a += i
    b += 1

ans = a/b
print(round(ans))
# print(answer) # 4