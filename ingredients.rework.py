# This will be the class for the diferent ingredients
#Future ideas, developnment: 
#-Create an specific class for each ingredient, to better handle position, and images, and work with objects in this class

# This is the reworked ingredients class due to confusion with the original

# IMPORTANT, READ ME THEN DELETE THESE COMMENT AND THE ONES ABOVE:
# Not added everything in the original class due to confusion
# Why is picked a private method??
# Made so you can pick it up from a distance of 8 pixels so you do not need to
# be extremely close to it

from chef import Chef

class Ingredient:
    """This is the ingredient class that will describe the behaviour of the
    ingredients in the game."""

    def __init__(self, type: str, x: int, y: int):
        """This will be the class for the ingredients to be used
        :param type: This will be the type of ingredient (chorizo, potato...)
        :param x: It will describe the x position  of the ingredient
        :param y: It will describe the y position of the ingredient
        :param preparation: This will be the state of the ingredient (chopped, blended)
        :param cooked: This will state if the ingredient is cooked or not
        """

        self.__INGREDIENT_TYPES = ("onion", "chorizo", "tomato", "potato", "egg")
        # Variable to be used throught the whole class

        self.type = type.lower() #this is in case we put the ingredient in uppercase
        self.x = x
        self.y = y

        # We add later the self.__INGREDIENT_TYPES (IDK what it is)

        self.preparation = "whole"
        # The preparation states will be whole, choppen and blended

        self.cooked = False
        # It is important to distinguish between the cooked state and the 
        # preparation state, one refers to being whole, chopped, blended and
        # This one refers to being cooked or not

        # Since the ingredients will be moved around they will need an image
        self.__image = (0, 16, 48, 16, 16)
        # Default coordinates are given to be changed later when initializing
    
        self.picked = False
        # This determines if the food is picked - for movement purposes

    # We define the properties and setters

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):

        if not isinstance(type, str):
            raise TypeError("The ingrendient must be a string")
        elif type.lower() not in self.INGREDIENT_TYPES:
            raise ValueError("This is not a valid ingredient type")
        else:
         self.__type = type

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        if not isinstance(x, int):
            raise TypeError("This is the wrong type of vairbale")
        elif x < 0: #CHANGED before was <= 0
            raise ValueError("This is not a valid value of the x coordinate") # CHANGED, before it gave self.x, made no sense
        else:
            self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y : int):
        if not isinstance(y, int):
            raise TypeError("This is the wrong type of vairbale")
        elif y < 0: # Changed, before was <= 0
            raise ValueError("This is not a valid value of the y coordinate") # CHANGED, before it gave something that didn't exist
        else:
            self.__y = y

    def chop(self) -> str:

        # We do not check if the ingredient can be chopped as the task allows to chop
        # all of the ingredients, same for blended and other states

        if self.cooked == False and self.preparation == "whole":

            self.preparation = "chopped"

            #After it the image should be changed to that of the chopped element, 
            #to make things easier, the images of the same ingredient should be next to
            #other so image only needs to be (0,(images[i][0])+16,images[i][1],16,16)
            
        else:
            return NotImplemented

    # We define the blend method, responsible for changing the state to blended

    def blend(self) -> str:

        # In this case, if it is chopped it will be able to be blended as it
        # makes no difference to whether it should or not be able to be blended


        if self.preparation != "blended":

            self.preparation = "blended"

        else:

            return NotImplemented

        # We define a method to change the state of the ingredient to cooked or not

    def cook(self) -> str:

        # We check for the ingredients that can actually be cooked
        COOKABLE = ("onion", "potato", "egg", "chorizo")

        if not self.cooked and self.type in COOKABLE:

            self.cooked = True

        else:

            return NotImplemented

    
    #Ingredient will be an Ingredient object and chef a Chef object
    def pick(self, ingredient: Ingredient, chef: Chef): 

        if (chef.x -8 <= ingredient.x <= chef.x + 8 ) and \
        (chef.y + 8 <= ingredient.y <= chef.y + 8):
        # Update: change the radius so they do not need to be in the same
        # exact coordinates to be picked up

            self.picked=True
        
        else: 
            self.picked=False
