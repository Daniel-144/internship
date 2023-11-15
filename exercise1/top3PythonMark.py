"""
problem #5
In your college Python is taught in 3 different departments by the same professor. 
For each dept, get the no of students stutying Python and their marks in the final exam 
Get the input as comma seperated string

Find the top 3 marks in each class
Find the top 3 marks if all classes are combined.
Find the avg mark of students with passing mark in each class and the classes combined.
Find which class has the best average mark and least number of failed students.
"""
noStudentsInDept1=int(input("enter the number of students in department 1:"))
noStudentsInDept2=int(input("enter the number of students in department 2:"))
noStudentsInDept3=int(input("enter the number of students in department 3:"))
Dept1pyMarks=input("enter the marks of the students of Dept1(separated by comma):")
Dept2pyMarks=input("Enter the marks of the students of Dept2(separated by comma):")
Dept3pyMarks=input("Enter the marks of the students of Dept3(separated by comma):")
Dept1pyMarks=Dept1pyMarks.split(",")
Dept2pyMarks=Dept2pyMarks.split(",")
Dept3pyMarks=Dept3pyMarks.split(",")
Dept1pyMarks.sort()
Dept2pyMarks.sort()
Dept3pyMarks.sort()
print(Dept1pyMarks,Dept3pyMarks)