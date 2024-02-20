# US States Guessing Game

⚡This Python script implements a simple game where users guess the names of US states interactively using the Turtle graphics library. The game provides a graphical interface using the Turtle module and utilizes data from a CSV file containing information about the US states.

## Libraries
- turtle ✔
- pandas ✔

![us_states](https://github.com/HarshanaPrabhath/US_State_game_Python/assets/132127313/eabe873d-2218-46ea-8bf3-b703f473b0ae)

### ⚡⚡Usage
1. Follow the prompts to guess the names of the US states.
2. Enter the name of the state when prompted. The game will display the name of the state on the map if it's correct.
3. To exit the game at any time, type "Exit" when prompted for a state name.
4. After exiting, the script will generate a CSV file named `to_learn.csv` containing the names of the states that were not guessed correctly.

###⚡⚡ How It Works
- The script reads the `50_states.csv` file, which contains data about the US states including their names and coordinates.
- It initializes a Turtle screen and sets a background image of the US map.
- Users are prompted to guess the names of the US states. The game keeps track of correct guesses and displays them on the map.
- If the user decides to exit the game, the script generates a CSV file `to_learn.csv` containing the names of the states that were not guessed correctly.


