#leap year checker in python 

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('It is a leap year!' )
            else:
                print('It is not a leap year')
        else:
            print('It is a leap year!' )
    else:
        print('It is not a leap year')
        
is_leap_year(2023)
