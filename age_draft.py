'''age = input('сколько вам лет?')
if age < 18:
    print('вам нельзя')
elif age > 18:
    print('синий или красный?')
'''

age = input('сколько вам лет?')
if int(age) < 18:
    print('вам нельзя')
elif int(age) > 18:
    print('синий или красный?')
else:
    print('введите цифры')