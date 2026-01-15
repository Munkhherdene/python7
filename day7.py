import random
from ui import word_list
remaining = 6

chosen_word = random.choice(word_list)
#print(chosen_word)
placeholder = ""
word_lenght = len(chosen_word)
for position in range(word_lenght):
    placeholder += "_"
print(placeholder)
print(f"{remaining}: guesses remaining")

game_over = False
correct_letters = []


while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    print(f"You guessed: {guessed_letter}")
    if guessed_letter not in chosen_word:
        remaining = remaining - 1


    display = ""

    for letter in chosen_word:
        if letter == guessed_letter:
            display += letter
            correct_letters.append(guessed_letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            
            

    print(display)
    print(f"{remaining} : guesses remaining")
    

    if "_" not in display:
        game_over = True
        print("you win") 
    elif remaining == 0:
        game_over = True
        print("You lose")