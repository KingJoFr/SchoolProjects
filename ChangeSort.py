change = int(input('input how much change:'))

#gives number of num_num_dollars
num_dollars = change//100
#calculates whats left after num_dollars taken out
left_over = change%100
num_quarters = (left_over)//25
left_over = left_over -(num_quarters*25)
num_dimes = (left_over)//10
left_over = left_over-(num_dimes*10)
num_nickels = left_over//5
left_over = left_over-(num_nickels*5)
num_pennies = left_over

#if change is 0 or negative prints "no change"
if change <= 0:
    print('No change')
else:

    #calculates if there is one multiple of a coin and print the corresponding singular or plural word
    # if its 0 nothing is printed
    if num_dollars == 1:
        print(num_dollars,'Dollar')
    elif num_dollars > 0:
        print(num_dollars,'dollars')

    if num_quarters ==1 :
        print(num_quarters,'Quarter')
    elif num_quarters > 0:
        print(num_quarters,'quarters')

    if num_dimes == 1:
        print(num_dimes,'dime')
    elif num_dimes > 0:
        print(num_dimes,'dimes')

    if num_nickels == 1:
        print(num_nickels,'Nickle')
    elif num_nickels > 0:
        print(num_nickels,'nickels')

    if num_pennies == 1:
        print(num_pennies,'Penny')
    elif num_pennies > 0: 
        print(num_pennies,'pennies')



