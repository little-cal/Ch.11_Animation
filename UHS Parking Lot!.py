import arcade
import random

SW = 600
SH = 600


class Car:
    def __init__(self, pos_x, pos_y, width, height, dx, dy, col, ta):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.dx = dx
        self.dy = dy
        self.col = col
        self.ta = ta

    def draw_car(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.col, self.ta)

    def update_car(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        if self.pos_y - self.width >= 600:
            self.pos_x = 700
            self.pos_y = 300
            self.dx = -5
            self.dy = 0
            self.ta = 90

        if self.pos_x + self.width <= -250:
            self.pos_x = 300
            self.pos_y = -150
            self.dx = 0
            self.dy = 5
            self.ta = 0


class Background:
    def __init__(self, pos_x, pos_y, width, height, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.col = col

    def draw_background(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.col)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.background = Background(300, 300, 600, 600, arcade.color.RED)
        self.clock = 0
        self.y = -150
        self.car_list = []

        for i in range(6):
            col = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
            dx = 0
            dy = 5
            x = 300
            ta = 0
            self.car = Car(x, self.y, 50, 100, dx, dy, col, ta)
            self.car_list.append(self.car)
            self.y -= 300

    def on_draw(self):
        arcade.start_render()
        self.background.draw_background()
        arcade.draw_rectangle_filled(300, 300, 50, 600, arcade.color.BLACK)
        arcade.draw_rectangle_filled(300, 300, 50, 600, arcade.color.BLACK, 90)

        for car in self.car_list:
            car.draw_car()

    def on_update(self, dt):
        self.clock += dt
        if self.clock <= 1:
            self.background.col = arcade.color.RED
        elif self.clock <= 2:
            self.background.col = arcade.color.BLUE
        elif self.clock <= 3:
            self.background.col = arcade.color.WHITE
        else:
            self.clock = 0

        for car in self.car_list:
            car.update_car()


def main():
    window = MyGame(SW, SH, "UHS PARKING LOT!")
    arcade.run()


if __name__=="__main__":
    main()