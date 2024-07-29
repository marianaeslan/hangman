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