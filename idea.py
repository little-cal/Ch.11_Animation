import arcade

SW = 600
SH = 600


class Ball:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col,):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update_ball(self):
        self.pos_x, self.pos_y = arcade.rotate_point(self.pos_x, self.pos_y, 300, 300, 60)
        # self.pos_x += self.dx
        # self.pos_y += self.dy
        #
        # if self.pos_x > 500 or self.pos_y > 500:
        #     self.dx *= -1
        #     self.dy *= -1
        # if self.pos_x < 100 or self.pos_y < 100:
        #     self.dx *= -1
        #     self.dy *= -1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.ball = Ball(300, 400, 3, 3, 15, arcade.color.BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_point(300, 300, arcade.color.BLACK, 15)
        arcade.draw_line(100, 300, 500, 300, arcade.color.BLACK)
        arcade.draw_line(300, 100, 300, 500, arcade.color.BLACK)
        self.ball.draw_ball()

    def on_update(self, dt):
        self.ball.update_ball()


def main():
    window = MyGame(SW, SH, "Drawing Example")
    arcade.run()


if __name__=="__main__":
    main()