import turtle
import pandas

# set up the screen and bg image
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

timmy = turtle.Turtle()

# read csv file using pandas
data = pandas.read_csv("50_states.csv")

# convert us states to a list
state_list = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    user_state_input = screen.textinput(title=f"{len(guessed_states)}/50 Correct Guesses",
                                        prompt="Enter the state name").title()
    if user_state_input == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("to_learn.csv")

        break

    if user_state_input in state_list:
        guessed_states.append(user_state_input)
        data_raw = data[data.state == user_state_input]
        x_cor = int(data_raw.x.iloc[0])
        y_cor = int(data_raw.y.iloc[0])

        timmy.penup()
        timmy.hideturtle()
        timmy.goto(x_cor, y_cor)
        timmy.write(f"{user_state_input}", font=("Arial", 11, "normal"))
