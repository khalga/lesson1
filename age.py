input_age = input('Сколько вам лет?')
def ask_age(input_age):
    if int(input_age) < 6:
        print('Иди в детский сад')
    elif int(input_age) > 6:
        print('Иди в школу')
    elif int(input_age) > 16:
        print('Иди в ВУЗ')
    elif int(input_age) > 22:
        print('Иди работать')
    else input_age:
        print('введите цифры')
ask_age(input_age)
