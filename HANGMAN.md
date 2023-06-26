# Hangman game in python

#### A list of words is defined, and a random word is chosen using the random.choice() function. The game starts with an initial number of tries set to 6. 

#### A while loop continues until the number of tries reaches 0 or the player correctly guesses the word. 
- Inside the loop, the current state of the word is displayed, with blank spaces for unguessed letters. 
- The player is asked to enter a letter, and the input is checked against the chosen word. If the guess is correct, the letter is added to the list of guessed letters. If the guess is incorrect, the number of tries is decreased by 1, and the letter is added to the guessed letters list.

#### The function `draw_hangman(tries)` is added to print the stick figure representation corresponding to the number of incorrect tries. 
- The `draw_hangman()` function takes the number of tries as an argument and prints the appropriate representation using a list of ASCII art strings.
- It is called inside the main while loop, after printing the current state of the game. The stick figure is displayed each time a letter is guessed or the game ends.

#### Once the loop ends, the program checks if the player has guessed the word or not. 
#### If the number of tries reaches 0, the game is over and the correct word is displayed.

## Info
The exact origin and history of the game Hangman are not entirely clear, as it has evolved over time and its roots can be traced back to various sources.

One theory suggests that Hangman could have originated in Victorian England as a parlor game called "Birds, Beasts, and Fishes." Another theory suggests that Hangman has its roots in the traditional paper-and-pencil game of "Bee and Flower," which was played in ancient China.

Over time, Hangman has become a popular game across different cultures and is now commonly played on digital platforms as well. It has also been adapted into various formats, including video games, mobile apps, and online multiplayer versions.

##### The game has a significant history in relation to programming and computer science.

One of the earliest mentions of the Hangman game in computer science can be traced back to the 1960s when computer programming was gaining momentum. Hangman was often used as a programming exercise to teach beginners the fundamentals of programming languages and concepts. It provided a practical application for understanding concepts such as loops, conditionals, input/output, and string manipulation.

In the early days of computer programming, Hangman was implemented using simple text-based interfaces, with players guessing letters and the program displaying the state of the word and the hangman figure. It helped students practice coding skills and problem-solving while developing an interactive game. It involves tasks such as handling user input, managing data structures, implementing game logic, and displaying output.
