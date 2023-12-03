"""
Problem #1.
Write a program for calculating the profit for railways.
For first class tickets, the profit is 25% of the price + Rs100 for every ticket sold.
For Second class tickets, the profit is 15% of the price + Rs70 for every ticket sold.
For Third class tickets (i don't know if there is a third class), the profit is 5% of the price.

Get the price and no of tickets sold for each class and calculate the total profit. 
Identity what calculation in the above problem can be written as a function 
and what the input and output should be.
"""

def calculateProfit(ticketClass,price,ticketsBooked):
    if ticketClass == "1":
        profitPercentage=0.25
        profitprice=100
        profit=(profitPercentage*price+profitprice)*ticketsBooked
    elif ticketClass == "2":
        profitPercentage=0.15
        profitprice=70
        profit=(profitPercentage*price+profitprice)*ticketsBooked
    else:
        profitPercentage=0.05
        profit=(profitPercentage*price)*ticketsBooked
    return profit

def calculateProfitPercentage(profit,totalProfit):
    profitPercentage=(profit/totalProfit)*100
    return (round(profitPercentage,2))


class1TicketsBooked=int(input("enter the number of class 1 tickets booked:"))
class1TicketPrice=float(input("Enter the price of the class 1 tickets:"))
profitClass1=calculateProfit("1",class1TicketPrice,class1TicketsBooked)

class2TicketsBooked=int(input("enter the number of class 2 tickets booked:"))
class2TicketPrice=float(input("Enter the price of the class 2 tickets:"))
profitClass2=calculateProfit("2",class1TicketPrice,class1TicketsBooked)

class3TicketsBooked=int(input("enter the number of class 3 tickets booked:"))
class3TicketPrice=float(input("Enter the price of the class 3 tickets:"))
profitClass3=calculateProfit("3",class1TicketPrice,class1TicketsBooked)

totalTicketsBooked=class1TicketsBooked+class2TicketsBooked+class3TicketsBooked
totalProfit=profitClass1+profitClass2+profitClass3

profitPercentageClass1=calculateProfitPercentage(profitClass1,totalProfit)
profitPercentageClass2=calculateProfitPercentage(profitClass2,totalProfit)
profitPercentageClass3=calculateProfitPercentage(profitClass3,totalProfit)


print("\n\tSUMMARY")
print(f"Total tickets Booked:{totalTicketsBooked}\n")
print(f"total class 1 tickets Booked:{class1TicketsBooked}\ntotal profit earned by class 1 ticket:{profitClass1}\npercentage of profit earned from class 1:{profitPercentageClass1}\n")
print(f"total class 2 tickets Booked:{class2TicketsBooked}\ntotal profit earned by class 2 ticket:{profitClass2}\npercentage of profit earned from class 2:{profitPercentageClass2}\n")
print(f"total class 3 tickets Booked:{class3TicketsBooked}\ntotal profit earned by class 3 ticket:{profitClass3}\npercentage of profit earned from class 3:{profitPercentageClass3}\n")
print(f"Total Profit earned {round(totalProfit,2)}")


"""
OP:
enter the number of class 1 tickets booked:100
Enter the price of the class 1 tickets:400
enter the number of class 2 tickets booked:100
Enter the price of the class 2 tickets:300
enter the number of class 3 tickets booked:100
Enter the price of the class 3 tickets:150

        SUMMARY
Total tickets Booked:300

total class 1 tickets Booked:100
total profit earned by class 1 ticket:20000.0
percentage of profit earned from class 1:57.14

total class 2 tickets Booked:100
total profit earned by class 2 ticket:13000.0
percentage of profit earned from class 2:37.14

total class 3 tickets Booked:100
total profit earned by class 3 ticket:2000.0
percentage of profit earned from class 3:5.71

Total Profit earned 35000.0
"""