"""
Problem #1
Print the following pattern
1
212
32123
4321234
543212345
Get user input for how far to go (up to 0)
"""
n = int(input("Enter the number of rows (up to 9): "))

for i in range(1, n + 1):
    # loop to Print decreasing numbers
    for k in range(i, 0, -1):
        print(k, end="")
    # example OP of the above  loop.
    """
    1
    21
    321
    4321
    """
    # loop to Print increasing numbers
    for l in range(2, i + 1):
        print(l, end="")
    # to print new line
    print()
    # example Op of the above loop .
    """
    
    2
    23
    234
    """

"""
OP:
Enter the number of rows (up to 9): 5
1
212
32123
4321234
543212345
"""
