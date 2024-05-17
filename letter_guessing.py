

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"


while "_" in display:
  guess = input("Guess a letter: ").lower()
  
  #Check guessed letter
  for position in range(word_length):
      letter = chosen_word[position]
      
      if letter == guess:
          display[position] = letter
  
  print(display)
  if "_" not in display:
    end_of_game=True
    print("You win!")

