import random

def hangman():
    words = ['apple', 'banana', 'orange', 'watermelon', 'strawberry']
    word = random.choice(words)
    guessed_letters = []
    tries = 6
    
    while tries > 0:
        guessed_word = ''
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += '_'
        
        print("Guess the word: ", guessed_word)
        print("Tries left: ", tries)
        
        if guessed_word == word:
            print("Congratulations! You guessed the word correctly.")
            break
        
        guess = input("Enter a letter: ")
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            print("Good guess!")
            guessed_letters.append(guess)
        else:
            print("Oops! That letter is not in the word.")
            tries -= 1
            guessed_letters.append(guess)
        
        print("----------")
        draw_hangman(tries)
    
    if tries == 0:
        print("Game over! The word was:", word)
        draw_hangman(tries)

def draw_hangman(tries):
    stages = [  # Final state: head, torso, both arms, and both legs
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # Head, torso, both arms, and one leg
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        ''',
        # Head, torso, both arms
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        ''',
        # Head, torso, one arm
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        ''',
        # Head and torso
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        ''',
        # Head
        '''
           --------
           |      |
           |      O
           |
           |
           |
           -
        ''',
        # Initial empty state
        '''
           --------
           |      |
           |
           |
           |
           |
           -
        '''
    ]
    print(stages[tries])

hangman()
