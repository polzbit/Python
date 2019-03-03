import turtle

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)
    
def draw_art():
    canvas = turtle.Screen()
    canvas.bgcolor("blue")

    dan = turtle.Turtle()
    dan.shape("circle")
    dan.color("white")
    dan.speed(12)
    for i in range(36):
        draw_square(dan)
        dan.right(10)
    canvas.exitonclick()

def main():
    draw_art()

if __name__ == "__main__": main()