import random
from logo_Numguess import logo
#print(guess)
easy_level_attempt=10
hard_level_attempt=5
def set_difficulty_level(level_choose):
    if level_choose=='easy':
        return easy_level_attempt
    else :
        return hard_level_attempt
def game():
   print("Let's guess any Number between 1 to 50")
   answer=random.randint(1,50)
   print(logo)
   level=input("Choose level of difficulty ... type 'easy' or 'hard':")
   attempt=set_difficulty_level(level)
   def check_answer(guessed, answer ,attempt):
      
      if guessed<answer:
         print(f"Your Guess is too low ...You have {attempt-1} attempts left")
         print("Guess again ...")
         return attempt-1
      elif guessed>answer:
         print("Your Guess is too high ...")
         print(f"Guess again ...You have {attempt-1} attempts left")
         return attempt-1
      else:
         print(f"Your guess is correct . the answer was {answer}")
         return None
   guessed=0
   while guessed!=answer:
      guessed=int(input("Make a Guess :"))
      attempt=check_answer(guessed , answer , attempt)
      if attempt==0:
         print("You lose ... You have no more attempts left.")
         break
   
game()
       

