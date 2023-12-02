"""
Problem #2
Same problem as above. Also calculate tickets price. 
Firsrt 3 rows - Rs100
Rows 4 to 12 - Rs 200
Rows 13 till top - Rs 300.
3 seats close to the wall on both sides costs less than the other seats in the same row.
"""
def calculateTotalCost(ticket,index ):
    cost=0
    if index==0 or index == 4:
        # cost of the ticket - discount.
        cost=ticket-((10/100)*ticket)
    else:
        cost+=ticket
    return(cost)
# function to calculate the seats filled in each row
def seatsFilled(seats,seatsfilled):
    temp=0
    for i in seats:
        # initialized count =0 inside the loop to find the number of occupied seat in each row.
        count=0
        for j in i:
            # x refers to occupied seat so we check if the value of j=="x"
            if j =="X":
                # count is incremented after each iteration if the seat is occupied
                count+=1
        # the current count of the seat filled is updated in the seatsfilled list.
        seatsfilled[temp] = count
        temp+=1
    # the updated list is returned to the main function.
    return(seatsfilled)

#function to display the seating arangement of the theater.
def display(seats,rows):
    # initialized count to count the rows.
    count=0
    # for loop to display the seating arrangement.
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
    print("Firsrt 3(A-C) rows - Rs100\nRows 4 to 12 (D-L)- Rs 200 Row 13(M)- Rs 300.")


# function to book tickets.
def booktickets(seats,rows,seatsfilled):
     # initializing cost = 0 to calculate the total cost.
     cost=0
     print("* "*10)
     # calling the function to display the seat arrangement.
     display(seats,rows)
     print("* "*10)
     row=input("eneter the row:")

     if row.upper() in rows:
        # to access the list of rows using the index value.
        rowIndex=int(rows.index(row.upper()))
        seat=int(input("enter the number of seats you want:"))
        # conditional statement to check if the seat is sufficient.
        if seats[rowIndex].count("o")<seat:
            return("we dont have that much seats")
        else:
            # initializing the list to append the seats booked.
            booked=[]
            for index in range(seat):
                # conditional statement to ensure the program is free from runtime error.
                if seat <=0:
                    break
                # to check if the seat is already booked or not.
                if seats[rowIndex][index+seatsfilled[rowIndex]]=="o":
                    seats[rowIndex][index+seatsfilled[rowIndex]]="X"
                    # to check if the seat is near the wall.
                    if rowIndex < 3:
                        ticket=100
                        cost+=calculateTotalCost(ticket,index+seatsfilled[rowIndex])
                    elif rowIndex == 12:
                        ticket = 300
                        cost+=calculateTotalCost(ticket,index+seatsfilled[rowIndex])
                    else:
                        ticket = 200
                        cost+=calculateTotalCost(ticket,index+seatsfilled[rowIndex])
                # append the tickets booked to the list called booked.
                booked.append(f"{rows[rowIndex]}:{index+seatsfilled[rowIndex]+1}")
            #return the booked seats and the total booking cost to main function.
            return(f"BOOKED SEATS ARE:{booked}\ntotal cost for booking:{cost}\n")


# initializing the seats.
seats=[
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o']    
]
seatsfilled=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while(True):
    choice=input("do you want to book tickets(yes/no):")
    rows=["A","B","C","D","E","F","G","H","I","J","K","L","M"]

    if choice.lower() == "yes":
        print(booktickets(seats,rows,seatsfilled))
        # function call to calculate the seats filled in each row.
        seatsfilled=seatsFilled(seats,seatsfilled)

    elif choice.lower() == "no":
        print("thank you.. The seats which remained unfilled are!!!")
        # function call to display the seats remained unfilled.
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
Row E : o o o o o
Row F : o o o o o
Row G : o o o o o
Row H : o o o o o
Row I : o o o o o
Row J : o o o o o
Row K : o o o o o
Row L : o o o o o
Row M : o o o o o
o - UNOCCUPIED
X - OCCUPIED
Firsrt 3(A-C) rows - Rs100
Rows 4 to 12 (D-L)- Rs 200 Row 13(M)- Rs 300.
* * * * * * * * * *
eneter the row:A
enter the number of seats you want:2
BOOKED SEATS ARE:['A:1', 'A:2']
total cost for booking:190.0

