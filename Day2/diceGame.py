"""
Its is a single player game where the user starts with 0 points. User keeps rolling the 
dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
added. If the number is odd, then if the number is 1,3 then the user has to jump. 
If the number is 5, then 3 points are added. The game ends when the user has 50 points.
"""
import random

# function to calculate the points
def calculate_points(point):
    while(True):
        if point > 50:
            return point
            break
        else:
            # using random to generate a random number
            dice=(random.randint(0,6))
            # print to show the random number generated
            print(f"the rolled value is {dice}")
            # if the random number is 0 then game ends.
            if dice == 0:
                return point
                break
            # if the random number is even then 2 points are added.
            elif(dice % 2 == 0):
                point+=2
            # if the number is odd and it is 1 or 3 then the player have to jump.
            elif(dice % 2 != 0):
                if( dice == 1 or dice ==3):
                    print("You have to jump!!")
                # if the number is 5 then 3 points are added.
                else:
                    point+=3


points=0
total_points=calculate_points(points)
print("Game Over!!")
print(f"Total points earned:{total_points}")

"""
OP:
the rolled value is 1
You have to jump!!
the rolled value is 5
the rolled value is 1
You have to jump!!
the rolled value is 0
Game Over!!
Total points earned:3
"""