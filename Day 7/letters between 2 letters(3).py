"""
problem 3:
In the input the first A and last A, print all the letters between those two A.
If there is no A or 2nd A is not found, Find the first B after the first A (if there is a A) and last last B and print all letters between these two B.
If there is no B or 2nd B is not found, Find the first C after the first B (if there is a B) and last last C and print all letters between these two C.
"""
# Finding if the given alphabet is present in the string.
def findAlpha(ipstring,alpha):
    if alpha in ipstring:
        return(True)
    else:
        print(f"NO {alpha} found")
        return(False)

# function to find if there is one or more occurence.
def find2Alpha(ipstring,alpha):
    #to find first index
    FirstAlphaIndex=ipstring.find(alpha)
    # to find last index
    LastAlphaIndex=ipstring.rfind(alpha)
    if FirstAlphaIndex == LastAlphaIndex:
        print(f"only one {alpha} found.")
        return(False)
    else:
        return(True)

# function to print the words between the given alphabet.
def PrintIntermediateLetters(ipstring,alpha):
    # To find first index
    FirstAlphaIndex=ipstring.find(alpha)
    # To find last index
    LastAlphaIndex=ipstring.rfind(alpha)
    print(f"the letters between the given alphabet {alpha} is : '{ipstring[FirstAlphaIndex+1:LastAlphaIndex]}'")

# if there is only one occurence this function returns the address of the first occurance(will be used to slice the string).
def slicingString(ipstring,alpha):
    FirstAlphaIndex=ipstring.find(alpha)
    return(FirstAlphaIndex)


# input from the user.
string=input("enter any string:")
# ascii value of the letter "a"
#alpha=97
# converting the string to lower case to get rid of errors due to  case sensitivity.
string=string.lower()
for alpha in range(97,101):
    if(findAlpha(string,chr(alpha)) == True):
        if(find2Alpha(string,chr(alpha)) == True):
            PrintIntermediateLetters(string,chr(alpha))
            break
        else:
            # string is sliced after the first occurance.
            string=string[slicingString(string,chr(alpha))+1:]


"""
1)enter any string:as deep as the pacific ocean      
the letters between the given alphabet a is : s deep as the pacific oce

2)enter any string:baby boss
only one a found.
the letters between the given alphabet b is : y 

3)enter any string:computer commerce
NO a found
NO b found
the letters between the given alphabet c is : omputer commer

4)enter any string:computer coma commerce course
only one a found.
NO b found
the letters between the given alphabet c is : ommerce

"""


