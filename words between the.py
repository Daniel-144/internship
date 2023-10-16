"""
Problem #1
Read a passage from a file. (If you don't know how to handle files in Python, you can hardcode a long passage)
Count the number of times the word 'the' followed by another 'the' without 'a' in between.

Eg The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.

answer is 4 (The king, the forest, The King the next).
"""
passage="The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day."
# changed the passage to lower case to make the string case insensitive
passage=passage.lower()
# used stip function to strip the passage with the word "the" ex: he is the hero :[he is,hero]
print("the passage is:",passage)
passage=passage.split("the")
# if there is a the present as the first word then empty character will be appended in a string so we use remove to remove the empty chracter
passage.remove("")
count=0
# loop to iterate through the list
for i in range(len(passage)):
    #  conditional statement to find if there is a "a" present in the string
    if "a" not in passage[i]:
        # increment count
        count+=1
# output
print("the answer is:",count)
# the next day will not be taken into count because the word day has a "a" in it

"""
OP
the passage is: the king went to the forest with the wife and a servernt. the king shot a deer. the king went to the forest again the next day.
the answer is: 3
"""

