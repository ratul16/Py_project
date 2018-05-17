import turtle
from alphabat import alphabet

myPen = turtle.Turtle()
myPen.speed(0)
window = turtle.Screen()
window.bgcolor("#ecf0f1")
myPen.pensize(2)

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
fontSize = 20
characterSpacing = 5
fontColor = "#e74c3c"
message = "Hello Zeba ghum theke uthar shomoy hoise"
displayMessage(message, fontSize, fontColor, -600, 0)
turtle.done()
