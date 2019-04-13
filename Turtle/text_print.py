import turtle
from alphabat import alphabet

myPen = turtle.Turtle()
myPen.speed(1)
window = turtle.Screen()
window.bgcolor("#ecf0f1")
myPen.pensize(4)

#Funtion Starts from here

def displayMessage(message, fontSize, color, x, y):
    myPen.color(color)
    message = message.upper()

    for character in message:
        if character in alphabet:
            letter = alphabet[character]
            myPen.penup()
            for dot in letter:
                myPen.goto(x + dot[0] * fontSize, y + dot[1] * fontSize)
                myPen.pendown()

            x += fontSize

        if character == " ":
            x += fontSize
        x += characterSpacing



# Main Program Starts Here
fontSize = 50
characterSpacing = 5
fontColor = "#e74c3c"
message = "Hello World"
displayMessage(message, fontSize, fontColor, -300, 0)
turtle.done()
