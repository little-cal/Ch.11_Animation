import arcade
import random
SW = 600
SH = 600


class Petal:
    def __init__(self, pos_x, pos_y, rad, col_1, col_2, angle, dx, dy):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rad = rad
        self.col_1 = col_1
        self.col_2 = col_2
        self.angle = angle
        self.dx = dx
        self.dy = dy

    def draw_petal(self):
        arcade.draw_ellipse_filled(self.pos_x, self.pos_y, self.rad/2.75, self.rad, self.col_1, self.angle)

    def update_petal(self):
        self.pos_y -= self.dy
        self.pos_x += self.dx

        if self.pos_y < self.rad:
            self.pos_y = random.randint(600, 700)
            self.pos_x = random.randint(0, 600)
            self.rad = random.randint(10, 20)
            self.angle = random.randint(-60, 60)

        if self.pos_x - self.rad > SW or self.pos_x < self.rad:
            self.dy = random.random() + random.randint(1, 4)
            self.dx = random.random() + random.randint(-3, 3)
            self.pos_y = random.randint(600, 700)
            self.pos_x = random.randint(0, 600)
            self.rad = random.randint(10, 20)
            self.angle = random.randint(-60, 60)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.petal_list = []
        # self.background = None
        for i in range(150):
            x = random.randint(0, 600)
            y = random.randint(0, 600)
            dy = random.random() + random.randint(1, 3)
            dx = random.random() + random.randint(-2, 2)
            rad = random.randint(10, 20)
            angle = random.randint(-60, 60)
            self.petal = Petal(x, y, rad, arcade.color.AMARANTH_PINK, arcade.color.WHITE, angle, dx, dy)
            self.petal_list.append(self.petal)

    # def setup(self):
    #     self.background = arcade.load_texture("tree.jpeg")

    def on_draw(self):
        arcade.start_render()

        # arcade.draw_lrwh_rectangle_textured(0, 0, SW, SH, self.background)
        for petal in self.petal_list:
            petal.draw_petal()

    def on_update(self, dt):
        for petal in self.petal_list:
            petal.update_petal()


def main():
    window = MyGame(SW, SH, "Drawing Example")
    # window.setup()
    arcade.run()


if __name__=="__main__":
    main()
