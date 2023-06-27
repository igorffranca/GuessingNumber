import random
import os

logo = """
 _____                       _   _                                  _               
|  __ \                     | | | |                                | |              
| |  \/_   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                    
"""
def clear():
   if os.name == 'nt':
      os.system('cls')
   else:
      os.system('clear')

def track_number(generated_number, guess_number):
   if guess_number > generated_number:
      return "Too high"
   elif generated_number > guess_number:
      return "Too low"
   else:
      return f"You got it! The answer was {generated_number}"


def difficulty():
   attempts = 0
   
   while not attempts == 5 or attempts == 10:
      level = input("Choose a difficulty. Type 'easy' or 'hard': ").strip()

      if level == "easy":
         attempts = 10
         break
      elif level == "hard":
         attempts = 5
         break
      else:
         attempts = 0
         print("Wrong option! Try again..")
   return attempts
    
clear()
print(logo)

print("Welcome to the Number Guessing Game!")

list_of_number = [num for num in range(1,101)]
number_chose = random.choice(list_of_number)

print("I'm thinking of a number between 1 and 100.")
attempts = difficulty()

print(number_chose)

while True:
  
  print(f"You have {attempts} attempts remaining to guess the number.")
  if attempts > 0:
      guess = int(input("Make a guess: ").strip())
      
      if guess == number_chose:
         track = track_number(number_chose, guess)
         print(track)
         break
      else:
         track = track_number(number_chose, guess)
         print(track)
         attempts -= 1
  else:
      print("You lose the game!")
      break
    
        

