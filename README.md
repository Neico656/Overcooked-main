# Overcooked
Final programming project.
This file contains information about the what each file from the current main branch contains. 

board22.py: It is home for the Board class, and import pyxel and all other classes on the game. 

-Board Class: It should contain all the elements which will be required for the game. 
Its attributes are: 
#The height must also include the scoreboard, orders, time...
Height: The vertical length of the screen displayed
Width: The horizontal length of the screen displayed
Chef1: The first player
Chef2: The second player
Chef1.image: Image of the first player 
Chef2.image: Image of the second player

Defined the attributes of the class, Board22.py contains two main methods: 

def update(self): Which executes the logical part of the game, repeatedly. With logical part of the game
we're referring to the distinct methods from the classes that are used to implement the logic of the game.
Until this moment these are: 
chef1/2.move, which takes in position the direction in which we want the chef to move and move it if some 
placement requirements are meet, (e.g Not in bounds) 

def draw(self): Repeatedly executes the code in charge of drawing all the elements necessary, the background 
the chef, the state of the ingredients, etc...

_________________________________________


chef22.py: It is home for the Chef class. It doesn't import any further class
-Chef Class attributes: 
self.x: Position with respect to the horizontal axis 
self.y: Position with respect to the vertical axis
self.holding: Bool value, determines whether a dish is being held or not

The move method used by board, is defined in this class. This method takes in the following parameters: 
Direction: Direction in which the chefs wants to be moved, its value is determined by user input
#Move takes in the sizes of the board, so that it can later use them as boundaries. 
Board_x_size: Horizontal size of the board 
Boarx_y_size: Vertical size of the board 

Then the method is divided in two main parts: 
A first one where it checks that the board values entered are correct. 
A second one where it calculates whether the chef is allowed to move in the direction it is told to move. 
Note that it is no part checking that direction is correct as these are already fixed in board22.py


___________________________________________

dish22.py: It is home for the Dish class and it imports the Chef class and the ingredients Class 

The add_ingredients is defined in this class. This method takes the following parameters:
ingredient: an ingredient from the Ingredient class that will be added to a list containing all ingredients in the dish.

The remove_ingredients is defined in this class. This method takes the following parameters
ingredient: an ingredient from the ingredient class. This will remove the ingredient if and only if it is inside the plate.

The move method is also defined in this class. It takes the following parameters:
chef: it is a Cheff class object so its position can be obtained and this adjust the position of the dish in function of the movement
of the chef and wether it is picked or not.



