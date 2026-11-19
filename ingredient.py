# This will be the class for the diferent ingredients
#Future ideas, developnment: 
#-Create an specific class for each ingredient, to better handle position, and images, and work with objects in this class
import json




class Ingredient:
    """This is the ingredient class that will describe the behaviour of the
    ingredients in the game."""

    def __init__(self, file_name, type: str, x: int, y: int):
        """This will be the class for the ingredients to be used
        :param type: This will be the type of ingredient (chorizo, potato...)
        :param preparation: This will be the state of the ingredient (chopped, blended)
        :param cooked: This will state if the ingredient is cooked or not
        :param x: It will describe the x position  of the ingredient
        :param y: It will describe the y position of the ingredient
        """

        with open(file_name, "r") as file:                       
            #configutation is a dictionary with the file contents
            #                                                    
            configuration= json.load(file)                       


        self.preparation ="whole"
        # For the state it will start whole like every item in the game

        self.cooked = False
        # It is important to distinguish between the cooked state and the 
        # preparation state, one refers to being whole, chopped, blended and
        # This one refers to being cooked or not

        self.x = x
        self.y = y

        # Since the ingredient will be draw it will need an image

        self.__image = (0, 16, 48, 16, 16)
        # Default coordinates are given to be changed later when initializing

       
        self.__INGREDIENT_TYPES = configuration.get("INGREDIENT_TYPES") #Added Dani
        #Type has to be after self.__INGREDIENT_TYPES since it has to check it to set its own value
        # 
        self.type = type.lower() # Added Nico
        # type has to be lower so it stores the same values as in ingredient types even if typed differently
        
        self.__picked=False


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

    def image(self): 

        return self.__image

    
    def update_image(self):

        #Defining coordinates for each of the ingredients
        onion_image= (8, 46)
        chorizo_image= ("To be replaced by start_x", "To be replaced by start_y")
        tomato_image= ("To be replaced by start_x", "To be replaced by start_y")
        potato_image= ("To be replaced by start_x", "To be replaced by start_y")
        egg_image= ("To be replaced by start_x", "To be replaced by start_y")

        #This list will contain both positions of the object as indixes in the form of tuples
        images= [onion_image,chorizo_image, tomato_image, potato_image, egg_image]

       #By iterating through self.type, the index of the ingredint in __INGREDIENT_TYPES can be found 
       #and used for assigning the proper image to the selected ingredient

        for i in range(len(self.INGREDIENT_TYPES)):

            if self.INGREDIENT_TYPES[i]==self.type:

                self.__image= (0, images[i][0],images[i][1],16,16)


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

    @property

    def picked(self): 

        return self.__picked

    @property 

    def INGREDIENT_TYPES(self): 

        return self.__INGREDIENT_TYPES

    # We will now define the methods that will change the state of the ingredient

    # We define the chop method, responsible for changing the state to chopped

    def chop(self) -> str:

        # We check if the ingredient can be chopped (is a choppable ingredient
        # (and is not already chopped or on another state where you can't chop it)

        CHOPPABLE = ("tomato", "potato", "chorizo", "onion")

        if self.type in CHOPPABLE and self.cooked == False and self.preparation \
            == "whole":

            self.preparation = "chopped"

            #After it the image should be changed to that of the chopped element, 
            #to make things easier, the images of the same ingredient should be next to
            #other so image only needs to be (0,(images[i][0])+16,images[i][1],16,16)

        else:
            return NotImplemented

    # We define the blend method, responsible for changing the state to blended

    def blend(self) -> str:

        # We check if the ingredient can be blended (is a blendeable ingredient)
        # In this case, if it is chopped it will be able to be blended as it
        # makes no difference to whether it should or not be able to be blended

        BLENDEABLE = ("tomato", "onion") # For the gazpacho recipe

        if self.type in BLENDEABLE and self.preparation != "blended":

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
    def pick(self, ingredient, chef): 

        if (ingredient.x== chef.x) and (ingredient.y== chef.y): 

            self.__picked=True
        
        else: 
            self.__picked=False

            
            

    




# ! Some things to consider in this class for the future, since ingredients are
# ! cooked together maybe something needs to be added to that

# ! In blendeable you could potentially blend something again, up to discussion



        
