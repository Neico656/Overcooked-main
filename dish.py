from chef import Chef
from ingredient import Ingredient
class Dish:
    # * We make the dish class

    def __init__(self, x: int, y: int):
        """This is the dish class, it aims to represent the plates
        : param x: repsents the x position of the plate sprite
        : param y: represents the y position of the plate sprite
        : param taken: represents if the plate is taken or not"""
        self.x = x
        self.y = y
        self.taken = True
        self.ingredients = []

        self.image(0,0,16,16,16)

    # * We define properties and setters

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):

        if not isinstance(x, int):
            raise TypeError("The x coordinate must be an ineter")
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
            raise TypeError("The y coordinate must be an ineter")
        elif y < 0:
            raise ValueError("The y coordinate must be bigger than zero")
        else:
            self.__y = y

    def add_ingredients(self, ingredient: Ingredient) -> list:
    # This method appends the whole of the ingredient's class not just
    # its name to control its state and cooked or not state
        if ingredient not in self.ingredients:
            
            self.ingredients.append(ingredient)

        else:

            return NotImplemented

    # This is the remove_ingredients class to remove the ingredients from a plate

    def remove_ingredients(self, ingredient: Ingredient) -> list:

        if ingredient in self.ingredients:

            self.ingredients.remove(ingredient)

        else:

            return NotImplemented

    # This will be the move method, that will move the sprite around

    # * We make the movement of the plate

    def move(self, chef: Chef):

        # The movement and position will depend if it is picked or not

        #self.picked changed by self.taken
        if self.taken and chef.holding:

            # The x position doesn't matter, only the y position
            self.y = chef.y - 16

        # If it is not picked then it will maintains its position

        
        
