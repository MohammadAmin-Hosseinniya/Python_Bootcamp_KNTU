course_name = ['riazi' , 'fizik' , 'zist' , 'zaban']
course_score = []

for course in course_name:
    course_score.append(float(input('nomreye darse {} chand mi bashad? '.format(course))))

sum_score = sum(course_score)
number_of_courses = len(course_score)
moadel = sum_score / number_of_courses

print ('moadele shoma dar in 4 dars barabare : {}  mi bashad'.format(moadel))
