print('Hello, who are you? ')
name = input(str())
if name[:4].lower() == 'sir ':
    print('hello, ' + name, 'good to meet you')
else:
    print('hello, Sir ' + name, 'good to meet you')
