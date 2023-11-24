"""
Problem #2
Read a passage from a file.
Count the number of times the word 'the' followed by another 'the' without 'a' in between.

Eg The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.

answer is 4 (The king, the forest, The King the next).
"""
# initialize a empty string.
passage=""
try:
    # initialize a empty list to store the words.
    wortdsWithoutAinBetween=[]
    with open('C:\\Users\\sugav\\OneDrive\\Desktop\\sayur\\internship\\Day 3\\passage.txt','r') as file:
        # loop to store the words in the empty string.
        for words in file:
            passage += words
except TypeError as e:
    print(f"error: {e}")
except Exception as e:
    print(f"Error occured: {e}")
# Change the passage to lowercase to make the string case insensitive
passage = passage.lower()

# Use strip function to strip the passage with the word "the" ex: he is the hero :[he is, hero]
print("The passage is:", passage)

try:
    # Split the passage using "the" as the delimiter
    passage = passage.split("the")

    # The first split will contain the word with only one "the," so we pop the word in index 0 and the last index
    # because there will be only one "the."
    if passage[0]=="":
       passage.pop(0)
    if passage[len(passage)-1]=="":
      passage.pop(len(passage) - 1)

    count = 0

    # Loop to iterate through the list
    for i in range(len(passage)):
        try:
            # Conditional statement to find if there is an "a" present in the string
            if "a" not in passage[i]:
                # Increment count
                count += 1
                # append the words in the list.
                wortdsWithoutAinBetween.append("The "+passage[i])
        except TypeError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Output
    print("The answer is:", count)
    print(f"The words are: {wortdsWithoutAinBetween}")
    # the next day will not be taken into count because the string has only one 'the'
    # forest again will not be taken into count because again has "a" in it.
except TypeError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occured: {e}")


"""
OP
The passage is: the king went to the forest with the wife and a servant. the king shot a deer. the king went to the forest again the next day.
The answer is: 3
The words are: ['The  king went to ', 'The  forest with ', 'The  king went to ']
"""

