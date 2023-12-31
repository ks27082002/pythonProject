import turtle
import pandas
screen = turtle.Screen()

image = "blank_states_img.gif"
screen.addshape("blank_states_img.gif")
turtle.shape(image)


data = pandas.read_csv("50_states.csv")

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Whats another state's name").title()
    print(answer_state.capitalize())

    if answer_state == "Exit":
        missing_states = [state for state in data.state.to_list() if state not in guessed_states]
        # for state in data.state.to_list():
        #     if state not in guessed_states:
        #         missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break



    if answer_state in data.state.to_list():
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




