# we want to calculate average of some scores for lessons
# first we have to input score for each course
riazi = input(' lotfan nomre riazi ra vared konid: ')
fizik = input(' lotfan nomre mounth ra vared konid: ')
zist = input(' lotfan nomre zist ra vared konid: ')
zaban = input(' lotfan nomre zaban ra vared konid: ')

# define numbers of courses
numbers = 4

# change type of input to float
riazi = float(riazi)
fizik = float(fizik)
zist = float(zist)
zaban = float(zaban)

# define sum of numbers
sum_scores = riazi + fizik + zist + zaban

# calculate the average
average = sum_scores / numbers

# output the resault
print(' The average of the scores is : ', average)





