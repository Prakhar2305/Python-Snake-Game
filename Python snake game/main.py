from turtle import Turtle,Screen
import time
from food import Food


file= open("my_file.txt", "r")    
high_score = file.read()

score=0
screen=Screen()
board=Turtle()
screen.listen()
screen.tracer(0)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.setup(600,600)
food=Food()




jessica=Turtle()
jessica.color("white")
jessica.shape("square")

harvey=Turtle()
mike=Turtle()
harvey.color("white")
mike.color("white")
jessica.penup()
harvey.penup()
mike.penup()

harvey.shape("square")
mike.shape("square")
harvey.setx(-20)
mike.setx(-40)
segments=[jessica,harvey,mike]
screen.update()
game_is_on=True

def turn_right():
    if jessica.heading()!=180:
       jessica.setheading(0)
def turn_left():
    if jessica.heading()!=0:
       jessica.setheading(180)
def up():
    if jessica.heading()!=270:
       jessica.setheading(90)
def down():
    if jessica.heading()!=90:
       jessica.setheading(270)


def game_on():
    global score
    global game_is_on
   # game_is_on=True

    while game_is_on:
        screen.update()
        board.color("blue")
        board.ht()
        board.penup()
        board.sety(260)
        board.write(f"Score:{score}   High Score:{high_score}",False,"Center",("Arial",15,"bold"))

        time.sleep(0.1)
        for seg_num in range(len(segments)-1,0,-1):
            segments[seg_num].goto(segments[seg_num-1].pos())
        segments[0].fd(20)
        screen.onkey(turn_right, "Right")
        screen.onkey(up, "Up")
        screen.onkey(down, "Down")
        screen.onkey(turn_left, "Left")
        if jessica.distance(food) < 15:
            #print("Yayy")
            food.refresh()
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.speed(10)
            segments.append(new_segment)
            score += 1
            board.clear()

        if jessica.xcor() > 300 or jessica.xcor() < -300 or jessica.ycor() < -300 or jessica.ycor() > 300:
            game_is_on = False
            print("You got banged to a wall!\nGame Over :(")
            #game_on()
        for x in range(1, len(segments)):
            if jessica.distance(segments[x]) < 15:
                game_is_on = False
                print("Your snake ate his own tail!\nGame Over!")
                #game_on()
    if score>int(high_score):
        file=open("my_file.txt","w")
        file.write(f"{score}")
    food.ht()
    final_board = Turtle()
    final_board.color("green")
    final_board.ht()
    final_board.penup()


    final_board.write(f"Game Over\nFinal Score:{score}", False, "Center", ("Arial", 40, "bold"))

screen.onkey(game_on, "space")
#with open(/Users/hp/PycharmProjects/day_24/my_file.txt) as file:
screen.exitonclick()
