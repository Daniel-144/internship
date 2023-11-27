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
# function to create the pattern  of the board
def creatingBoard(board,dim):
    for i in range(0,dim):
        for j in range(0,dim):
            board[i].append('*')
    # calling display function to display the board.
    display(board)

# function to display the board.
def display(board):
    for outer in range(0,len(board)):
        for inner in range(0,len(board[outer])):
            print(f"{board[outer][inner]}",end=" ")
        # to print new line after each row.
        print()

# function to allocate space for the players and to calculate the points.
def procedure(board,player,row,column,point,round):
    # if the given place is occupied by the star then replace it by the first character of the player name
    if board[row][column]=="*":
        board[row][column]=player
    # if the given space is occupied by the players first char then replace it by the other player and add a point
    elif board[row][column]!=player:
        board[row][column]=player
        # increment the point of the player
        point+=1
        print(f"player {player} earned a point")
        # return the points of the player
        return(point)
    # to print the count of the round.
    print(f"ROUND:{round}")
    # function call to display the board.
    display(board)
    # to return the point of the player.
    return(point)

# funtion to roll the dice.
def roll():
    a=random.randint(1,6)
    return(a-1)
# imported random 
import random
# initialized points to 0
player1point=0
player2point=0
# getting name as the input from the user
player1name=input("enter your name:")
player2name=input("enter your name:")
# initializing a empty list to store the first letters of the players.
players=[]
# appending the first letters of the players names.
players.append(player1name[0])
players.append(player2name[0])
# board matrix model
board=[[],[],[],[],[],[]]
# function call to create the board pattern
creatingBoard(board,6)
# round coounter
round=0
while player1point<5 and player2point<5:
    round+=1
    # function call generate row and column using the randint.
    row=roll()
    column=roll()
    index=0
    # function call to calculate the points of the player
    player1point =procedure(board,players[index],row,column,player1point,round)

    index+=1
    # function call to generate row and column using the rand int.
    row=roll()
    column=roll()
    # function call to calculate the point of player 2
    player2point =procedure(board,players[index],row,column,player2point,round)

# conditional statement to determine the winner.
if player1point == 5:
    print(f"Winner:{player1name}")
elif player2point == 5:
    print(f"Winner:{player2name} ")

"""
OP:
enter your name:goku
enter your name:vegeta
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * *
* * * * * *
ROUND:1
* * * * * *
* g * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
ROUND:1
* * * * * *
* g * * * *
* * * * * *
* * * * * *
* * * v * *
* * * * * *
ROUND:2
* * * * * *
* g * * * *
* * * * * *
* * * * * *
* * g v * *
* * * * * *
ROUND:2
v * * * * *
* g * * * *
* * * * * *
* * * * * *
* * g v * *
* * * * * *
ROUND:3
v * * * * g
* g * * * *
* * * * * *
* * * * * *
* * g v * *
* * * * * *
ROUND:3
v * * * * g
* g * * * *
* * * * * *
v * * * * *
* * g v * *
* * * * * *
ROUND:4
v * * * * g
* g * * * *
* * * * * *
v * * * * *
* * g v g *
* * * * * *
ROUND:4
v * v * * g
* g * * * *
* * * * * *
v * * * * *
* * g v g *
* * * * * *
ROUND:5
v * v * * g
* g * * * *
* * * * * *
v * * * * *
* * g v g *
* * * * * *
ROUND:5
v * v * * g
* g * * * *
* * * * * *
v * * * * *
* * g v g *
* * * v * *
ROUND:6
v * v * * g
* g * * * *
* * * * * *
v * * g * *
* * g v g *
* * * v * *
ROUND:6
v * v * * g
* g * * * *
* * * * * *
v * * g * *
* * g v g *
* * * v * v
ROUND:7
v * v * * g
* g * * * *
* * * * * *
v * * g * g
* * g v g *
* * * v * v
ROUND:7
v * v * * g
v g * * * *
* * * * * *
v * * g * g
* * g v g *
* * * v * v
ROUND:8
v * v * * g
v g * * * *
* * * * * *
v * * g * g
* * g v g *
* * * v * v
ROUND:8
v * v * * g
v g * * * *
* * * v * *
v * * g * g
* * g v g *
* * * v * v
player g earned a point
ROUND:9
v * v * * g 
v g * * * *
* * * g * *
v * * g * g
* * g v g v
* * * v * v
player g earned a point
ROUND:10
v * v * * g
v g * * * v
* * * g * *
g * * g * g
* * g v g v
* * * v * v
ROUND:11
v * v * * g
v g * * * v
* * * g * *
g * * g * g
g * g v g v
* * * v * v
ROUND:11
v * v * * g
v g * * * v
* * * g * *
g * * g * g
g * g v g v
* * * v * v
ROUND:12
v * v * * g
v g * * * v
* * * g g *
g * * g * g
g * g v g v
* * * v * v
player v earned a point
ROUND:13
v * v * * g
v g * * * v
* * * g g *
g * * v * g
g * g v g v
* * * v * v
ROUND:13
v * v * * g
v g * * * v
* * * g g *
g * * v * g
g * g v g v
* * * v * v
player g earned a point
ROUND:14
v * v * * g
v g * * * v
* * * g g *
g * * g * g
g * g v g v
v * * v * v 
ROUND:15
v * v * * g
v g * * * v
* * * g g *
g * * g * g
g * g v g v
v * * v * v
ROUND:15
v * v * * g
v g * * * v
* * * g g *
g * * g * g
g * g v g v
v * * v * v
ROUND:16
v * v * * g
v g * * * v
* * * g g *
g * * g * g
g * g v g v
v * * v * v
ROUND:16
v * v * * g
v g * * * v
* * * g g *
g * * g * g
g * g v g v
v * * v * v
ROUND:17
v * v * * g
v g * * * v
* * g g g *
g * * g * g
g * g v g v
v * * v * v
ROUND:17
v * v * * g
v g * v * v
* * g g g *
g * * g * g
g * g v g v
v * * v * v
ROUND:18
v * v * * g
v g g v * v
* * g g g *
g * * g * g
g * g v g v
v * * v * v
ROUND:18
v * v * * g
v g g v * v
* * g g g *
g * * g * g
g * g v g v
v * * v * v
ROUND:19
v * v * * g
v g g v * v
* * g g g g
g * * g * g
g * g v g v
v * * v * v
ROUND:19
v * v * * g
v g g v * v
* * g g g g
g * * g * g
g * g v g v
v * * v * v
player g earned a point
ROUND:20
v * v * * g
v g g v * v
* * g g g g
g * * g v g
g * g v g v
v * * g * v
ROUND:21
v * v * * g
v g g v * v
* * g g g g
g * * g v g
g * g v g v
v * * g * v
ROUND:21
v * v * * g
v g g v * v
* * g g g g
g * * g v g
g * g v g v
v * * g * v
ROUND:22
v * v * * g
v g g v * v
* * g g g g
g * * g v g
g * g v g v
v * * g * v
ROUND:22
v * v * * g
v g g v * v
* * g g g g
g * * g v g
g * g v g v
v * * g * v
player g earned a point
ROUND:23
v * v * * g
g g g v * v
* * g g g g
g * * g v g
g * g v g v
v * * g * v
Winner:goku
"""