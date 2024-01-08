from art import *
import random

end_of_game = False
word_list = ["ardvark", "baboon", "camel", "elephant", "Galaxy", "Song", "Pumpkin", "Rhinoceros", "Dinosaur",
             "Butterfly", "Avalanche", "Giant", "Thunder"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


print("""
***************************
*********WELCOME***********
***********TO**************
*********HANGMAN***********
***************************
""")

mode = input("What mode do you want to play on ? Type \"E\" for Easy mode or type \"H\" for Hard mode : ").lower()
if mode == "e":
    lives = 6
    print(f"Good Luck ! You chose to play on easy mode and have {lives} lives")
elif mode == "h":
    lives = 3
    print(f"Good Luck ! You chose to play on hard mode and have {lives} lives")

display = []
for _ in range(word_length):
    display += "_"


def game_play():
    global mode
    global end_of_game
    global lives
    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        # Check guessed letter
        for position in range(word_length):

            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            lives -= 1
            print(f"Beware!, you have {lives} lives left")
            if lives == 0:
                print(stages_for_easy[0])
                print("You Lose...")
                break

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win!!!.")
            break

        if mode == 'e':
            print(stages_for_easy[lives])
        else:
            print(stage_for_hard[lives])

game_play()

print("Thank You for Playing this game!!!")
