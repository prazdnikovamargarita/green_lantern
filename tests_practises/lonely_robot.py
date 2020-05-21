import pytest

class Asteroid:
    def __init__ (self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__ (self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        self.direction = direction
        if self.x > self.asteroid.x:
            raise MissAsteroidError()
        if self.y > self.asteroid.y:
            raise MissAsteroidError()
            
    def turn_left(self, direction):
        turns = {"East": "North"}
        self.direction = turns [self.direction]
    
    def turn_right(self, direction):
        turns = {"North": "Sourth"}
        self.direction = turns [self.direction]
    
    def move_forward(self, direction, x, y):
        moves = {f"{x}, {y}":f"{x+1}, {y}"}
        self. direction = moves[self.direction]
    
    def move_backward(self, direction, x, y):
        moves = {f"{x}, {y}":f"{x+1}, {y}"}
        self. direction = moves[self.direction]

    def robot_in_asteroid(self, x, y, Asteroid):
        asteroid = Asteroid (x, y)
        if (x!= asteroid.x and y!= asteroid.y):
            print ("Not in Asteroid")



class MissAsteroidError (Exception): #кастумна помылка

    pass