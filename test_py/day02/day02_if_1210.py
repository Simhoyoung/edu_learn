#if
age = int(input('몇 살이얌? :'))
if age >= 20:
    print('성인')
else:
    if age >= 10:
        print('청소년')
    else:
        if age >= 5:
            print('어린이')
        else:
            print('유아')