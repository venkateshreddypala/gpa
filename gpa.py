print ('Please enter your grades one per line')
#map letter to point values
points = {'A':4, 'B':3, 'C':1, 'F':0}
num_courses = 0
total_points =0 
done = False
while not done:
    grade = input()
    if grade == '':
        done =True
    elif grade not in points:
        print ("Unknown grade'{0}' beign ignore".format(grade))
    else:
        num_courses = num_courses+ 1
        total_points = total_points+ points[grade]
    if num_courses>0:
        print('Your GPA is {0:.3}'.format(total_points/num_courses))