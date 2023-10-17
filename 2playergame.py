"""
Problem #2
You have 6 x 6 game board where each cell is shown as a *
This is a two player dice game. The die has numbers 1 to 6.
Each player rolls the dice twice. First roll is row number, second roll is col number.
After the player rolls the dice, in the (row,col) enter the player's initial. 
If the player  A rolls the dice and  if  player B already has their initial in the same row,col
add a point to A and change the initial to A. 

Player who gets 5 points first wins the game.
"""
# imported random 
import random
# initialized points to 0
player1point=0
player2point=0
# getting name as the input from the user
player1name=input("enter your name:")
player2name=input("enter your name:")
# initialized board as a list (2d array in python caused more trouble so i have chosen list instead of array but it gave me the exact output).
board=["*"]*36
# initialized count to count the number of rounds
count=0
# we dont know how many iterations it will take so i have used the while loop
while(True):
    # conditional statement to check if the
    if(player1point<=5 and player2point<=5):
        # incrementr the count(round)
        count+=1
        # use randint from the random package to generate a random integer
        Arow=random.randint(1,6)
        Acol=random.randint(1,6)
        Brow=random.randint(1,6)
        Bcol=random.randint(1,6)
        # check if player 2 name is already in the given index
        if board[(Arow*Acol)-1]==player2name[0]:
            # increment the point of player 1
            player1point+=1
            board[(Arow*Acol)-1]=player1name[0]
            print(f"player1 earned a point| points:{player1point}")
        # to check if player 1 name is already in the given index.
        elif board[(Brow*Bcol)-1]==player1name[0]:
            # increment the point of payer 2
            player2point+=1
            board[(Brow*Bcol)-1]=player2name[0]
            print(f"player2 earned a point| points:{player2point}")
        # if we got a unique index print the first letter of the player name in that index.
        else:
            board[(Arow*Acol)-1]=player1name[0]
            board[(Brow*Bcol)-1]=player2name[0]
        # loop to print the result of the round.
        for i in range(0,len(board),6):
            # * is used to unpack the list and we have used slicing to crate a sublist and print it into 6 rows.
            print(*board[i:i + 6])
        print(f"Round{count+1}")
    else:
        break
# loop to print the final form of the board.
for j in range(0,len(board),6):
    # * is used to unpack the list and we have used slicing to crate a sublist and print it into 6 rows
    print(*board[j:j + 6])
print()
# conditional statement to check who is the winner.
if player1point > player2point:
    print(f"player 1 {player1name} wins")
if player2point > player1point:
    print(f"player 2 {player2name} wins")

"""
Op:
enter your name:Daniel
enter your name:Haniman
* * H * * *
* * * * * *
* * * * * *
* * * * * *
D * * * * *
* * * * * *
Round2
* * H H * *
* * * * * *
* * * * * D
* * * * * *
D * * * * *
* * * * * *
Round3
player1 earned a point| points:1
* * H D * *
* * * * * *
* * * * * D
* * * * * *
D * * * * *
* * * * * *
Round4
* * H D * D
* * * * * *
* * * * * D
* * * * * H
D * * * * *
* * * * * *
Round5
* * H D * D
* * * * * D
* * H * * D
* * * * * H
D * * * * *
* * * * * *
Round6
* H H D * D
* * * D * D
* * H * * D
* * * * * H
D * * * * *
* * * * * *
Round7
* H H D * D
* * * D * D
* * H * * D
* * * * * H
D * * * * *
* * * * * *
Round8
player2 earned a point| points:1
* H H H * D
* * * D * D
* * H * * D
* * * * * H
D * * * * *
* * * * * *
Round9
* H H H H D
* * * D * D
* * H * * D
* * * * * H
D * * * * D
* * * * * *
Round10
player1 earned a point| points:2
* D H H H D
* * * D * D
* * H * * D
* * * * * H
D * * * * D
* * * * * *
Round11
* D H H H D
* H * D * D
* * H * * D
* * * * * H
D * * * * D
* * * * * *
Round12
* D H H H D
* H * D * D
* * H * * D
* * * * * H
D * * * * D
* * * * * *
Round13
player1 earned a point| points:3
* D H H D D
* H * D * D
* * H * * D
* * * * * H
D * * * * D
* * * * * *
Round14
player2 earned a point| points:2
* H H H D D
* H * D * D
* * H * * D
* * * * * H
D * * * * D
* * * * * *
Round15
player1 earned a point| points:4
* H D H D D
* H * D * D
* * H * * D
* * * * * H
D * * * * D
* * * * * *
Round16
player2 earned a point| points:3
* H D H H D
* H * D * D
* * H * * D
* * * * * H
D * * * * D
* * * * * *
Round17
* H D H H D
* H * D * D
* * H * * D
* D * * * H
D * * * * D
* * * * * *
Round18
player2 earned a point| points:4
* H D H H D
* H * D * D
* * H * * D
* H * * * H
D * * * * D
* * * * * *
Round19
player1 earned a point| points:5
* H D D H D
* H * D * D
* * H * * D
* H * * * H
D * * * * D
* * * * * *
Round20
player1 earned a point| points:6
* H D D H D
* H * D * D
* * H * * D
* D * * * H
D * * * * D
* * * * * *
Round21
* H D D H D
* H * D * D
* * H * * D
* D * * * H
D * * * * D
* * * * * *

player 1 Daniel wins

"""