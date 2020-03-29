import pytest
from lonely_robot import Robot, Asteroid, MissAsteroidError

class TestRobotCreation:

    def test_paramaters (self):
        x, y = 10,15
        asteroid =Asteroid (x+1, y+1)
        direction = "East"
        robot = Robot (x, y, asteroid, direction)
        
        assert robot.x == 10
        assert robot.y == 15
        assert robot.asteroid == asteroid
        assert robot.direction == direction

    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates", #'параметры, которые будут проверяться в тесте (функции) нижеб что проевяется и какие значения""""
        (
            ((15, 45), (26, 30)),
            ((15, 55), (26, 28 )),
            ((15, 65), (15, 27))
        )

    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises (MissAsteroidError):
            asteroid = Asteroid (*asteroid_size)
            Robot (*robot_coordinates, asteroid)
    
class RobotBehaivors():
    def setup(self):
        x, y = 10,15
        self.asteroid =Asteroid (x+1, y+1)

    @pytest.mark.parametrize(
        "current_direction, expected_direction", #'параметры, которые будут проверяться в тесте (функции) нижеб что проевяется и какие значения""""
        (
            ("North", "West"),
            ("West", "South"),
            ("South", "East")
        )
    )
    def test_turn_life(self, current_direction, expected_direction, x, y, asteroid):
        
        
        robot = Robot (x, y, asteroid,  current_direction)
        robot.turn_left("West")
        assert robot.direction ==  expected_direction
        pass

    def test_turn_right(self, current_direction, expected_direction, x, y, asteroid):
        robot = Robot (x, y, asteroid,  current_direction)
        robot.turn_right("West")
        assert robot.direction ==  expected_direction
        pass

    def test_move_forward(self, direction, x, y, asteroid, current_direction):
        robot = Robot (x, y, asteroid,  current_direction)
        robot.move_forward
        assert Robot (x, y, asteroid,  current_direction) == Robot (x+1, y, asteroid,  current_direction)
    
    def test_move_backward(self, direction, x, y, asteroid, current_direction):
        robot = Robot (x, y, asteroid,  current_direction)
        robot.move_backward
        assert Robot (x, y, asteroid,  current_direction) == Robot (x-1, y, asteroid,  current_direction)

    def test_robot_in_asteroid(self, direction, x, y, asteroid, current_direction):
        robot = Robot(x, y, asteroid, current_direction)
        robot.move_backward
        robot.move_forward
        assert robot.x == asteroid.x
        assert robot.y == asteroid.y
 
