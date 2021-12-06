from turtle import Screen
from name_writer import NameWriter
import pandas

screen = Screen()
name_writer = NameWriter()
screen.bgpic("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
x_positions = data["x"].to_list()
y_positions = data["y"].to_list()

game_on = True
amount_correct = 0
amount_guessed = 0
completed_states = []
missed = []
while game_on:
    user_input = screen.textinput(f"{amount_correct}/50 States Correct", "Name a state:").title()

    if user_input in states and user_input not in completed_states:
        index = states.index(user_input)
        position = (x_positions[index], y_positions[index])
        name_writer.write_state(position=position, state=user_input)
        amount_correct += 1
        completed_states.append(user_input)

    if amount_correct == 50:
        name_writer.game_over()
        game_on = False

    if amount_guessed == 50 or user_input == "Exit":
        game_on = False
        for missed_states in states:
            if missed_states not in completed_states:
                missed.append(missed_states)
        missed_data = pandas.DataFrame(missed)
        missed_data.to_csv("states_to_learn.csv")

    amount_guessed += 1
