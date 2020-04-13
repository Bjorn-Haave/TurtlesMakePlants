import turtle

class PlantTurtle:
    def __init__(self):
        self.health = 1
        self.turtle = turtle.Turtle()
        #TODO
        
    def step(self):
        self.turtle.forward(10)
        #TODO
        
    def place_at(self, x, y):
        pass
        #TODO
        
    def rotate_relative(self, theta):
        pass
        #TODO
    
    def rotate_abs(self, theta):
        pass
        #TODO
        
    def move(self, dist):
        pass
        #TODO
        
    def update(self):
        pass
        #TODO
        
def main():
    s = turtle.getscreen()
    my_turtle = PlantTurtle()
    my_turtle.step()
    input()
    
if __name__ == "__main__":
    main()