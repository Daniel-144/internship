"""
Problem #1
Wrote a program for seat reservation in a theatre.
You can decide on the configuaration of the seats (no of rows and no of seats in each row, and a passage in between)
When the user asks for tickets, you need to provide them tickets in the form of seat no.
For eg, User ask for 3 seats in the middle. Output is F11, F12 , F13
Print the theatre configuaration at the end of each transaction.
"""
def display(seats,rows):
    count=0
    for i in seats:
        print(f"Row {rows[count]} : ",end="")
        for j in i:
            if i =="o":
                print(j,end=" ")
            else:
                print("X",end=" ")
        print()
        count+=1

def booktickets(seats,rows):
    print("* "*10)
    display(seats)
    print("* "*10)
    row=input("eneter the row:")
    if row.upper() in rows:
       rowIndex=int(rows.index(row.upper))
       seat=int(input("enter the number of seats you want:"))
       if seats[row].count("o")<seat:
           print("we dont have that much seats")
        else:
           booked=[]
           for rowIndex in range(len(rows)):
               if seat ==0:
                   break
               if seats[row]


seats=[
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o']
]

while(True):
    choice=input("do you want to book tickets(yes/no):")
    if choice.lower() == "yes":
        rows=["A","B","C","D"]
        booktickets(seats,rows)

    elif choice.lower() == "no":
        print("thank you.. The seats which remained unfilled are!!!")
        display(seats)
        break
