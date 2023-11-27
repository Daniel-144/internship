"""
Problem #1
write a program that reads a passage and reverses the order of
letters in each word while keeping the word order intact. Use function.
Eg- input - I am Sayur
output I ma ruyaS
"""
# function to reverse the words.
def reversedWords(tempstring):
    # initializing the count variable for indexing.
    count=0
    for i in tempstring:
        # replacing the elements of tempstring by the reversed element. 
        tempstring[count]=i[::-1]
        # count for indexing
        count+=1
    # join the words to convert the list into a string.
    tempstring= " ".join(tempstring)
    return tempstring
        
# initialize a empty string to store the words from the text file
string=""
# to open the file (passage.txt) as file
with open('C:\\Users\\sugav\\OneDrive\\Desktop\\sayur\\internship\\Day 4\\passage') as file:
    # loop to store the words in the file
    for words in file:
        string+=words
# use split function to split the words in the passage and store it as a list
tempstring=string.split(" ")
# calling the reverse function to reverse the words in the list.
encodedString=reversedWords(tempstring)

print(f"INPUT: {string}")
print(f"OUTPUT: {encodedString}")

"""
OP:
INPUT: I am Sayur
OUTPUT: I ma ruyaS

"""




