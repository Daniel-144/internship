"""
Problem #2
Write a program that reads a passage or string and counts the occurrences of two consecutive words 
that are the same without any other specific word in between.
 For example, count the occurrences of "apple apple" but not "apple orange apple."
"""
passage=input("enter tghe passage:")
listOfWords=passage.split(" ")
consecutiveWords=0
for i in range(len(listOfWords)-1):
    if listOfWords[i] == listOfWords[i+1]:
        print(f"consecutive word found!! {listOfWords[i]} and {listOfWords[i+1]}")
        consecutiveWords+=1
print(f"No.of consecutive words found:{consecutiveWords}")


"""
Op:
enter tghe passage:apple apple orange apple orange orange
consecutive word found!! apple and apple
consecutive word found!! orange and orange
No.of consecutive words found:2

enter tghe passage:apple orange apple
No.of consecutive words found:0
"""
