import random

from hangman_words import word_list
from hangman_art import logo, stages

print(logo)


lives = 6
print("Welcome to Hangman!")
print(f"****************************{lives}/6 LIVES LEFT****************************")
chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)


game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    display = ""
    if guess in correct_letters:
        print(f"You have already guessed the letter '{guess}'. Try again.")
        continue
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
        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************")
            break

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    print(stages[lives])
    print(f"You have {lives} lives left.")
print(f"The chosen word was {chosen_word}.")