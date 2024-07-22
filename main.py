import string

# 1. Initialize the Game
word_to_guess = "hello"  # Define the word to be guessed
display_word = ['_' for _ in word_to_guess]  # Display with underscores
max_tries = 6  # Maximum number of tries allowed
tries_left = max_tries  # Initialize tries left

# 2. Explain the Game
print("Welcome to the Word Guessing Game!")  # Game introduction
print("Try to guess the word, one letter at a time.")  # Instructions
print("The word to guess is:")
print(' '.join(display_word))  # Display the initial state with blanks

# 3. User Input and Validation
def get_valid_input():
    while True:
        guess = input("Enter a single letter: ").lower()  # Get user input
        if len(guess) == 1 and guess in string.ascii_lowercase:
            return guess  # Return valid input
        else:
            print("Invalid input. Please enter a single alphabetic character.")  # Error message for invalid input

# 4. Game Loop
while '_' in display_word and tries_left > 0:  # Continue until the word is guessed or tries run out
    guess = get_valid_input()  # Get a valid guess from the user

    if guess in word_to_guess:
        # Update display_word with correct guess
        for index, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[index] = guess  # Update the display with the guessed letter
        print(f"Good guess! The word now looks like: {' '.join(display_word)}")  # Show the updated word
    else:
        tries_left -= 1  # Decrease the number of tries left
        print(f"Wrong guess. You have {tries_left} tries left.")  # Inform the user of remaining tries

    if '_' not in display_word:  # Check if the word has been completely guessed
        print("Congratulations! You guessed the word:", word_to_guess)  # Winning message
        break
else:
    if tries_left == 0:  # Check if the user has run out of tries
        print("Sorry, you ran out of tries. The word was:", word_to_guess)  # Losing message