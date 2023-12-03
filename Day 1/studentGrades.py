"""
Problem #3
you have a list of student names. you have one list each for their marks in CS, Math and English. 
hard code the values. no need to get it as input
Pass mark is 50.
Grade A is, mark 90 or above
Grade B , 80 or above
Fail is < 50
Print the name of the students who got A in all subjects or atleast one A and the rest B.
Try to use only one if statement.
"""
studentlist=['AB De villiers','surya kumar yadav','kohli','gill','rashid']
csmarks=[90,64,96,98,23] # cs marks
mathmark=[90,80,96,48,73] # maths mark
engmark=[86,100,96,88,83] # english marks
students_with_goodgrades=[]
# find the students if they have atleast 1 A grade and others with atleast B grade. 
for mark in range(len(csmarks)):
    if((csmarks[mark] >= 90 or mathmark[mark] >= 90 or engmark[mark] >= 90) and (csmarks[mark]>=80 and mathmark[mark]>=80 and engmark[mark] >= 80)):
        students_with_goodgrades.append(studentlist[mark])
print("students with atlest 80 marks in all subjects and with atleast only one a grade:",students_with_goodgrades)

"""
OP
students with atlest 80 marks in all subjects and with atleast only one a grade: ['AB De villiers', 'kholi']
"""