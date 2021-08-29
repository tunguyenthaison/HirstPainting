import io, os
from tkinter import filedialog
from turtle import TurtleScreen

import colorgram
from PIL import Image

palette = colorgram.extract("image.jpeg", 34)
# print(len(palette))

def color_extracted(color):
    """
    :param color: an item from the palette
    :return: a tuple of rgb color
    """
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    return (r, g, b)

rgb_palette = [color_extracted(x) for x in palette]

for _ in range(4):
    rgb_palette.pop(0)

print(rgb_palette)

import turtle as t
import random
STEP = 50
WIDTH, HEIGHT = 11*STEP, 11*STEP

tim = t.Turtle()
tim.hideturtle()
t.colormode(255)
screen = t.Screen()
# screen.reset()

# screen.setup(WIDTH + 4, HEIGHT + 8) # fudge factors due to window borders & title bar
# screen.screensize(WIDTH, HEIGHT)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

counter = 0


tim.penup()
for col in range(1,10):
    # tim.showturtle()
    tim.setposition(STEP, col * STEP)
    rand_color = random.choice(rgb_palette)
    tim.dot(20, rand_color)
    ps = t.getcanvas().postscript(file="art{0:03d}.ps".format(counter))
    counter += 1

    for row in range(1, 10):
        rand_color = random.choice(rgb_palette)
        tim.forward(STEP)
        tim.dot(20, rand_color)
        ps = t.getcanvas().postscript(file="art{0:03d}.ps".format(counter))
        counter += 1

    tim.left(90)
    tim.right(90)
tim.hideturtle()
t.done()

# tim.shape("turtle")
# tim.showturtle()
# print(screen.screensize())


#
# img_list = []
# for i in range(0, 90):
#     name = "art{x:02d}.ps".format(x = i)
#     img_list.append(name)
# print(img_list)
#
# import os
#
# os.system('convert -loop 0 %s anime.gif' % ' '.join(img_list))
#


