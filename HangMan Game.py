import random

# List of words
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the list
choice = random.choice(word_list)

# Initialize the displayed word as underscores
displayed_word = "_" * len(choice)
print(displayed_word)

# List to track guessed letters
guessed_letters = []

# Start the game loop
while "_" in displayed_word:
    # Get user input (single letter)
    word = input("Enter a letter: ").lower()

    # Validate input
    if len(word) != 1 or not word.isalpha():
        print("Please enter a valid letter.")
        continue

    # Check if the letter has already been guessed
    if word in guessed_letters:
        print(f"You've already guessed the letter '{word}'. Try again!")
        continue
    else:
        guessed_letters.append(word)

    # If the letter is in the word, reveal it
    if word in choice:
        # Update the displayed_word with the correct letters
        displayed_word_list = list(displayed_word)
        for i in range(len(choice)):
            if word == choice[i]:
                displayed_word_list[i] = word

        # Convert the list back to a string
        displayed_word = "".join(displayed_word_list)
        print(f"The word is: {displayed_word}")
    else:
        print(f"Wrong guess! The letter '{word}' is not in the word.")

# Game over, user guessed all letters
print(f"Congratulations! You guessed the word: {choice}")
