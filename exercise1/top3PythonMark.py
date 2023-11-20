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

def is_correct(dep,value,total):
    if len(value)< total:
        print(f"You have left some marks in class{dep}.")
        print(f"The total marks is {total}. But you have entered {len(value)} marks.")
    elif len(value)> total:
        print(f"You have added some extra marks in class{dep}.")
        print(f"The total marks is {total}. But you have entered {len(value)} marks.")
def pass_or_fail(marks):
    passmark=50
    pass_std=[]
    fail_std=[]
    for mark in marks:
        if int(mark)>=passmark:
            pass_std.append(int(mark))
        else:
            fail_std.append(int(mark))
    return pass_std,fail_std
#getting the total no of students in each department
dep_1_tot=int(input("Enter the no of students in dep 1:"))
dep_2_tot=int(input("Enter the no of students in dep 2:"))
dep_3_tot=int(input("Enter the no of students in dep 3:"))
#getting their marks in exam for each department
print("Enter the marks separated by commas")
marks_dep_1=input("Enter the final exam mark of student of dep 1:").split(',')
cr1=is_correct(1,marks_dep_1,dep_1_tot)
marks_dep_2=input("Enter the final exam mark of student of dep 2:").split(',')
cr2=is_correct(2,marks_dep_2,dep_2_tot)
marks_dep_3=input("Enter the final exam mark of student of dep 3:").split(',')
cr3=is_correct(3,marks_dep_3,dep_3_tot)
marks_tot= marks_dep_1+marks_dep_2+marks_dep_3
#sorting them in ascending order
marks_dep_1.sort()
marks_dep_2.sort()
marks_dep_3.sort()
marks_tot.sort()
#finding the maximum 3 marks
top_of_dep1=marks_dep_1[-3:]
top_of_dep2=marks_dep_2[-3:]
top_of_dep3=marks_dep_3[-3:]
top_of_all_dep=marks_tot[-3:]
#function pass or fail calling
a=pass_or_fail(marks_dep_1)
b=pass_or_fail(marks_dep_2)
c=pass_or_fail(marks_dep_3)
d=pass_or_fail(marks_tot)
#finding the average
avg_1=sum(a[0])/len(a[0])
avg_2=sum(b[0])/len(b[0])
avg_3=sum(c[0])/len(c[0])
tot_avg=sum(d[0])/len(d[0])
#finding the least number of students
least_1=len(a[1])
least_2=len(b[1])
least_3=len(c[1])
tot_least=len(d[1])
print(f"The top 3 marks in class 1 ={top_of_dep1}")
print(f"The top 3 marks in class 2 ={top_of_dep2}")
print(f"The top 3 marks in class 3 ={top_of_dep3}")
print(f"The top 3 marks in total class of combination ={top_of_all_dep}")
print(f"Average mark in class 1 ={avg_1}")
print(f"Average mark in class 2 ={avg_2}")
print(f"Average mark in class 3 ={avg_3}")
print(f"Average mark in  total classes ={tot_avg}")
print(f"Least number of failed students in class 1 ={least_1}")
print(f"Least number of failed students in class 2 ={least_2}")
print(f"Least number of failed students in class 3 ={least_3}")
print(f"Least number of failed students in total class  ={tot_least}")
