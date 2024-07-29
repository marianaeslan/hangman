#setting variables
secret_word = "javascript"
attempts = len(secret_word) - 2
guessed = []

#display header -> start of the game
print("=========================")
print("|        HANGMAN        |")
print("=========================")
print(f"\t\t\tAttempts: {attempts}")
print("-------------------------")
print("_ " * len(secret_word))
print("\n")

#input letter guess and checking if it exists in the secret word
while attempts > 0:
    letter_guess = input("\nInsert a letter: ").lower()
    print("\n")
    if letter_guess in guessed:
        print("You already guessed this letter, try another one")
    if letter_guess in secret_word:
        guessed.append(letter_guess)
    else:
        attempts -= 1
        print("-------------------------")
        print("Wrong guess... Try again")
        print(f"\t\t\tAttempts: {attempts}")
        print("-------------------------")