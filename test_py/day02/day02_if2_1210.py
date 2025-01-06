#elif
age = int(input('몇 살?? :'))

if age >= 20:
    print('성인')
elif age >= 10:
    print('청소년')
elif age >= 5:
    print('어린이')
elif 0 < age < 5:
    print('유아')
else:
    print('제대로 입력하셈')
