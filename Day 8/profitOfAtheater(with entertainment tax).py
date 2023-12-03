

def ProfitOfTickets(TicketClass,ticketsBooked,ticketPrice):
    entertainmentTax=0.05
    if TicketClass =="VIP":
        profitPercentage=0.3
        profit=(profitPercentage*ticketPrice+120)*ticketsBooked
    elif TicketClass == "General":
        profitPercentage=0.2
        profit=(profitPercentage*ticketPrice+80)*ticketsBooked
    else:
        profitPercentage=0.15
        profit=(profitPercentage*ticketPrice)*ticketsBooked

    profit-= ticketPrice*entertainmentTax
    return(round(profit,2))



def calculatePercentage(profit,totalProfit):
    profitPercentage=round((profit/totalProfit)*100,2)
    return (round(profitPercentage,2))


vipTicketsBooked=int(input("Enter the no of Vip tickets booked:"))
vipTicketsPrice=float(input("Enter the price of the vip tickets:"))
profitOfVIPTickets=ProfitOfTickets("VIP",vipTicketsBooked,vipTicketsPrice)

generalTicketsBooked=int(input("Enter the no of general tickets booked:"))
generalTicketsPrice=float(input("Enter the price of the general tickets:"))
profitOfGeneralTickets=ProfitOfTickets("General",generalTicketsBooked,generalTicketsPrice)

matnieeTicketsBooked=int(input("Enter the no of Matinee tickets booked:"))
matnieeTicketProfit=float(input("Enter the price of the Matinee tickets:"))
profitOfMatineeTickets=ProfitOfTickets("Matinee",matnieeTicketsBooked,matnieeTicketProfit)

totalProfit=profitOfGeneralTickets+profitOfMatineeTickets+profitOfVIPTickets
PercentageOfVipprofit=calculatePercentage(profitOfVIPTickets,totalProfit)
percentageOfGeneralProfit=calculatePercentage(profitOfGeneralTickets,totalProfit)
percentageOfMatineeProfit=calculatePercentage(profitOfMatineeTickets,totalProfit)
totaltickets=vipTicketsBooked+generalTicketsBooked+matnieeTicketsBooked

print("\tSUMMARY\t")
print(f"Total tickets Booked:{totaltickets}")
print(f"No.Of Vip tickets booked:{vipTicketsBooked}")
print(f"Profit earned from 'Vip class':{profitOfVIPTickets}\nPercentage of profit earned from 'VIP class':{PercentageOfVipprofit}\n")
print(f"No.Of General tickets Booked:{generalTicketsBooked}")
print(f"Profit earned from 'General class':{profitOfGeneralTickets}\nPercentage of profit earned from 'General class':{percentageOfGeneralProfit}\n")
print(f"No.Of Matniee tickets Booked:{matnieeTicketsBooked}")
print(f"Profit earned from 'Matniee show':{matnieeTicketProfit}\nPercentage of profit earned from 'Matniee show':{percentageOfMatineeProfit}\n")
print(f"total Profit Earned by the theatre:{round(totalProfit,2)}")