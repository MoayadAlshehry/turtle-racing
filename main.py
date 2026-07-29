from turtle import Turtle, Screen
import random
turtles = [Turtle(), Turtle(), Turtle(), Turtle(), Turtle(), Turtle()]
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
for i in range(len(turtles)):
    turtles[i].shape("turtle")
    turtles[i].color(colors[i])

screen = Screen()
screen.setup(500 , 400)
is_race_on = False

user_bet = screen.textinput("Make your bet" , "which turtle will win the race? Enter a color:")
if user_bet in colors:
    is_race_on = True


for i in reversed(range(len(turtles))):
    y = i * 30
    turtles[i].penup()
    turtles[i].color()
    turtles[i].goto(-230, y - (len(turtles) - 1) * 15)

while is_race_on:
    for t in turtles:
        dist = random.randint(0, 10)
        t.forward(dist)
        if t.xcor() > 225:
            winning = t.pencolor()
            if winning == user_bet:
                print(f"You've won! The {winning} turtle is the winner!")
            else:
                print(f"You've lost! The {winning} turtle is the winner!")
            is_race_on = False
            break

screen.exitonclick()
