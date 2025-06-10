import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ronaldo", "messi", "kaka", "neymar", "pele", "maradona", "zidane", "maldini", "buffon", "xavi", "iniesta"]


lives = 6
print("Welcome to Sport Hangman!")
chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)


game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("You lose!")
            break

    if "_" not in display:
        game_over = True
        print("You win!")


    print(stages[lives])
    print(f"You have {lives} lives left.")
print(f"The chosen word was {chosen_word}.")