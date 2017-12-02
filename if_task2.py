str1 = input('string1')
str2 = input('string2')

def two_strings(str1, str2):
    if str1 == str2:
        print('1')
    elif str1 != str2:
        if len(str1) > len(str2):
            print('2')
        elif str2 == 'learn':
            print('3')

two_strings(str1, str2)


