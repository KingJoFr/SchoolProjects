#get month from user
input_month = input('input month:')
#get day from user
input_day = int(input('input day:'))
#create day ranges for seasons
days = list(range(0, 366))

#lowercase input month to match the dictionary
month = input_month.lower().strip()

#create dictionary of months to match list of days
months_dict = {'january': 0, 'febuary': 1, 'march': 2, 'april': 3, 'may':4, 'june': 5,'july': 6,'august': 7, 'september': 8,'october': 9,'november': 10,'december':11}
# list of days for each month
months_days = (31, 28, 31, 30, 31, 30,31,31,30,31,30,31)

# days of year matched to a season
winter1 = list(range(0,79))
winter2 = list(range(355,365))
spring  = list(range(79,172))
summer  = list(range(172,265))
autumn  = list(range(265,355))

#check if input month is in month dictionary
if month in months_dict:
    print('month is in months_dict')
    # checks to make sure that number mathces a day in the month
    index_of_month =months_dict[month]
    if input_day <= months_days[index_of_month] and input_day > 0:
        print(index_of_month, index_of_month-1)
        # if months is past january does this
    
        print('sum of the days from 0 to:', month,sum(months_days[:index_of_month]))
        day_of_year = sum(months_days[:index_of_month]) + input_day
        print('input day is:', input_day)
        print('sum of months:', sum(months_days[:index_of_month]))
        print('the day of the year is:', day_of_year)
        if day_of_year in winter1 or day_of_year in winter2:
            print('the season is winter')
        elif day_of_year in summer:
            print('summer')
        elif day_of_year in autumn:
            print('autumn')
        elif day_of_year in spring:
            print('spring')
        
        
            
    else:
        print('Invalid')
else:
    print('Invalid')
