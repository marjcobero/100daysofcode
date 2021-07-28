import turtle
import pandas
from pandas._libs import missing


# Screen Settings
screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# have panda read our csv file
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list() # making our csv file into a list first so its easier to get the data 
guessed_states = []

while len(guessed_states) < 50:
    # our prompt
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit": # if exit is typed it will exit the game
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    # to check if the state is one of the states
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] # to get our data
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)



screen.exitonclick()