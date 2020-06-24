import random
random.seed()
chosen_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
lives = 8
guesses = set()
print("H A N G M A N")
while True:
    if input("Type 'play' to play the game, 'exit' to quit: ") == "exit":
        break

    while lives > 0:
        hint = ""

        for letter in chosen_word:
            if letter in guesses:
                hint += letter
            else:
                hint += "-"

        if hint == chosen_word:
            print(f"You guessed the word!\nYou survived!")
            break

        guess = input(f"\n{hint}\nInput a letter: ")

        if len(guess) != 1:
            print("You should input a single letter")
            continue

        if not (guess.isalpha() and guess.islower()):
            print("It is not an ASCII lowercase letter")
            continue

        if guess in guesses:
            print("You already typed this letter")
            continue

        guesses.add(guess)
        if guess not in chosen_word:
            lives -= 1
            print("No such letter in the word")
    else:
        print("You are hanged!")

