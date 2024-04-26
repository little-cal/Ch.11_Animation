import arcade

SW = 600
SH = 600


class Electron:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col,):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def draw_electron(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)
        arcade.draw_circle_outline(self.pos_x, self.pos_y, self.rad, arcade.color.BLACK)

    def update_electron(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        if self.pos_x - self.rad <= 0 and self.pos_y == 25:
            self.dx = 0
            self.dy = 5
        elif self.pos_y + self.rad >= 600 and self.pos_x == 25:
            self.dy = 0
            self.dx = 5
        elif self.pos_x + self.rad >= 600 and self.pos_y == 575:
            self.dx = 0
            self.dy = -5
        elif self.pos_y - self.rad <= 0 and self.pos_x == 575:
            self.dx = -5
            self.dy = 0


class Lightbulb:
    def __init__(self, col_1, col_2):
        self.col_1 = col_1
        self.col_2 = col_2

    def draw_lightbulb(self):
        arcade.draw_rectangle_filled(300, 300, 500, 500, self.col_2)
        arcade.draw_circle_filled(300, SH - 150, 100, self.col_1)
        arcade.draw_rectangle_filled(300, 568, 100, 64, arcade.color.GRAY)
        arcade.draw_line(250, 592, 350, 592, arcade.color.BLACK)
        arcade.draw_line(250, 584, 350, 584, arcade.color.BLACK)
        arcade.draw_line(250, 576, 350, 576, arcade.color.BLACK)
        arcade.draw_line(250, 568, 350, 568, arcade.color.BLACK)
        arcade.draw_line(250, 560, 350, 560, arcade.color.BLACK)
        arcade.draw_line(250, 552, 350, 552, arcade.color.BLACK)
        arcade.draw_line(250, 544, 350, 544, arcade.color.BLACK)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ANTIQUE_BRASS)
        self.lightbulb = Lightbulb(arcade.color.SILVER, arcade.color.BLACK)
        self.counter = -210
        self.electron_list = []
        self.x = 575
        for i in range(44):
            y = 25
            dx = -5
            dy = 0
            self.electron = Electron(self.x, y, dx, dy, 25, arcade.color.COPPER)
            self.electron_list.append(self.electron)
            self.x += 50

    def on_draw(self):
        arcade.start_render()
        for electron in self.electron_list:
            electron.draw_electron()
        arcade.draw_rectangle_filled(575, 25, 50, 50, arcade.color.BLACK_OLIVE)
        arcade.draw_rectangle_outline(575, 25, 50, 50, arcade.color.BLACK)
        arcade.draw_rectangle_filled(525, 25, 50, 50, arcade.color.COPPER)
        arcade.draw_rectangle_outline(525, 25, 50, 50, arcade.color.BLACK)
        arcade.draw_rectangle_filled(498, 25, 4, 15, arcade.color.SILVER)
        arcade.draw_rectangle_outline(498, 25, 4, 15, arcade.color.BLACK)

        self.lightbulb.draw_lightbulb()

    def on_update(self, dt):
        self.counter += 1
        for electron in self.electron_list:
            electron.update_electron()

        while 60 <= self.counter <= 120:
            self.lightbulb.col_1 = arcade.color.YELLOW
            self.lightbulb.col_2 = arcade.color.LIGHT_YELLOW
            self.counter += 1

        while 180 <= self.counter <= 240:
            self.lightbulb.col_1 = arcade.color.SILVER
            self.lightbulb.col_2 = arcade.color.BLACK
            self.counter += 1

        if self.counter >= 240:
            self.counter = 0


def main():
    window = MyGame(SW, SH, "Electricity!")
    arcade.run()


if __name__=="__main__":
    main()