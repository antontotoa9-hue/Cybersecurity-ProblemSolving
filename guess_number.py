# Simple guess-the-number game
# Run with: python guess_number.py

secret_number = 42  # secret number to guess

print("Guess the secret number!")

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if guess < secret_number:
        print("Too low, try again.")
    elif guess > secret_number:
        print("Too high, try again.")
    else:
        print("Correct! You guessed the secret number.")
        break
