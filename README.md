# _Hangman'os'_

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

![Right Guesses](/assets/images/Right-Guesses.png)


- __Hangman Stages__
 
  - The hangman stages is just the visual feedback of how many attempts are lefting.
  - Each time the user guesses wrong, a part of the hangman will be drawn, first the head, then the torso, arms and finally the legs, ending the game.

![Hangman Stages](/assets/images/Hangman-Stages.png)

- __Game Over Menssage_
 
  - When the game is over, as a result of the user running out of attempts or the correct word is guessed, a message with the user result will be displayed, and then the mystery word will be revealed.
  - Lastly, the user will be asked if he would like to keep playing or not, if he does want, then a new word will be picked, restarting the game, otherwise the game will exit, just the letters 'y' or 'n' will be accepted as a input, lower or upper case.

![Hangman Stages](/assets/images/Game-Over.png)

### Features Left to Implement

- Allow the user to get a hint to guess the word.
- Allow user to choose the dificulty, easy, medium or hard.
  - In the easy mode, the first letter is shown.
  - In the medium mode, no special rules will apply.
  - In the hard mode, the user starts with the head, torso and arms drew, leaving just two attempts to guess the word.

## Testing

- I have tested the code by the following methods:
 - Passed on the validator code PEPE8, no issues found.
 - I manually tested the code, passing invalids inputs.
 - I tried all possibles ways to win or lose the game, and no bugs were found.
 - The game was tested on Heroku terminal and on the local terminal.

## Validator Testing

- No errors were returned when passing through the official [PEP8](https://pep8ci.herokuapp.com/) validator.

## Bugs

- BLA BLA

# Deployment

> This project was deployed at Heroku, steps for deploy are listed bellow:
> fork or clone the repository.
> Creat a new Heroku app.
> Set up the configs for the deployment.
> Link the Heroku app to the repository, then Deploy.

- The live link can be found here: [My Game]()

## Credits:

- __Content__ 
    - BLA BLA