from art import *
import random

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
stages_length = len(stages)


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
    lives = 5
    print(f"Good Luck ! You chose to play on hard mode and have {lives} lives")