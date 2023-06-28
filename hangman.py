def hangman_game():
    hangmanWord = "whiteboard"
    linesOfChar = ""

    for char in hangmanWord:
        linesOfChar += "_ "

    triesLeft = 7
    guessed_letters = []

    print(linesOfChar)

    while triesLeft > 0:
        guessed_letter = input('Guess a letter: ')

        if guessed_letter in guessed_letters:
            print("You already guessed that letter!")
        elif guessed_letter in hangmanWord:
            print("Good guess!")
            guessed_letters.append(guessed_letter)
        else:
            print("Wrong guess!")
            triesLeft -= 1

        show_word = ""
        for char in hangmanWord:
            if char in guessed_letters:
                show_word += char + " "
            else:
                show_word += "_ "

        print(show_word)

        if all(char in guessed_letters for char in hangmanWord):
            print("Congratulations! You won!")
            break

        print("Tries left:", triesLeft)

    else:
        print("You lost! The word was:", hangmanWord)

hangman_game()