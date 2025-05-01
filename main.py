import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black") #changes the background of the screen
screen.title("My snake game") #changes the title of the program...
                              #... on the screen
screen.tracer(0)

# Todo 1. create  a snake body

snake= Snake()
food = Food()
score_board = ScoreBoard()

# Todo 3. Control the snake using keyboard controls

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Todo 2. Move the snake

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Todo 4. Detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()

        # Todo 5. Keep track of the score and create a scoreboard
        score_board.increase_score()

    # Todo 6. Figure out when the game should end
    #        Detecting collision with wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280
        or snake.head.ycor() > 280 or snake.head.ycor() > 280):
        game_on = False
        score_board.game_over()


    # Todo 7. Detect collision with it's
    #         tail and game should end as well
    for segment in snake.all_segments[1:]:
         if snake.head.distance(segment) < 10:
            game_on = False
            score_board.game_over()


screen.exitonclick()