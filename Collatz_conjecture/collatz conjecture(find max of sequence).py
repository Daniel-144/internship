"""
#Problem #3
Get a input. Create a sequence of numbers from that input using the above alg.
Find the largest number in the sequence. 
"""

num=int(input("enter the number: "))
number_for_itteration=num
count=0
list=[]
while number_for_itteration !=1:
    count+=1
    if number_for_itteration % 2 ==0:
        number_for_itteration=number_for_itteration//2
    else:
        number_for_itteration=(number_for_itteration*3)+1
    print(number_for_itteration,end=",")
    list.append(number_for_itteration)
print()
print(f"Total number of itteration:{count}")
print(f"the maximum number in the sequence is {max(list)}")

"""
OP:
enter the number: 9
28,14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1,
Total number of itteration:19
the maximum number in the sequence is 52
"""

