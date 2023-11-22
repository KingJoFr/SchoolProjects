change = int(input('input how much change:'))

#gives number of dollars
dollars = change//100
#calculates whats left after dollars taken out
left_over = change%100
quarters = (left_over)//25
left_over = left_over -(quarters*25)
dimes = (left_over)//10
left_over = left_over-(dimes*10)
nickles = left_over//5
left_over = left_over-(nickles*5)
pennies = left_over

#if change is 0 or negative prints "no change"
if change <= 0:
    print('No change')
else:

    #calculates if there is one multiple of a coin and print the corresponding singular or plural word
    # if its 0 nothing is printed
    if dollars == 1:
        print(dollars,'Dollar')
    elif dollars > 0:
        print(dollars,'Dollars')

    if quarters ==1 :
        print(quarters,'Quarter')
    elif quarters > 0:
        print(quarters,'Quarters')

    if dimes == 1:
        print(dimes,'dime')
    elif dimes > 0:
        print(dimes,'Dimes')

    if nickles == 1:
        print(nickles,'Nickle')
    elif nickles > 0:
        print(nickles,'Nickles')

    if pennies == 1:
        print(pennies,'Penny')
    elif pennies > 0: 
        print(pennies,'Pennies')



