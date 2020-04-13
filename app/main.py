import turtle
from math import pi

class PlantTurtle:
    def __init__(self, x, y):
        self.health = 1
        self.decay = 0.5
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        #TODO
        
    def step(self):
        self.move(50 * self.health)
        self.rotate_relative(20)
        self.health = self.health * self.decay
        #TODO
        
    def place_at(self, x, y):
        pass
        #TODO
        
    def rotate_relative(self, theta):
        self.turtle.left(theta)
    
    def rotate_abs(self, theta):
        self.turtle.setheading(theta)
        
    def move(self, dist):
        self.turtle.forward(dist)
        
    def update(self):
        pass
        #TODO
        
def main():
    s = turtle.getscreen()
    s.setworldcoordinates(-100, 0, 100, 200)
    my_turtle = PlantTurtle(0,0)
    my_turtle.rotate_abs(90)
    for i in range(5):
        my_turtle.step()
        input()
    
if __name__ == "__main__":
    main()