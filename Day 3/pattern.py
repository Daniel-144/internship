"""
Problem 1:
print the following pattern.
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
"""
# range of the pattern
rows=int(input("enter the range of the pattern:"))
for i in range(1,rows+1):
    num=1
    # to print the spaces.
    print(f"{' '*(rows-i)}",end="")
    for j in range(1,i+1):
        print(num,end=" ")
        num=num*(i-j)//j
    print()


"""
OP:
enter the range of the pattern:5
    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1 
"""



