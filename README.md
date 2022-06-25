# Cycle
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

```
python3 -m pip install raylib
```

After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.

```
python3 snake 
```

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:

```
root                    (project root folder)
+-- snake               (source code for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Kaden Brown (bro22001@byui.edu)
* Stephanie Clark (sclark@inventoryshield.com)
* Nikita Wong (iamspecial19@gmail.com)

## Contribution
---
* Kaden Brown - Snakes tail grows as they move. Snakes don't start moving until the player starts and won't lose velocity ever.
* Stephanie Clark - Game over cycle. When they collide the game would end. Specifications in the game - Snakes don't move until a key is pressed.
* Nikita Wong - Create Player 2. Work on Player 2 using "I, J, K, and L" keys. Set text and position for Player 2.