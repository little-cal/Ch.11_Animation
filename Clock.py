import arcade

SW = 600
SH = 600


class Hand:
    def __init__(self, pos_x, pos_y, width, height, col, ta):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.col = col
        self.ta = ta

    def draw_hand(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.col, self.ta)

    def update_ball(self):
        pass


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.STEEL_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(300, 300, 180, arcade.color.WHITE, 0, 60)

        arcade.draw_rectangle_filled(445, 300, 45, 10, arcade.color.BLACK)
        arcade.draw_rectangle_filled(300, 445, 45, 10, arcade.color.BLACK, 90)
        arcade.draw_rectangle_filled(155, 300, 45, 10, arcade.color.BLACK)
        arcade.draw_rectangle_filled(300, 155, 45, 10, arcade.color.BLACK, 90)

        arcade.draw_rectangle_filled(400, 400, 45, 10, arcade.color.BLACK, -45)

        arcade.draw_rectangle_filled(430, 355, 45, 10, arcade.color.BLACK, -30)



    def on_update(self, dt):
        pass


def main():
    window = MyGame(SW, SH, "Drawing Example")
    arcade.run()


if __name__=="__main__":
    main()