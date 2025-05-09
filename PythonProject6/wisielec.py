import random
from hangman_words import word_list
from hangman_art import logo, hangman

#Projekt 1 - Wisielec - Jakub Grzebielucha 59599

class Hangman:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print("Welcome in a Hangman game! Good luck!!")

hang = Hangman("Hangman")

print("======================================")
hang.welcome()
print("======================================")

print("(If an error occurs, please restart the program.)")

lives = 6
print(logo)

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(hangman[0])
        hangman.pop(0)
        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
        print("***************************CONGRATS!***************************")
