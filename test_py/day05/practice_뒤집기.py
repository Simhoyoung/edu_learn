word = 'hello'
#
ans=''
# for w in word:
#     ans = + ans
# print(ans)

for i in range(len(word)-1, -1, -1):
    ans += word[i]

print(ans)