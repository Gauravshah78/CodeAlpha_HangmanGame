import random

# Predefined list of 5 words
words = ["python", "apple", "mango", "school", "computer"]

# Select a random word
secret_word = random.choice(words)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("================================")
print("       WELCOME TO HANGMAN!")
print("================================")
print("Guess the hidden word one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

# Main game loop
while incorrect_guesses < max_attempts:

    # Display the current word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    # Check if the player has guessed the word
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        print("You won!")
        break

    # Take user input
    guess = input("Guess a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.\n")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You have already guessed that letter. Try again!\n")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!\n")
    else:
        incorrect_guesses += 1
        print("Wrong guess!\n")

# Game over message
if incorrect_guesses == max_attempts:
    print("GAME OVER!")
    print("The correct word was:", secret_word)
    
