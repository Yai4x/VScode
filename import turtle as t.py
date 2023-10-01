import turtle as t

def draw_heart():
    t.fillcolor('#FFA500')
    t.begin_fill()
    t.left(140)
    t.forward(224)
    
    for _ in range(200):
        t.right(1)
        t.forward(2)
    
    t.left(120)
    
    for _ in range(200):
        t.right(1)
        t.forward(2)
    
    t.forward(224)
    t.end_fill()
    
def write_text():
    t.penup()
    t.goto(-125, 100)  # Adjust the position for text
    t.pendown()
    t.color('black')
    t.write("Thank You for Listening", font=("Arial", 18, "bold"))

# Create a Turtle screen
screen = t.Screen()
screen.bgcolor("#ffe6b3")

# Set up the Turtle
t.speed(0)  # Fastest drawing speed
t.penup()
t.goto(0, -100)  # Position the heart at the center
t.pendown()

# Call the function to draw the heart
draw_heart()

# Call the function to write the text inside the heart
write_text()

# Close the Turtle graphics window on click
screen.exitonclick()
