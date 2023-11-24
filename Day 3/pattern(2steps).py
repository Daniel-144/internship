"""
Observe how the nunmbers in the triangle are calculated. 
Do it in two steps. Work on the generating the numbers first in right angle triangle
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
"""
rows=int(input("enter the number of rows:"))
#step 1:(printing in right angled triangle):
print("STEP 1: SIMPLE RIGHT ANGLED PATTERN")
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print()
print("STEP 2:EXACT PATTERN")
for i in range(1,rows+1):
    num=1
    for j in range(1,i+1):
        print(num,end=" ")
        num=num*(i-j)//j
    print()

"""
OP:
enter the number of rows:5
STEP 1: SIMPLE RIGHT ANGLED PATTERN
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

STEP 2:EXACT PATTERN
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
"""




        