#!/usr/bin/env python3
"""
Will you be mine?
"""


import random
import turtle as t


def makeHeart(size):
    """Draw a single heart based on a custom size."""
    t.forward(size)
    t.circle(size / 2, 180)
    t.right(90)
    t.circle(size / 2, 180)
    t.forward(size)
    t.left(90)


def i_love_you(size, length, depth):
    """Draw 45 recursive loops of hearts."""

    # Recurse until the level of depth (of your love) is reached, then exit
    if depth == 0:
        return
    i_love_you(size * 1.5, length, depth - 1)

    # Draw multiple-colored hearts for the length of the timer
    counter = 360
    while counter > 0:
        heartColor = \
            random.randint(100, 255), \
            random.randint(100, 255), \
            random.randint(100, 255)
        t.color(heartColor)
        t.fillcolor(heartColor)
        t.begin_fill()
        makeHeart(size)
        t.end_fill()
        t.left(45)
        counter = counter - 45


def main():
    """Configuring the Valentine Machine and iterating across the screen."""
    t.speed(0)
    t.colormode(255)

    i_love_you(20, 0, 8)
    t.back(100)
    t.color("black")
    t.write(
        "I love you",
        move=False,
        align="left",
        font=("Comfortaa", 24, "bold"))
    t.exitonclick()


main()
