from turtle import Turtle, Screen
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        food_x_pos = random.randint(-280, 280)
        food_y_pos = random.randint(-280, 280)
        self.goto(food_x_pos, food_y_pos)
