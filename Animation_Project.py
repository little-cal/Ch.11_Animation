import arcade
import random
import time

SW = 600
SH = 600


# creating the class for the moon
class Moon:
    # variables necessary for instantiation
    def __init__(self, pos_x, pos_y, rad, col, dx, dy):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rad = rad
        self.col = col
        self.dx = dx
        self.dy = dy

    def draw_moon(self):
        # drawing the moon
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)
        arcade.draw_circle_filled(self.pos_x + 15, self.pos_y + 17, self. rad / 3, (190, 189, 201))
        arcade.draw_circle_filled(self.pos_x - 30, self.pos_y - 10, self.rad / 3.5, (190, 189, 201))
        arcade.draw_circle_filled(self.pos_x - 5, self.pos_y + 20, self.rad / 4, (190, 189, 201))
        arcade.draw_circle_filled(self.pos_x + 15, self.pos_y - 7, self.rad / 4, (190, 189, 201))
        arcade.draw_circle_filled(self.pos_x, self.pos_y - 30, self.rad / 6, (190, 189, 201))

    def update_moon(self):
        # updating position of the moon
        self.pos_x += self.dx
        self.pos_y -= self.dy

        # if x position is too large, resetting position to ~0, 150
        if self.pos_x >= 750:
            self.pos_x = 0 - self.rad
            self.pos_y = 150
            self.dy *= -1

        # reverse movement after y pos is == 400
        if self.pos_y == 400:
            self.dy *= -1


# creating the background class
# allows for manipulation of color
class Background:
    def __init__(self, pos_x, pos_y, width, height, col_1, col_2, col_3, col_step_1, col_step_2, col_step_3):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        # starting colors
        self.col_1 = col_1
        self.col_2 = col_2
        self.col_3 = col_3
        # how much each color should increase/decrease by per frame
        self.col_step_1 = col_step_1
        self.col_step_2 = col_step_2
        self.col_step_3 = col_step_3

    def draw_background(self):
        # drawing the background with initial colors
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height,
                                     (self.col_1, self.col_2, self.col_3))

    def update_background(self):
        # increasing colors by indicated step amount
        self.col_1 += self.col_step_1
        self.col_2 += self.col_step_2
        self.col_3 += self.col_step_3

        # reversing color change after col 3 has hit 270 or greater
        if self.col_3 >= 270:
            self.col_step_1 *= -1
            self.col_step_2 *= -1
            self.col_step_3 *= -1

        # when col 3 is 0 or less than 0 multiply by -1 to make the color change positive again
        if self.col_3 <= -15:
            self.col_step_1 *= -1
            self.col_step_2 *= -1
            self.col_step_3 *= -1


# creating the cloud piece class
# pieces are made and 'assembled' into a cloud later
class CloudPiece:
    def __init__(self, pos_x, pos_y, rad, col, dx):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rad = rad
        self.col = col
        self.dx = dx

    def draw_cloud(self):
        # drawing the circle/piece that make up a cloud
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update_cloud(self):
        # updating the cloud position and resetting it after it has gone off the screen
        self.pos_x += self.dx

        if self.pos_x > 800:
            self.pos_x = -150


# class for stars
# allows for hundreds of stars to be drawn without their position being updated
class Star:
    def __init__(self, x, y, rad, col):
        self.x = x
        self.y = y
        self.rad = rad
        self.col = col

    # drawing the star
    def draw_star(self):
        arcade.draw_circle_filled(self.x, self.y, self.rad, self.col)


# class inheriting arcade.Window, allows for updates, drawing, and anything else in the final animation to be made
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # creating the moon object with its proper variables
        self.moon = Moon(300, 400, 50, arcade.color.LAVENDER_GRAY, 3, 2, )

        # creating the background object
        self.background = Background(300, 300, 600, 600, 1, 1, 1, 1.3, 1.5, 2)

        # varying lists that creating objects will be placed into and later iterated through
        self.star_list = []
        self.cloud_list = []
        self.piece_list = []

        # cloud creation loops
        for i in range(5):
            # set variables for all pieces made in the j loop
            # randomized again in the next iteration
            x = random.randint(300, 600)
            y = random.randint(300, 600)
            dx = random.random() + random.randint(1, 3)
            for j in range(20):
                # the loop that makes all the pieces of a cloud based off the variables in the i loop
                x1 = x + random.randint(-40, 40)
                y1 = y + random.randint(-20, 20)
                rad = random.randint(10, 20)
                # creating the cloud piece and appending it to the piece list
                self.cloud_piece = CloudPiece(x1, y1, rad, arcade.color.PERIWINKLE, dx)
                self.piece_list.append(self.cloud_piece)
            # appending the previously made piece list to the cloud list
            self.cloud_list.append(self.piece_list)

        # loop that creates all the stars in the animation
        for i in range(300):
            x = random.randint(0, SW)
            y = random.randint(0, SH)
            rad = random.randint(1, 3)
            self.star = Star(x, y, rad, (163, 197, 255))
            self.star_list.append(self.star)

    def on_draw(self):
        # method that draws every creating object
        arcade.start_render()
        self.background.draw_background()

        # drawing each star in the star list
        for star in self.star_list:
            star.draw_star()

        # draws the moon in front of the stars
        self.moon.draw_moon()

        # runs through cloud list, which runs through each piece list, drawing each piece and creating a cloud
        for cloud in self.cloud_list:
            for piece in self.piece_list:
                piece.draw_cloud()

    def on_update(self, dt):
        # method responsible for updating the image, creating an animation

        # updates background, changes color
        self.background.update_background()

        # updates position of the moon
        self.moon.update_moon()

        # updates position of each piece of every cloud
        for cloud in self.cloud_list:
            for piece in self.piece_list:
                piece.update_cloud()


def main():
    # main function
    # instantiating the MyGame class
    window = MyGame(SW, SH, "Caleb Little Ch. 11 Project")
    arcade.run()

# if the namespace is == __main__, calls the main function
if __name__ == "__main__":
    main()
