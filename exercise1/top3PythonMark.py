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
average1

def pass_or_fail(marks):
    passmark=50
    passedStudents=[]
    failedStudents=[]
    for mark in marks:
        if int(mark)>=passmark:
            passedStudents.append(int(mark))
        else:
            failedStudents.append(int(mark))
    return passedStudents,failedStudents
#getting the total no of students in each department
dept1Total=int(input("Enter the no of students in dep 1:"))
dept2Total=int(input("Enter the no of students in dep 2:"))
dept3Total=int(input("Enter the no of students in dep 3:"))
#getting their marks in exam for each department
print("Enter the marks separated by commas")
marksDept1=input("Enter the final exam mark of student of dep 1:")
marksDept1=marksDept1.split(",")
marksDept2=input("Enter the final exam mark of student of dep 2:")
marksDept2=marksDept2.split(",")
marksDept3=input("Enter the final exam mark of student of dep 3:")
marksDept3.split(",")
for i in range
#sorting the marks of the students
marksDept1.sort()
marksDept2.sort()
marksDept3.sort()
marks_tot.sort()
#finding the maximum 3 marks
top_of_dep1=marksDept1[-3:]
top_of_dep2=marksDept2[-3:]
top_of_dep3=marksDept3[-3:]
top_of_all_dep=marks_tot[-3:]
# calling function pass or fail calling
a=pass_or_fail(marksDept1)
b=pass_or_fail(marksDept2)
c=pass_or_fail(marksDept3)
d=pass_or_fail(marks_tot)
# average calculation
avg1=sum(a[0])/len(a[0])
avg2=sum(b[0])/len(b[0])
avg3=sum(c[0])/len(c[0])
totalAvg=sum(d[0])/len(d[0])
#finding the least number of students
leastMark1=len(a[1])
leastMark2=len(b[1])
leastMark3=len(c[1])
fails=[leastMark1,leastMark2,leastMark3]
for zzzzzz

print(f"The top 3 marks in class 1 ={top_of_dep1}")
print(f"The top 3 marks in class 2 ={top_of_dep2}")
print(f"The top 3 marks in class 3 ={top_of_dep3}")
print(f"The top 3 marks in total class of combination ={top_of_all_dep}")
print(f"Average mark in class 1 ={avg1}")
print(f"Average mark in class 2 ={avg2}")
print(f"Average mark in class 3 ={avg3}")
print(f"Average mark in  total classes ={totalAvg}")
print(f"Least number of failed students in class 1 ={leastMark1}")
print(f"Least number of failed students in class 2 ={leastMark2}")
print(f"Least number of failed students in class 3 ={leastMark3}")
print(f"Least number of failed students in total class  ={least}")
