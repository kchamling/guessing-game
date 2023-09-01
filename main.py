import random

secret_number = random.randint(1, 100)
print(secret_number)
guess_count = 0
guess_limit = 5
out_of_guesses = False
user_guess = None

while user_guess != secret_number and out_of_guesses == False:
    if guess_count < guess_limit:
        user_guess = int(input("Please enter a number(1-100) : "))
        guess_count += 1
        if user_guess < secret_number:
            print("Too Low. Guess higher!") 
        elif user_guess > secret_number:
            print("Too High. Guess lower!")
        else:
            print("Invalid input!")
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Sorry! You lose and ran out of guesses.")
else:
    print(f"You Win. You guessed in {guess_count} attempts.")