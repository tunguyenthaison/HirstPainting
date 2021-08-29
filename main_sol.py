import random
import turtle as turtle_module


def func() -> object:
    turtle_module.colormode(255)
    tim = turtle_module.Turtle()
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle()
    color_list = [(197, 165, 119), (144, 81, 56), (220, 201, 138), (61, 95, 121), (165, 150, 54), (136, 162, 180),
                  (131, 34, 23), (52, 119, 87), (73, 37, 29), (190, 96, 82), (145, 177, 150), (100, 76, 80),
                  (165, 147, 157), (21, 92, 68), (28, 59, 75), (225, 177, 167), (59, 44, 46), (133, 29, 33),
                  (180, 202, 179), (26, 84, 89), (88, 147, 129), (13, 70, 58), (42, 65, 89), (180, 99, 102),
                  (216, 181, 186), (182, 191, 204), (112, 128, 146), (71, 63, 55), (111, 136, 140), (178, 199, 202)]

    tim.setheading(225)
    tim.forward(400)
    tim.setheading(0)

    number_of_dots = 100

    for dot_count in range(1, number_of_dots + 1):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(10 * 50)
            tim.setheading(0)
    screen = turtle_module.Screen()
    screen.exitonclick()

func()
