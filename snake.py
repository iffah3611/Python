import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# --- Screen setup ---
window = turtle.Screen()
window.title("FIRST GAME")
window.colormode(255)
window.bgcolor(255, 182, 193)
window.setup(width=600, height=600)
window.tracer(0)

# --- Snake head ---
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color((171, 65, 97))
head.penup()
head.goto(0, 0)
head.direction = "stop"

# --- Food ---
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("light green")
food.penup()
food.goto(0, 100)

segments = []   # Snake body segments

# --- Scoreboard ---
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("SCORE: 0 HIGH SCORE: 0", align="center",
          font=("Times New Roman", 24, "normal"))

# --- Functions to move snake ---


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)


# --- Key bindings ---
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# --- Main Game Loop ---
while True:
    window.update()

    # Border collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reset score only (high score remains)
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("SCORE: {} HIGH SCORE: {}".format(score, high_score),
                  align="center", font=("Times New Roman", 24, "normal"))

    # Move body segments in reverse order
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move the first segment to head's position
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Check collision with food
    if head.distance(food) < 20:
        # Move food to random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color((171, 65, 97))
        new_segment.penup()
        segments.append(new_segment)

        # Shorten delay (speed up)
        delay = max(0.05, delay - 0.001)

        # Increase the score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("SCORE: {} HIGH SCORE: {}".format(score, high_score),
                  align="center", font=("Times New Roman", 24, "normal"))

    # Check collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the body
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # Reset score only
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("SCORE: {} HIGH SCORE: {}".format(score, high_score),
                      align="center", font=("Times New Roman", 24, "normal"))
            break

    time.sleep(delay)

window.mainloop()
