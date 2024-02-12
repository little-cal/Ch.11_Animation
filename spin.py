import arcade
import random
SW = 600
SH = 600


class Line:
    def __init__(self, pos_x, pos_y, w, h, col, ta):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.col = col
        self.ta = ta

    def draw_line(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.w, self.h, self.col, self.ta)

    def update_line(self):
        self.pos_x, self.pos_y = arcade.rotate_point(self.pos_x, self.pos_y, 300, 300, 359)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.line = Line(200, 400, 1, 100, arcade.color.BLACK, 0)
        self.line2 = Line(150, 350, 1, 100, arcade.color.BLACK, 90)
        self.line3 = Line(150, 450, 1, 100, arcade.color.BLACK, 90)
        self.line4 = Line(100, 400, 1, 100, arcade.color.BLACK, 0)
        self.line5 = Line(121, 463, 1, 50, arcade.color.BLACK, 60)
        self.line6 = Line(221, 463, 1, 50, arcade.color.BLACK, 60)
        self.line7 = Line(221, 363, 1, 50, arcade.color.BLACK, 60)
        self.line8 = Line(242, 425, 1, 100, arcade.color.BLACK, 0)
        self.line9 = Line(191, 475, 1, 100, arcade.color.BLACK, 90)
        self.line10 = Line(191, 375, 1, 100, arcade.color.BLACK, 90)
        self.line11 = Line(142, 425, 1, 100, arcade.color.BLACK, 0)
        self.line12 = Line(121, 363, 1, 50, arcade.color.BLACK, 60)

    def on_draw(self):
        arcade.start_render()
        self.line.draw_line()
        self.line2.draw_line()
        self.line3.draw_line()
        self.line4.draw_line()
        self.line5.draw_line()
        self.line6.draw_line()
        self.line7.draw_line()
        self.line8.draw_line()
        self.line9.draw_line()
        self.line10.draw_line()
        self.line11.draw_line()
        self.line12.draw_line()

    def on_update(self, dt):
        self.line.update_line()
        self.line2.update_line()
        self.line3.update_line()
        self.line4.update_line()
        self.line5.update_line()
        self.line6.update_line()
        self.line7.update_line()
        self.line8.update_line()
        self.line9.update_line()
        self.line10.update_line()
        self.line11.update_line()
        self.line12.update_line()


def main():
    window = MyGame(SW, SH, "Drawing Example")
    arcade.run()


if __name__=="__main__":
    main()