'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random


SW = 600
SH = 600


class Ball:

    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dy = dy
        self.dx = dx
        self.rad = rad
        self.col = col

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update_ball(self):
        self.pos_y += self.dy

        if self.pos_y > 500 or self.pos_y < 100:
            self.dy *= -1


class Ball2(Ball):
    def __init__(self, pos_x, pos_y, dy, dx, rad, col):
        super().__init__(pos_x, pos_y, dy, dx, rad, col)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def update_ball(self):
        self.pos_x += self.dx

        if self.pos_x < 100 or self.pos_x > 500:
            self.dx *= -1


class Ball3(Ball):
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        super().__init__(pos_x, pos_y, dx, dy, rad, col)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def update_ball(self):
        self.pos_x, self.pos_y = arcade.rotate_point(self.pos_x, self.pos_y, 300, 300, 45)
        # self.pos_x += self.dx
        # self.pos_y += self.dy


class Ball4(Ball):
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        super().__init__(pos_x, pos_y, dx, dy, rad, col)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def update_ball(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        # (500, 500), (500, 100), (100, 500), (100, 100)

        if self.pos_x > 500 and self.pos_y > 500:
            self.dx *= -1
            self.dy *= -1
        if self.pos_x < 100 and self.pos_y < 100:
            self.dx *= -1
            self.dy *= -1
        if self.pos_x > 500 and self.pos_y < 100:
            self.dx *= -1
            self.dy *= -1
        if self.pos_x < 100 and self.pos_y > 500:
            self.dx *= -1
            self.dy *= -1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        # self.ball = Ball(300, 100, 0, 4.5, 15, arcade.color.AUBURN)
        # self.ball4 = Ball(300, 500, 0, 4.5, 15, arcade.color.AUBURN)
        # self.ball2 = Ball2(100, 300, 0, 4.5, 15, arcade.color.AUBURN)
        # self.ball5 = Ball2(500, 300, 0, 4.5, 15, arcade.color.AUBURN)

        self.ball3 = Ball3(300, 500, 2, 2, 15, arcade.color.AUBURN)
        self.ball6 = Ball3(100, 300, 2, 2, 15, arcade.color.AUBURN)
        self.ball7 = Ball3(500, 300, 2, 2, 15, arcade.color.AUBURN)
        self.ball8 = Ball3(300, 100, 2, 2, 15, arcade.color.AUBURN)

        self.ball13 = Ball3(450, 150, 2, 2, 15, arcade.color.AUBURN)
        self.ball14 = Ball3(150, 450, 2, 2, 15, arcade.color.AUBURN)
        self.ball15 = Ball3(450, 450, 2, 2, 15, arcade.color.AUBURN)
        self.ball16 = Ball3(150, 150, 2, 2, 15, arcade.color.AUBURN)

        # self.ball9 = Ball4(500, 500, 4.5, 4.5, 15, arcade.color.AUBURN)
        # self.ball10 = Ball4(500, 100, -4.5, 4.5, 15, arcade.color.AUBURN)
        # self.ball11 = Ball4(100, 100, 4.5, 4.5, 15, arcade.color.AUBURN)
        # self.ball12 = Ball4(100, 500, 4.5, -4.5, 15, arcade.color.AUBURN)

    def on_draw(self):
        arcade.start_render()
        # self.ball.draw_ball()
        # self.ball2.draw_ball()
        self.ball3.draw_ball()
        # self.ball4.draw_ball()
        # self.ball5.draw_ball()
        self.ball6.draw_ball()
        self.ball7.draw_ball()
        self.ball8.draw_ball()
        # self.ball9.draw_ball()
        # self.ball10.draw_ball()
        # self.ball11.draw_ball()
        # self.ball12.draw_ball()
        self.ball13.draw_ball()
        self.ball14.draw_ball()
        self.ball15.draw_ball()
        self.ball16.draw_ball()

    def on_update(self, dt):
        # self.ball.update_ball()
        # self.ball2.update_ball()
        self.ball3.update_ball()
        # self.ball4.update_ball()
        # self.ball5.update_ball()
        self.ball6.update_ball()
        self.ball7.update_ball()
        self.ball8.update_ball()
        # self.ball9.update_ball()
        # self.ball10.update_ball()
        # self.ball11.update_ball()
        # self.ball12.update_ball()
        self.ball13.update_ball()
        self.ball14.update_ball()
        self.ball15.update_ball()
        self.ball16.update_ball()


def main():
    window = MyGame(SW, SH, "Drawing Example")
    arcade.run()



if __name__=="__main__":
    main()

