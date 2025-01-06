from traceback import print_tb

users = {
    'total_user':3,
    'information':[
        {'name':'alex', 'age':3, 'license':True},
        {'name':'june', 'age':7, 'license':False},
        {'name':'peter', 'age':4, 'license':False}
    ]
}
print(users[0])

total_age = cnt =0
for i in users['information']:
    print(i[0])
    # total_age += i['age']
    # cnt += 1


print(total_age/cnt)

# print(users['total_user'])
# print(users['information'][1]['age'])

