import turtle

angie = turtle.Turtle()


def draw_triangle():
    cntr = 0

    for x in range(3):
        angie.forward(100)
        angie.right(120)
        cntr += 1


def draw_triangles(n):
    "Draw n triangles, changing the angle of each"

    for x in range(n):
        draw_triangle()
        angie.right(10)


draw_triangles(30)
