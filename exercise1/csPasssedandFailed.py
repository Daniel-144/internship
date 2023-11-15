"""
Problem #2
you have a list of student names and another list with their marks in CS. 
hard code the values. no need to get it as input
Pass mark is 50.
Print a new list with all the students with pass marks along with their mark in the format name:mark.
Also print the number of students who failed.
"""
StudentName=['messi','sergio ramos','ronaldo','tony kroos','belingham']
StudentMark=[34,56,78,23,90]
PassMark=50
failcount=0
# initializing a list to store the students with passmark
PassList=[]
# loop to find the number of students who got fail mark and to store the name and mark of students with pass mark in a list
for mark in range(len(StudentMark)):
    if StudentMark[mark]>=50:
        # if student got pass mark in all subjects their mark and their name are stored in a list.
        PassList.append(StudentName[mark]+':'+str(StudentMark[mark]))
    else:
        failcount+=1

print(f"pass student's name and markks:{PassList}")
print(f"No of student's failed:{failcount}")

"""
OP
pass student's name and markks:['sergio ramos:56', 'ronaldo:78', 'belingham:90']
No of student's failed:2
"""
