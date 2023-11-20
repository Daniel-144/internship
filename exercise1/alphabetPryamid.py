"""
Generate the following output using for loop. Go until g.
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba
"""
rang=int(input("enter the range of pyramid:"))
alpha=97
char=""
for i in range(0,7):
    print(char+chr(alpha)+char(alpha+i)+char)
    print()
    char=(char+chr(alpha+i)+char)