do you want to book tickets(yes/no):yes
* * * * * * * * * *
Row A : X X o o o
Row B : o o o o o
Row C : o o o o o
Row D : o o o o o
Row E : o o o o o
Row F : o o o o o
Row G : o o o o o
Row H : o o o o o
Row I : o o o o o
Row J : o o o o o
Row K : o o o o o
Row L : o o o o o
Row M : o o o o o
o - UNOCCUPIED
X - OCCUPIED
Firsrt 3(A-C) rows - Rs100
Rows 4 to 12 (D-L)- Rs 200 Row 13(M)- Rs 300.
* * * * * * * * * *
eneter the row:A
enter the number of seats you want:3
BOOKED SEATS ARE:['A:3', 'A:4', 'A:5']
total cost for booking:290.0

do you want to book tickets(yes/no):yes
* * * * * * * * * *
Row A : X X X X X
Row B : o o o o o
Row C : o o o o o
Row D : o o o o o
Row E : o o o o o
Row F : o o o o o
Row G : o o o o o
Row H : o o o o o
Row I : o o o o o
Row J : o o o o o
Row K : o o o o o
Row L : o o o o o
Row M : o o o o o
o - UNOCCUPIED
X - OCCUPIED
Firsrt 3(A-C) rows - Rs100
Rows 4 to 12 (D-L)- Rs 200 Row 13(M)- Rs 300.
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
Row E : o o o o o
Row F : o o o o o
Row G : o o o o o
Row H : o o o o o
Row I : o o o o o
Row J : o o o o o
Row K : o o o o o
Row L : o o o o o
Row M : o o o o o
o - UNOCCUPIED
X - OCCUPIED
Firsrt 3(A-C) rows - Rs100
Rows 4 to 12 (D-L)- Rs 200 Row 13(M)- Rs 300.
* * * * * * * * * *
eneter the row:B
enter the number of seats you want:5
BOOKED SEATS ARE:['B:1', 'B:2', 'B:3', 'B:4', 'B:5']
total cost for booking:480.0

do you want to book tickets(yes/no):yes
* * * * * * * * * *
Row A : X X X X X
Row B : X X X X X
Row C : o o o o o
Row D : o o o o o
Row E : o o o o o
Row F : o o o o o
Row G : o o o o o
Row H : o o o o o
Row I : o o o o o
Row J : o o o o o
Row K : o o o o o
Row L : o o o o o
Row M : o o o o o
o - UNOCCUPIED
X - OCCUPIED
Firsrt 3(A-C) rows - Rs100
Rows 4 to 12 (D-L)- Rs 200 Row 13(M)- Rs 300.
* * * * * * * * * *
eneter the row:M
enter the number of seats you want:2
BOOKED SEATS ARE:['M:1', 'M:2']
total cost for booking:570.0

do you want to book tickets(yes/no):yes
* * * * * * * * * *
Row A : X X X X X
Row B : X X X X X
Row C : o o o o o
Row D : o o o o o
Row E : o o o o o
Row F : o o o o o
Row G : o o o o o
Row H : o o o o o
Row I : o o o o o
Row J : o o o o o
Row K : o o o o o
Row L : o o o o o
Row M : X X o o o
o - UNOCCUPIED
X - OCCUPIED
Firsrt 3(A-C) rows - Rs100
Rows 4 to 12 (D-L)- Rs 200 Row 13(M)- Rs 300.
* * * * * * * * * *
eneter the row:M
enter the number of seats you want:2
BOOKED SEATS ARE:['M:3', 'M:4']
total cost for booking:600

do you want to book tickets(yes/no):yes
* * * * * * * * * *
Row A : X X X X X
Row B : X X X X X
Row C : o o o o o
Row D : o o o o o
Row E : o o o o o
Row F : o o o o o
Row G : o o o o o
Row H : o o o o o
Row I : o o o o o
Row J : o o o o o
Row K : o o o o o
Row L : o o o o o
Row M : X X X X o
o - UNOCCUPIED
X - OCCUPIED
Firsrt 3(A-C) rows - Rs100
Rows 4 to 12 (D-L)- Rs 200 Row 13(M)- Rs 300.
* * * * * * * * * *
eneter the row:E
enter the number of seats you want:5
BOOKED SEATS ARE:['E:1', 'E:2', 'E:3', 'E:4', 'E:5']
total cost for booking:960.0

do you want to book tickets(yes/no):no
thank you.. The seats which remained unfilled are!!!
Row A : X X X X X
Row B : X X X X X
Row C : o o o o o
Row D : o o o o o
Row E : X X X X X
Row F : o o o o o
Row G : o o o o o
Row H : o o o o o
Row I : o o o o o
Row J : o o o o o
Row K : o o o o o
Row L : o o o o o
Row M : X X X X o
o - UNOCCUPIED
X - OCCUPIED
Firsrt 3(A-C) rows - Rs100
Rows 4 to 12 (D-L)- Rs 200 Row 13(M)- Rs 300.
"""