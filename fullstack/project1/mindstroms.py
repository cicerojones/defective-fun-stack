import turtle

brad = turtle.Turtle()
angie = turtle.Turtle()
window = turtle.Screen()

def draw_square():
    cntr = 0

    for x in range(4):
        brad.forward(100)
        brad.right(90)
        cntr += 1

def draw_triangle():
    cntr = 0
    angie.right(30)
    
    for x in range(3):
        angie.forward(100)
        angie.right(120)
        cntr += 1

        

draw_triangle()
draw_square()
