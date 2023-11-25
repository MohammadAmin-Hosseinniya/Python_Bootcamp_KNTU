# we want to calculate what percentage of the year has passed?
# first we have to input date od today
day = input(' emrooz chandomin rooze mahe? ')
month = input(' mahe chandome? ')

# change type of input to float
day = float(day)
month = float(month)

# calculate the percentage
if 0 < month <= 6:
    dayofyear = ((month - 1) * 31) + day

elif 6 < month <= 11:
    dayofyear = (6 * 31) + ((month - 7) * 30) + day

elif month == 12:
    dayofyear = (6 * 31) + (5 * 30) + day

else:
    print(' adade mah ro dorost vared nakardi !!! ')

if day <= 0 or day >= 32:
    print('adade rooz ro dorost vared nakardi !!!')

per_of_year = dayofyear / 365 * 100

# output the resault
print(' today we passed ', per_of_year, '%', ' of the year')
