nouninput = input()
noun1 = nouninput.split()
noun = noun1[0]
num = noun1[1]


while noun != 'quit':
    print('Eating {} {} a day keeps the doctor away.'.format(num,noun,))
    nouninput = input()
    noun1 = nouninput.split()
    noun = noun1[0]
    num = noun1[1]
