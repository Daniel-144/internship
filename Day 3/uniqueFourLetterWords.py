"""
Problem #3
From the same file as above, read from the file, count the number of unique 4 letter words and it no of occurrences
for each word. Write this information at the end of file under the heading "Summary of 4 letter words"
"""
try:
    myDict={}
    # initialize a empty list to store the words.
    wortdsWithoutAinBetween=[]
    inputPassage=open('C:\\Users\\sugav\\OneDrive\\Desktop\\sayur\\internship\\Day 3\\passage.txt','r')
    passage=inputPassage.read()
    passage=passage.split()
    for words in passage:
        if len(words)==4 and words not in myDict:
            count=passage.count(words)
            myDict[words]=count
    with open('C:\\Users\\sugav\\OneDrive\\Desktop\\sayur\\internship\\Day 3\\passage.txt','w') as file:
        file.write("\nSUMMARY OF 4 LETTER WORDS\n")
        for key,occurances in myDict.items():
            file.write(f"{key}:{occurances}\n")
    print("SUMMARY OF 4 LETTER WORDS")
    for key,occurances in myDict.items():
        print(f"{key}:{occurances}")
except:
    print("file name may be incorrect or not found.")
finally:
    print("the above details are appended in the file.")


"""
OP
SUMMARY OF 4 LETTER WORDS
king:3
went:2
with:1
wife:1
shot:1
next:1
day.:1
the above details are appended in the file.
"""


