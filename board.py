import pyxel
from chef import Chef
from ingredient import Ingredient
#importing json library 
import json


class Board:

    def __init__(self, file_name: str):
        "The class board will include everything that will be shown"
        ":param file_name a json file with all the required config file " 
        
        #Reading the file and storing its information into a dictionary 
        with open(file_name, "r") as file:
            #configutation is a dictionary with the file contents
            # 
            configuration= json.load(file)

        #THIS IS WRONG 
        self.height = configuration.get("heigth")
        self.width = configuration.get("width")
        
        # * We define the chefs that will be appearing

        self.chef1 = Chef(80, 64) # It will appear in the 
        # middle
        self.chef2 = Chef(80, 128)

        # * We define the pyxel assets we want to use for the chefs

        self.chef1.image = (0, 0, 0, 16, 16)
        # * Its format is 1: image nº, 2 and 3 starting x and y, 4 and 5 sprite
        # * width and height dimensions
        self.chef2.image = (0, 16, 0, 16, 16)


        # * We need to initialize and load pyxel
        pyxel.init(self.width, self.height, "Overcooked")

        # * We need to load the pyxel sprites
        pyxel.load("assets/sprites.pyxres")

        # *This will make it so python self updates the sprites with movement
        pyxel.run(self.update, self.draw)

    def update(self):
        """This is a pixel method that will make it so it is exectuded in every"
        "itaration of the game"""


        #Movement module: 
        # * We make the movements for the first character 

        if pyxel.btn(pyxel.KEY_A):
            self.chef1.move("left", self.width, self.height)
        if pyxel.btn(pyxel.KEY_S):
            self.chef1.move("down", self.width, self.height)
        if pyxel.btn(pyxel.KEY_D):
            self.chef1.move("right", self.width, self.height)
        if pyxel.btn(pyxel.KEY_W):
            self.chef1.move("up", self.width, self.height)

        # * We make the movements for the second character

        if pyxel.btn(pyxel.KEY_UP):
            self.chef2.move("up", self.width, self.height)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.chef2.move("down", self.width, self.height)
        if pyxel.btn(pyxel.KEY_LEFT):
            self.chef2.move("left", self.width, self.height)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.chef2.move("right", self.width, self.height)
    
    def draw(self):
        """This method will update itself in every iteration"""

        pyxel.cls(0)

        # We draw the map

        pyxel.blt(0, 0, 1, 0, 0, 192, 176)

        # Printing the first chef
        pyxel.blt(self.chef1.x, self.chef1.y, *self.chef1.image)
        # Printing the seond chef
        pyxel.blt(self.chef2.x, self.chef2.y, *self.chef2.image)

        # We display the coordinates of the chefs

        pyxel.text(10, 10, f"({self.chef1.x},{self.chef1.y}", 7)
        pyxel.text(150, 10, f"({self.chef2.x},{self.chef2.y}", 7)

        # We display a text when the action key is pressed

        if pyxel.btn(pyxel.KEY_LSHIFT):
            pyxel.text(self.chef1.x, self.chef1.y - 10, "action", 7)

        if pyxel.btn(pyxel.KEY_RSHIFT):
            pyxel.text(self.chef2.x, self.chef2.y - 10, "action", 7 )

        



