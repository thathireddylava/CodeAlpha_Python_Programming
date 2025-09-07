import random

words = ["apple", "tiger", "water", "phone", "train"]
word = random.choice(words)
guessed = []
attempts = 6

print("Welcome to Hangman Game")
print("You have 6 chances to guess the word.")

while attempts > 0:
    display_word = "".join([letter if letter in guessed else "_" for letter in word])
    print("Word:", display_word)
    if display_word == word:
        print("Congratulations! You guessed the word:", word)
        break
    guess = input("Enter a letter: ").lower()
    if guess in guessed:
        print("You already guessed this letter.")
        continue
    guessed.append(guess)
    if guess not in word:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)
    else:
        print("Good guess!")

if attempts == 0:
    print("Game Over! The word was:", word)

