import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# def get_mouse_click_coor(x,y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor())
# turtle.mainloop()
guessed_list = []

while len(guessed_list) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 States Correct", prompt="What's another state's name?")

    if answer_state in all_states:
        guessed_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# If answer_state is one of the fifty from data
# Create a turtle to place that on the map
screen.exitonclick()
