'''
# 11.0 Jedi Training (50pts)  Name:________________



 
CHAPTER 11 FINAL CODE QUESTIONS: (10pts)
--------------------------------
1.) Where is the ball's original location?
initial values put in for pos_x and pos_y
2.) What are the variables dx and dy?
How many pixels the x and y position should move when updated
3.) How many pixels/sec does the ball move in the x-direction?
180 pixels/second
4.) How many pixels/sec does the ball move in the y-direction?
120 pixels/second
5.) Which method is run 60 times/second?
delta time, on update
6.) What does this code do?   self.dx *= -1
'reverses' the direction of the x value being updated. mimics a bounce
7.) What does this code do?  self.pos_y += self.dy
adds the dy variable to the y position
8.) What is the width of the window?
640 pixels
9.) What is this code checking?  self.pos_y > SH - self.rad:
if the y position is greater than the screen height minus the radius
10.) What is this code checking? if self.pos_x < self.rad
if the x position is less than the radius, key in bouncing off the edge of screen
'''






'''
30 BOX BOUNCE PROGRAM (20pts)
---------------------
You will want to incorporate lists to modify the
Ball Bounce Program to create the following:

1.) Screen size 600 x 600
2.) Draw four 30px wide side rails on all four sides of the window
3.) Make each side rail a different color.
4.) Draw 30 black boxes(squares) of random size from 10-50 pixels
5.) Animate them starting at random speeds from -300 to +300 pixels/second. 
6.) All boxes must be moving.
7.) Start all boxes in random positions between the rails.
8.) Bounce boxes off of the side rails when the box edge hits the side rail.
9.) When the box bounces change its color to the rail it just hit.
10.)Title the window 30 Boxes

Helpful Hints:
1.) When you initialize the MyGame class create an empty list called self.boxlist=[] to hold all of your boxes.
2.) Then use a for i in range(30): list to instantiate boxes and append them to the list.
3.) In the on_draw section use: for box in self.boxlist: box.draw_box()
4.) Also in the on_draw section draw the side rails.
5.) In the on_update section use: for box in self.boxlist: box.update_box()
'''
import arcade
import random

SW = 600
SH = 600
#
#
# class Box:
#     def __init__(self, left, right, top, bottom, dx, dy, col):
#         self.left = left
#         self.right = right
#         self.top = top
#         self.bottom = bottom
#         self.dx = dx
#         self.dy = dy
#         self.col = col
#
#     def draw_box(self):
#         arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top, self.bottom, self.col)
#
#     def update_box(self):
#         self.top += self.dy
#         self.bottom += self.dy
#
#         self.left += self.dx
#         self.right += self.dx
#
#         #bounce off edge of screen
#
#         if self.left <= 30:
#             self.dx *= -1
#             self.col = arcade.color.RED
#         elif self.right >= SW - 30:
#             self.dx *= -1
#             self.col = arcade.color.BLUE
#         if self.top >= SH - 30:
#             self.dy *= -1
#             self.col = arcade.color.YELLOW
#         elif self.bottom <= 30:
#             self.dy *= -1
#             self.col = arcade.color.GREEN
#
#
# class MyGame(arcade.Window):
#     def __init__(self, width, height, title):
#         super().__init__(width, height, title)
#         arcade.set_background_color(arcade.color.ASH_GREY)
#         self.box_list = []
#         for i in range(30):
#             left = random.randint(30, 520)
#             right = left + random.randint(10, 50)
#             bottom = random.randint(30, 520)
#             top = bottom + random.randint(10, 50)
#             x = random.randint(-5, 5)
#             y = random.randint(-5, 5)
#             if x == 0 or y == 0:
#                 x = random.randint(-5, 5)
#                 y = random.randint(-5, 5)
#             self.box = Box(left, right, top, bottom, x, y, arcade.color.BLACK)
#             self.box_list.append(self.box)
#
#     def on_draw(self):
#         arcade.start_render()
#         arcade.draw_rectangle_filled(585, 300, 30, 600, arcade.color.BLUE)
#         arcade.draw_rectangle_filled(15, 300, 30, 600, arcade.color.RED)
#         arcade.draw_rectangle_filled(300, 585, 600, 30, arcade.color.YELLOW)
#         arcade.draw_rectangle_filled(300, 15, 600, 30, arcade.color.GREEN)
#         for box in self.box_list:
#             box.draw_box()
#
#     def on_update(self, dt):
#         for box in self.box_list:
#             box.update_box()
#
#
# def main():
#     window = MyGame(SW, SH, "30 Boxes")
#     arcade.run()
#
#
# if __name__ == "__main__":
#     main()





'''
SNOWFALL  (20pts)
--------
Try to create the snowfall animation by meeting
the following requirements:

1.) Create a 600 x 600 window with black background
2.) Window title equals "Snowfall"
3.) Crossbars 10 px wide. Snow must be outside!
4.) Make snowflake radius random between 1-3
5.) Randomly start snowflakes anywhere in the window.
6.) Random downward speed of -4 to -1
7.) Start snowflakes again at random x from 0-600 and random y from 600-700
8.) Generate 300 snowflakes
9.) Color snowflake #1 red just for fun.
10.) All other snowflakes should be white.
'''


class Snowflake:
    def __init__(self, pos_x, pos_y, dy, dx, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dy = dy
        self.dx = dx
        self.rad = rad
        self.col = col

    def draw_flake(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update_flake(self):
        self.pos_y -= self.dy
        self.pos_x += self.dx

        if self.pos_y < self.rad:
            self.pos_y = random.randint(600, 700)
            self.pos_x = random.randint(0, 600)
            self.rad = random.randint(1, 3)

        if self.pos_x - self.rad > SW or self.pos_x < self.rad:
            self.dy = random.random() + random.randint(1, 4)
            self.dx = random.random() + random.randint(-3, 3)
            self.pos_y = random.randint(600, 700)
            self.pos_x = random.randint(0, 600)
            self.rad = random.randint(1, 3)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.flake_list = []
        for i in range(500):
            x = random.randint(0, 600)
            y = random.randint(0, 600)
            dy = random.random() + random.randint(1, 3)
            dx = random.random() + random.randint(-2, 2)
            rad = random.randint(1, 3)
            if i == 1:
                self.flake = Snowflake(x, y, dy, dx, rad, arcade.color.RED)
            else:
                self.flake = Snowflake(x, y, dy, dx, rad, arcade.color.WHITE)
            self.flake_list.append(self.flake)

    def on_draw(self):
        arcade.start_render()
        for flake in self.flake_list:
            flake.draw_flake()
        arcade.draw_rectangle_filled(300, 300, 600, 10, arcade.color.BOLE)
        arcade.draw_rectangle_filled(300, 300, 10, 600, arcade.color.BOLE)

    def on_update(self, dt):
        for flake in self.flake_list:
            flake.update_flake()


def main():
    window = MyGame(SW, SH, "Snowfall")
    arcade.run()


if __name__=="__main__":
    main()