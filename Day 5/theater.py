"""
Problem #1
Wrote a program for seat reservation in a theatre.
You can decide on the configuaration of the seats (no of rows and no of seats in each row, and a passage in between)
When the user asks for tickets, you need to provide them tickets in the form of seat no.
For eg, User ask for 3 seats in the middle. Output is F11, F12 , F13
Print the theatre configuaration at the end of each transaction.
"""

def seatsFilled(seats,seatsfilled):
    temp=0
    for i in seats:
        count=0
        for j in i:
            if j =="X":
                count+=1
        seatsfilled[temp] = count
        temp+=1
    return(seatsfilled)

def display(seats,rows):
    count=0
    for i in seats:
        print(f"Row {rows[count]} : ",end="")
        for j in i:
            if j =="o":
                print(j,end=" ")
            else:
                print("X",end=" ")
        print()
        count+=1

    print("o - UNOCCUPIED")
    print("X - OCCUPIED")


def booktickets(seats,rows,seatsfilled):
     print("* "*10)
     display(seats,rows)
     print("* "*10)
     row=input("eneter the row:")

     if row.upper() in rows:
        rowIndex=int(rows.index(row.upper()))
        seat=int(input("enter the number of seats you want:"))
        if seats[rowIndex].count("o")<seat:
            return("we dont have that much seats")
        else:
            booked=[]
            for index in range(seat):
                if seat ==0:
                    break
                if seats[rowIndex][index+seatsfilled[rowIndex]]=="o":
                    seats[rowIndex][index+seatsfilled[rowIndex]]="X"
                booked.append(f"{rows[rowIndex]}:{index+seatsfilled[rowIndex]+1}")
            return(f"BOOKED SEATS ARE:{booked}")



seats=[
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o']
]
seatsfilled=[0,0,0,0]
while(True):

    choice=input("do you want to book tickets(yes/no):")
    rows=["A","B","C","D"]
    if choice.lower() == "yes":
        print(booktickets(seats,rows,seatsfilled))
        seatsfilled=seatsFilled(seats,seatsfilled)

    elif choice.lower() == "no":
        print("thank you.. The seats which remained unfilled are!!!")
        display(seats,rows)
        break

    else:
        print("invalid choice!!!!")

"""
OP:
do you want to book tickets(yes/no):yes
* * * * * * * * * * 
Row A : o o o o o 
Row B : o o o o o
Row C : o o o o o
Row D : o o o o o
o - UNOCCUPIED
X - OCCUPIED
* * * * * * * * * *
eneter the row:A
enter the number of seats you want:5
BOOKED SEATS ARE:['A:1', 'A:2', 'A:3', 'A:4', 'A:5']
do you want to book tickets(yes/no):yes
* * * * * * * * * *
Row A : X X X X X
Row B : o o o o o
Row C : o o o o o
Row D : o o o o o
o - UNOCCUPIED
X - OCCUPIED
* * * * * * * * * *
eneter the row:A
enter the number of seats you want:1
we dont have that much seats
do you want to book tickets(yes/no):yes
* * * * * * * * * *
Row A : X X X X X
Row B : o o o o o
Row C : o o o o o
Row D : o o o o o
o - UNOCCUPIED
X - OCCUPIED
* * * * * * * * * *
eneter the row:B
enter the number of seats you want:3
BOOKED SEATS ARE:['B:1', 'B:2', 'B:3']
do you want to book tickets(yes/no):yes
* * * * * * * * * *
Row A : X X X X X
Row B : X X X o o
Row C : o o o o o
Row D : o o o o o
o - UNOCCUPIED
X - OCCUPIED
* * * * * * * * * *
eneter the row:D4
None
do you want to book tickets(yes/no):yes
* * * * * * * * * *
Row A : X X X X X
Row B : X X X o o
Row C : o o o o o
Row D : o o o o o
o - UNOCCUPIED
X - OCCUPIED
* * * * * * * * * *
eneter the row:D
enter the number of seats you want:4
BOOKED SEATS ARE:['D:1', 'D:2', 'D:3', 'D:4']
do you want to book tickets(yes/no):no
thank you.. The seats which remained unfilled are!!!
Row A : X X X X X
Row B : X X X o o
Row C : o o o o o
Row D : X X X X o
o - UNOCCUPIED
X - OCCUPIED
"""