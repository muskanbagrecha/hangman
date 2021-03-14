import random
from word import word_list
from assets import logo, stages
import os
print(logo)
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives=6
display = []
chosen=[]

for _ in range(word_length):
    display += "_"

is_present=False
print(f"{' '.join(display)}")
while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            is_present=True
    if not is_present:
        if guess in chosen:
            print("You have already made that guess. Try another one. ")
        else:
            print(f'You have chosen {guess} but it\'s not in the word.')
            lives-=1
            print(stages[lives])
            chosen.append(guess)
    is_present=False
    print(f"{' '.join(display)}\n")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    if lives==0:
        end_of_game = True
        print("You lose!! Better luck next time.")
        print(f"The word was: '{chosen_word}'")
