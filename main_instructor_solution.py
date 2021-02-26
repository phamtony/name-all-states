import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = []
all_state = data.state.to_list()


#I still wrote out a function to make it more readable
def write_state(state, x, y):
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.goto(x, y)
    new_turtle.write(f"{state}")


while len(state_list) < 50:
    answer_state = screen.textinput(title=f"{len(state_list)}/50 States Correct", prompt="What's another state name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_state if state not in state_list]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    #instructor's solution didn't check for using the answer twice
    if answer_state in all_state and answer_state not in state_list:
        state = data[data.state == answer_state]
        state_list.append(answer_state)
        write_state(answer_state.title(), int(state.x), int(state.y))
