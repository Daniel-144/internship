"""
Generate the following output using for loop. Go until g.
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba
"""
# initializing start and end points
start='a'
end='g'
temp=start
# while loop to print the pattern
while (ord(start) <= ord(end)):
    print(temp)
    start=chr(ord(start)+1)
    temp=temp+start+temp


"""
OP:
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba
abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacabagabacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
"""



