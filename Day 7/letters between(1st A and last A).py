"""
find the letters between the first a and last a and print them.
"""

# function to print the first a and last a and print the intermediate letters
def theLettersBetweenFirstAandLastA(string,alpha):
    # conditional statement to check if there is a 'a' in given string
    if "a" in string:
        # first index
        FirstAIndex=string.find(alpha)
        LastAIndex=string.rfind(alpha)
        if (FirstAIndex == LastAIndex):
            print("no letters between first A and Last A.")
        else:
            print(f"the letters between '{alpha}'{string[FirstAIndex+1:LastAIndex]}")
    else:
        print("There is No A in the given string.")

    


  
inputString=input("enter any string:")
# converting the string to lower case to get rid of errors due to  case sensitivity.
alpha="a"
inputString=inputString.lower()
# calling the function to  print the intermediate letters.
theLettersBetweenFirstAandLastA(inputString,alpha)



