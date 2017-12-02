names = ['john', 'antony', 'melanie', 'sid', 'kira', 'eddie', 'donald', 'sid']
while names:
    if names.pop() == 'sid':
        print('we got him!')
        break
a = names.index('sid')
print('''sid's index is ''' + str(a))

