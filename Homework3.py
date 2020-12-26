print("HANGMAN GAME / GUESS CAPITALS of EUROPE")
name = str(input("Name: "))
surname = str(input("Surname: "))
print("Welcome " + name + " " + surname)
import random as rnd
words = list(["rome", "paris", "ankara", "berlin", "amsterdam", "londra", "madrid", "brussels", "bern", "tirana", "chisinau", "vilnius", "athens", "warsaw", "cardif"])
check = False
secret = rnd.choice(words)
print("HINT:Your city name has ",len(secret) , "chars!!!" )
print("You have just 5 guesses to save him")
for i in range(5):
    guess = input("Please enter your guess: ")
    if guess==secret:
        print("Congrats!!")
        check = True
        break  
    else: 
        print("Try again")
if not check:
   print("GAME OVER...The city was:", secret)
