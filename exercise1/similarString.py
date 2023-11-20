"""
problem #4
write a program to find if two strings are same.
two string are considered same if both strings have same letters in same order, but from different starting point
eg abcd is same as bcda (a is moved to the right)
abcd is same as cdab 
abcd is  not same as cdba

123456 = 456123
123456 not = 412356
hint - 
there are many simple answers. you can try with slice function
"""
def DeterminingTheString(firstCharIndex,similarString,string):
    result=False
    for i in range(len(firstCharIndex)):
        print(string[firstCharIndex[i]:]+ string[0:firstCharIndex[i]])
        if (string[firstCharIndex[i]:]+ string[0:firstCharIndex[i]] == similarString ):
            result=True
    return(result)
            
firstCharIndex=[]
string=input("Enter a string:")
similarString=input("enter a string similar to 1st string:")
if (len(string)!=len(similarString)):
    print(f"Both string has different length. {string} and {similarString} are not same")
else:
    for i in string:
        if i not in similarString:
            print(f"{string} is not same as {similarString}")
    count=string.count(similarString[0])
    print(count)
    for s in range(len(string)):
        if similarString[0] is string[s]:
            firstCharIndex.append(s)
    print(firstCharIndex)
    result=DeterminingTheString(firstCharIndex,similarString,string)
    print(result)
    if result == True:
        print(f"{string} is same as {similarString}")
    else:
        print(f"{string} is not same as {similarString}")
            




