# edit


class Chef:

    def __init__(self, x: int, y: int):
        """This is the chef class, it will be the class of the chef characters
        in the game
        :param x: Is the x position of the chef
        :param y: Is the position in y of the chef
        :param holding: Determines if the chef is holding something or not"""

        self.x = x
        self.y = y
        self.holding = False

        # * We now make the intial position of the chef class

        self.image = (0, 0, 0, 16, 16)  #Change: Before self.image[3] was 0


        # * We now make the properties and setters

        # * For the x

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):

        if not isinstance(x, int):
            raise TypeError("The x coordinate must be an integrer")
        elif x < 0:
            raise ValueError("The x coordinate must be bigger than zero")
        else:
            self.__x = x

    # * For the y

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):

        if not isinstance(y, int):
            raise TypeError("The y coordinate must be an integrer")
        elif y < 0:
            raise ValueError("The y coordinate must be bigger than zero")
        else:
            self.__y = y

    # * We now make the method to move the character

    def move(self, direction: str, board_x_size: int, board_y_size: int):
        """This is the move method, aimed at moving the chefs
        :param board_x_size: gives the x value of the board
        :param board_y_size: gives the y value of the board
        :param direction: gives the direction to which the chef moves"""
        # * We define the directions
        DIRECTIONS = ("right", "left", "up", "down")

        if not isinstance(board_x_size, int):
            raise TypeError("The board size (x) must me an integer")
        if not isinstance(board_y_size, int):
            raise TypeError("The board size (y) must be an integer")
        # * We check the direction values
        if not isinstance(direction.lower(), str):
            raise TypeError("The direction must be a string")
        elif direction.lower() not in DIRECTIONS:
            raise ValueError("The direction must be right, left, up or " \
            "down")


        # * We define the map bounds we want

        MAP_BOUNDS = (0, 48, board_x_size, 160)
        # Left in x, up in y, right in x, down in y

        # ( The 48 is bc the first 48 tiles must be left black for scores...)

        CENTRE_BOUNDS_Y = (95, 113)

            # VERTICAL MOVEMENT REQUIREMENTS

        if direction.lower() == "up" and self.y > MAP_BOUNDS[1] \
        and not (CENTRE_BOUNDS_Y[0] < self.y < CENTRE_BOUNDS_Y[1]):
            self.y -= 1
        elif direction.lower() == "down" and self.y < MAP_BOUNDS[3] - self.image[4] \
        and not (CENTRE_BOUNDS_Y[0] - self.image[4]  < self.y < CENTRE_BOUNDS_Y[1] - self.image[4]):
            self.y +=1

            # HORIZONTAL MOVEMENT REQUIREMENTS

        elif direction.lower() == "right" and ((self.x + self.image[3]) < MAP_BOUNDS[2]):
            self.x += 1
        elif direction.lower() == "left" and (self.x > MAP_BOUNDS[0]):
            self.x -= 1


    def __str__(self):

        chef



