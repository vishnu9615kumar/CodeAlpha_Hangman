import random

def hangman():
    words = ["apple", "banana", "grape", "orange", "peach"]
    word = random.choice(words)
    guessed = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("🎮 Welcome to Hangman Game!")
    print("Guess the word, one letter at a time. You have 6 chances.\n")

    while attempts > 0 and '_' in guessed:
        print("Word: " + ' '.join(guessed))
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print(" Good guess!\n")
        else:
            attempts -= 1
            print(f" Wrong guess. Attempts left: {attempts}\n")

    if '_' not in guessed:
        print("\n Congratulations! You guessed the word:", word)
    else:
        print("\n Game over! The word was:", word)

if __name__ == "__main__":
    hangman()
