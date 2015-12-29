import turtle

brad = turtle.Turtle()
window = turtle.Screen()


def draw_square():
    cntr = 0

    for x in range(4):
        brad.forward(100)
        brad.right(90)
        cntr += 1


def draw_squares(n):
    "Draw n squares, changing the angle of each"

    for x in range(n):
        draw_square()
        brad.right(10)


draw_squares(10)
