"""
In the input, find the first A and last A, print all the letters between  these two A.
If there no A or 2nd A is not found, find the first B and second B and prinyt all the letters between these two B.
If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C.
"""

# Function to find the letters between the two given alphabet.
def FindTheLettersBetween2Letters(inputString,alpha):
    if (alpha in inputString):
        # fining the index of first alphabet and the last alphabet.
        FirstAlpha=inputString.find(alpha)
        LastAlpha=inputString.rfind(alpha)
        # if the index of the first alphabet and the last alphabet  are  same then there is only one found.
        if (FirstAlpha == LastAlpha):
            print("There is no A after the first A")
            return(False)
        # it has more than one occurance so we can print the intermediate letters.
        else:
            print(f"The Letters between two {alpha} is :'{inputString[FirstAlpha+1:LastAlpha]}'")
            return(True)
    # no given alphabet is found in the string
    else:
        print(f"There is no {alpha} FOund")
        return(False)


# getting string from the user.
string=input("enter the string:")
# ascii value of letter "a".
#alph=97
string=string.lower()
for alph in range(97,101):
    #if(FindTheLettersBetween2Letters(string,chr(alph))==False):
    condition=FindTheLettersBetween2Letters(string,chr(alph))
    if condition == True:
        break
        
    
        

"""
1)enter the string:apple and orange
The Letters between two a is :'pple and or'

2)enter the string:a boy , borrow
There is no A after the first A
The Letters between two b is :'oy , '

3)enter the string:carrom cot creed
There is no A after the first A
There is no b FOund
The Letters between two c is :'arrom cot '
"""