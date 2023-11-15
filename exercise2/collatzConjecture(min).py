"""
Problem #2
Same as above.
Input two numbers.
Print which number has less steps to reach 1.
"""
# function to find the collatz_conjecture.
def calculate_collratz_conjecture(number):
    # initializing c=0 to count the number of iterations.
    c=0
    while(number!= 1):
        if number % 2 == 0:          # for even number , divide by 2(n/2)
            number = number//2
        else:                        # for odd number - 3n+1
            number = (3 * number)+1
        print(number,end=",")
        c+=1                         # incrementing the count (c) after each iterations.
    print()
    return(c)                        # the count is returned to the main function.


# initializing the lists to store the number and count
count = []
num = []
for i in range(2):
    num.append(int(input("enter the value: ")))            # the number is obtained as a input from the user and appended in the list
    count.append(calculate_collratz_conjecture(num[i]))    # the function is called and the argument(num[i]) is passed and the returned value is stored in the list
print(f"the number {num[count.index(min(count))]} became 1 after with minimum number of iterations({min(count)} times).")


"""
OP:-
enter the value: 8
4,2,1,
enter the value: 12
6,3,10,5,16,8,4,2,1,
the number 8 became 1 after with minimum number of iterations(3 times).
"""