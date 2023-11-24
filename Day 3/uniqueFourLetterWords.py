"""
Problem #3
From the same file as above, read from the file, count the number of unique 4 letter words and it no of occurrences
for each word. Write this information at the end of file under the heading "Summary of 4 letter words"
"""
import re
# initialize a empty string.
passage=""
fourLetterWords=[]
fourLetterWordscount=[]
try:
    # initialize a empty list to store the words.
    wortdsWithoutAinBetween=[]
    with open('C:\\Users\\sugav\\OneDrive\\Desktop\\sayur\\internship\\Day 3\\passage.txt','r') as file:
        # loop to store the words in the empty string.
        for words in file:
            passage += words
    passage=re.sub('[^a-zA-Z0-9]+'," ",passage)
except TypeError as e:
    print(f"error: {e}")
except Exception as e:
    print(f"unexpected error: {e}")
# to avoid case sensitivity.
passage = passage.lower()
# using split function to split the passage into a list.
passage=passage.split(" ")
try:
    # loop to count the number of 4 letter words in the passage.
    for i in range (len(passage)):
        if len(passage[i])==4:
            fourLetterWords.append(passage[i])
    fourLetterWordNonRepeated=list(set(fourLetterWords))
    for j in range(len(fourLetterWordNonRepeated)):
        fourLetterWordscount.append(fourLetterWords.count(fourLetterWordNonRepeated[j]))
except TypeError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"unexpected error: {e}")
print("summary of 4 letter words")
for i in range(len(fourLetterWordNonRepeated)):
    print(f"{fourLetterWordNonRepeated[i]} : {fourLetterWordscount[i]}",end=" ")
    if fourLetterWordscount[i] == 1:
        print(f" The word is present in the passage only one time",end="")
    else:
        print(f"The word is present in the passage more than 1 time.",end=" ")
    print()




"""
summary of 4 letter words
shot : 1  The word is present in the passage only one time.
went : 2 The word is present in the passage more than 1 time. 
deer : 1  The word is present in the passage only one time.
king : 3 The word is present in the passage more than 1 time. 
next : 1  The word is present in the passage only one time.
with : 1  The word is present in the passage only one time.
wife : 1  The word is present in the passage only one time.
"""


