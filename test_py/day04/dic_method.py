names = ['a', 'b', 'b', 'c', 'a', 'b', 'a', 'c','c','a','b','b']
# d = {'a':0, 'b':0, 'c':0} # 집계는 미리 만들 수 없음
d = {}

for name in names:
    d[name] = d.get(name, 0) + 1

# for name in names:
#     if name in d:
#         d[name] += 1
#     else:
#         d[name] = 1

# .get사용
# for name in names:
#     if d.get(name, -1) == -1:
#         d[name] =1
#     else:
#         d[name] += 1

print(d)



# d = {'name':'jane', 'age': 7, 'license':True}
# for k in d:
#     print(k, d[k])