import random
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter you color: ")
colors = ["red", "green", "yellow", "purple", "pink", "black"]

is_race_on = False
start = -100
turtle_list = []
for every in range(6):
    new_turtle = Turtle(shape="turtle")
    turtle_list.append(new_turtle)
    new_turtle.color(colors[every])
    new_turtle.penup()
    turtle_list[every].goto(x=-230, y=start)
    start = start + 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()
