

from random import randint


logo="""  ▄▀    ▄   ▄███▄     ▄▄▄▄▄    ▄▄▄▄▄          ▄▄▄▄▀ ▄  █ ▄███▄          ▄     ▄   █▀▄▀█ ███   ▄███▄   █▄▄▄▄ 
▄▀       █  █▀   ▀   █     ▀▄ █     ▀▄     ▀▀▀ █   █   █ █▀   ▀          █     █  █ █ █ █  █  █▀   ▀  █  ▄▀ 
█ ▀▄  █   █ ██▄▄   ▄  ▀▀▀▀▄ ▄  ▀▀▀▀▄           █   ██▀▀█ ██▄▄        ██   █ █   █ █ ▄ █ █ ▀ ▄ ██▄▄    █▀▀▌  
█   █ █   █ █▄   ▄▀ ▀▄▄▄▄▀   ▀▄▄▄▄▀           █    █   █ █▄   ▄▀     █ █  █ █   █ █   █ █  ▄▀ █▄   ▄▀ █  █  
 ███  █▄ ▄█ ▀███▀                            ▀        █  ▀███▀       █  █ █ █▄ ▄█    █  ███   ▀███▀     █   
       ▀▀▀                                           ▀               █   ██  ▀▀▀    ▀                  ▀    
                                                                                                            
"""

print(logo)

easy_level=10
hard_level=5



def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns-1
  elif guess == answer:
    print(f"You got it! The answer was {answer}.")
    
  

def set_difficulty():
  level=input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return easy_level
    
  elif level== "hard":
    return hard_level


def game():
  print("Welcome to the Number Guessing Game!")
  print("I am guessing a number between 1 to 100")
  answer=randint(1,100)
  
  turns=set_difficulty()
 
  
  guess=0
  while guess!=answer:
     print(f"You have {turns} attempts remaining to guess the number.")

     guess=int(input("Guess any number between 1 to 100: "))
     turns=check_answer(guess, answer, turns)

     if turns==0:
       print("You have run out of guesses. You lose.")
       return
game()    
    






