from turtle import Screen
from tur import Tur
from cars import Car
import time
from score import Score


class Main:
    def __init__(self):
        self.s = Screen()
        self.s.tracer(0)  
        self.s.bgcolor("black")
        self.s.setup(600, 700)
        self.score = Score(self.s)
        self.tur = Tur(self.s)  
        self.car_manager = Car()  
        self.game_mode()  
        self.s.exitonclick()
        self.game_timer = 500

    def game_mode(self):
        self.s.listen()
        self.s.onkey(self.tur.move, "Up")  
        self.game_loop()

    def game_loop(self):

        result = self.car_manager.move(self.tur.turtle)  
        if result == "crash":
            self.score.game_over()
            return
        self.s.update()
        if self.tur.turtle.ycor() > 290:
            self.score.refresh()
            self.tur.refresh()
            if self.score.score == 4:
                self.score.check_winner()
                return

        self.s.ontimer(self.game_loop, 500)


main = Main()
