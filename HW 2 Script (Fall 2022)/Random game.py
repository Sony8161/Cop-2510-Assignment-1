#Duong Lam U68618275 The Price is right game.
'''in this game you have to guess a random integer in order to win money
The closest guess wins the game, and who ever exactly guesses the amount wins $500 :D
'''
import random
import math
randint = random.randint(1000, 5000)

P1 = int(input("Welcome Player One, What is your Starting Bid?:"))
P2 = int(input("Welcome Player Two, What is your Starting bid?:"))
P3 = int(input("Welcome Player Three, What is your Starting bid?:"))
P4 = int(input("Welcome Player Four, What is your Starting bid?:"))

if (P1 > randint and P2 > randint and P3 > randint and P4 > randint):
    print("Game Over! Everyone overbid :(")
    quit()
if P1 == randint:
    print("You have correctly bid, you win $500 :D") 
winner = "1"
if P2 == randint:
    print("You have correctly bid, you win $500 :D") 
winner = "2"
if P3 == randint:
    print("You have correctly bid, you win $500 :D")
winner = "3"
if P4 == randint:
    print("You have correctly bid, you win $500 :D")
winner ="4"

d1 = (math.fabs(P1 - randint))
d2 = (math.fabs(P2 - randint))
d3 = (math.fabs(P3 - randint))
d4 = (math.fabs(P4 - randint))

g = min(d1, d2, d3, d4)

if(g == d1):
    winner = "1"

elif(g == d2):
    winner = "2"

elif(g == d3):
    winner = "3"

elif(g == d4):
    winner = "4"


print (f"Actual price is ${randint}! Player{winner}, come on up!")
