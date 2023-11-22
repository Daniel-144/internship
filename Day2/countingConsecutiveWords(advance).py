"""
Problem #2
Write a program that reads a passage or string and counts the occurrences of two consecutive words 
that are the same without any other specific word in between.
 For example, count the occurrences of "apple apple" but not "apple orange apple."
"""
string=input("enterthe string:")
word = string.split(" ")
occuranceDict={}
consecutiveWords=0

for i in range(0,len(word)-1):
    if (word[i] == word[i+1]):
        consecutiveWords+=1
        repeatedWord=word[i]
        if repeatedWord in occuranceDict:
            occuranceDict[repeatedWord] +=1
        else:
            occuranceDict[repeatedWord] = 1
    
print(f"Total number of consecutive words:{consecutiveWords}")
for element, count in occuranceDict.items():
    print(f"{element} is present in the string consecutively: {count} times")

"""
enterthe string:apple apple apple orange orange orange a a orange banana banana
Total number of consecutive words:6
apple is present in the string consecutively: 2 times
orange is present in the string consecutively: 2 times
a is present in the string consecutively: 1 times
banana is present in the string consecutively: 1 times
"""