import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#To get coordinates within the map
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

score = 0
state_prompt = "What's another state name?"
game_is_on = True
state_list = []
missing_states = []

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()


def write_state(state, x, y):
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.goto(x, y)
    new_turtle.write(f"{state}")


while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt=state_prompt).title()

    if answer_state == "Exit":
        break
    else:
        if data[data.state == answer_state].empty:
            pass
        else:
            state = data[data.state == answer_state]

            if answer_state in state_list:
                pass
            else:
                state_list.append(answer_state)
                write_state(answer_state.title(), int(state.x), int(state.y))
                score += 1

for state in all_state:
    if state in state_list:
        pass
    else:
        missing_states.append(state)

csv_missing_state = {
    "states": missing_states
}

csv_panda_data = pandas.DataFrame(csv_missing_state)
csv_panda_data.to_csv("missing_states.csv")
