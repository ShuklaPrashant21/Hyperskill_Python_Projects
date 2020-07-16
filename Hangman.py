def Hangman_Game():

        import random
        random.seed()
        word_dict = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
                'Shapes':'square triangle rectangle circle ellipse rhombus trapazoid chevron pentagon hexagon septagon octogon'.split(),
                  'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantalope mango strawberry tomato'.split(),
                  'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split(),
                  'Programming Language Name':'python java kotlin javascript scala sql swift ruby objectivec csharp php brainfuck perl prolog lisp cobra julia'.split()
                 }
                 
        guess_value = random.randint(0, len(word_dict) - 1)   ##Generate random key index.
        chosen_list = word_dict[list(word_dict)[guess_value]] ##Make a list of values of selected key.
        chosen_word = random.choice(chosen_list)              ##Chose random word from list of values.
        guess_Key = list(word_dict)[guess_value]              ##Store random selected key.

        x = 0
        HANGMAN_PICS = [ '''
          +---+
              |
              |
              |
             ===''', '''
          +---+
          O   |
              |
              |
             ===''', '''
          +---+
          O   |
          |   |
              |
             ===''', '''
          +---+
          O   |
         /|   |
              |
             ===''', '''
          +---+
          O   |
         /|\  |
              |
             ===''', '''
          +---+
          O   |
         /|\  |
         /    |
             ===''', '''
          +---+
          O   |
         /|\  |
         / \  |
             ===''','''
          +---+
         [O   |
         /|\  |
         / \  |
             ===''','''
          +---+
         [O]  |
         /|\  |
         / \  |
             ==='''
                   ]

        lives = 9
        guesses = set()
        for a in range(2):
              print("********                        ********")
        print("******** H-A-N-G-M-A-N  G.A.M.E ********")
        for b in range(2):
              print("********                        ********")     
        print("\nYou have guess a word, input each letter and only 8 wrong guesses will be allowed.\nGood Luck!!\n ")
        print("\nThe guess word belongs to '"+guess_Key+"'.")    

        while lives > 0:
                hint = ""

                for letter in chosen_word:
                    if letter in guesses:
                        hint += letter
                    else:
                        hint += "-"

                if hint == chosen_word:
                    print(f"\nBravo, You guessed the word!\nYou survived! Champion")
                    
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
                    print(HANGMAN_PICS[x])
                    x  +=1
                    #life_left = lives - x
                    print("No such letter in the word.")
                    print("Now you have, "+ str(lives)+" guesses left.")

                if x==9:    
                          print("\nYou are hanged!")
                          print('\nSuch a shame, you did not guess a simple word i.e "', str(chosen_word) + ' " ' )
                          print('\nBetter Luck Next Time!')
                        
 Hangman_Game
