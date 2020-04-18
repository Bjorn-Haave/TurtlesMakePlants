import turtle
from math import pi

class Flock:
    def __init__(self):
        self.screen = turtle.getscreen()
        self.flock = []
        
        self.screen.setworldcoordinates(-100, 0, 100, 200)
        
        my_turtle = PlantTurtle(0,0)
        my_turtle.rotate_abs(90)
        self.flock.append(my_turtle)
        
    def step(self):
        new_flock = []
        for t in self.flock:
            new_flock += t.step()
        else:
            self.flock = new_flock
            

class PlantTurtle:
    def __init__(self, x, y):
        self.health = 1
        self.decay = 0.7
        self.turtle = turtle.Turtle()
        
        self.turtle.speed(0)
        self.turtle.hideturtle()
        # Is this code going to be the same for for place_at()
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        #TODO
        
    def step(self):
        self.move(50 * self.health)
        child = self.copy()
        child.rotate_relative(-20)
        child.health = child.health * child.decay

        self.rotate_relative(45)
        self.health = self.health * self.decay

        return [self, child]
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
        
    def copy(self):
        other = PlantTurtle(self.turtle.xcor(), self.turtle.ycor())
        other.health = self.health
        other.decay = self.decay
        other.turtle = self.turtle.clone()
        return other
        
def main():
    my_flock = Flock()
    for i in range(5):
        my_flock.step()
    input("Go Forward")


if __name__ == "__main__":
    main()