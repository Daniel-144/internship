"""
Problem #1
Write a program for Collatz_conjecture.
Collatz_conjecture means -  start with the input number. 
For even number , divide by 2 (n/2)
For odd number - 3n + 1
apply the above for the result number until the answer is 1.

Eg, input is 8
8, 4,2, 1
input is 9
9,28,14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1
"""
def collatzconjecture(num):
    c=0                         # count is initialized as c
    while num!=1:
        c+=1
        if (num % 2)==0:        # if the number is a even number the number should be divided by 2
            num=num//2
        else:                   # if the number is a odd number the number should be multiplied by 3 and added with 1.
            num=3*num+1
        print(f"{num}",end=",") # print statement to print the value after each itteration.
    print()
    return c                    # the count value is returned to the main function.

num=int(input("enter the number:"))
print(f"the number {num} became 1 after {collatzconjecture(num)} times") # the function collatz conjecture is called inside the print statement.

"""
Op:
enter the number:8
4,2,1,
the number 8 became 1 after 3 times
"""