# __Hangman'os'_

Hangman'os' is a pure Python language program, running Code Institute mock terminal deployed on Heroku.

You can use your memory skills, challenging yourself to try to find the right word while feeling the nostalgia of this amazing game.

![Responsice Mockup](/assets/images/ResponsiceMockup.png)

## How to play

The game consists of a simple Hangman game, well-known for most of us, being present day by day in our childhood. As a brief resume of the game, we can say that is a word guess game with six attempts to win, in this project the computer gets a random word and display its length to the user, who can guess a letter of the word or the whole word, if the user entered the wrong letter, will be displayed for him, the head, after the torso and so on, otherwise if he guesses the right one, the corresponding letter and its position on the word will be displayed for him.

## Features
### Existing Features

- __Random Word Generation__
 
  - A message to welcome the user to the game is displayed.
  - The gallows pole is displayed to the user.
  - The user can see the word length and the mystery letters are displayed as underscores.

![Land Page](/assets/images/Start-Page.png)

- __Guesses Conditions__
 
  - The user can guess the letters according to the following conditions:
    - Only alphabetic characters are inputted.
    - Only one letter per turn or the word itself.
    - Only new guesses, assuring the user did not input the same letter again.

![Guesses Conditions](/assets/images/Guesses-Conditions.png)

- __Right Guesses__

- If the user guess the letter, the letter would be shown in its corresponding position at the word, even if the letter occurs twice at the word.

![Right Guesses](/assets/images/Right-Guesses.pngh)


- __Hangman Stages__
 
  - The hangman stages is just the visual feedback of how many attempts are lefting.
  - Each time the user guesses wrong, a part of the hangman will be drawn, first the head, then the torso, arms and finally the legs, ending the game.

![Hangman Stages](/assets/images/Right-Guesses.png)
