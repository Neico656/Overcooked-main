#This class aims to gather all the different stations that can be found in the game. 
#We consider as stations, all the elements on which a player can perform an action.
#This let us with: ingredient holder, surfaces, sink, pan, blender, delivery surface, dish container. 
#We consider to create inheritanced classes for each individual station which will have as methods, 
#the actions that can be performed on it. For instance class IngredientHolder(Station): def extract_ingredient(self)

class Station: 

    def __init__(self):
        ": param action: It defines whether an action has been performed on a station  "

        self.used= False

        self.__stations_positions= {"Ingredient holder": [(0,32),(16,32),(32,32),(0,152),(16,152)],
                                    "Chopping board": [(64,32),(80,152)],
                                    "Blender": (96,32),
                                    "Serving station": (168,32),
                                    "Passing stations": [(16,96), (48,96), (112,96), (152,96)], 
                                    "Bin": (80,96),
                                    "Sink": (144,96),
                                    "Pan": (112,160),
                                    "Dirty dish":(128,160), 
                                    "Dish": (144,160) 
                                    }
                                                             
    
    #Defining the property and setter for actions as it can be read and edited
    @property

    def action(self): 

        return self.__action

    @action.setter

    def action(self, action): 

        if not isinstance(bool, action): 

            raise TypeError("Action must be a boolean ")

        else: 

            self.__action=action


    #This method needs to check the position of the chef and if it coincides with the position 
    #of any of the available stations. 

    #For now this method is only able to detect when the chef is close an station adn return this postition.
    #We may also be able of detecting which types of station has been used, by obtaining the key of the values
    #which coincide. 

    def selected(self, chef):
        ": param station: station has to be a Station object"
        ": param chef: chef has to be a Chef object"

        for key, element in self.__stations_positions.items(): 

        #If element is a list that implies that there are several stations of that type, e.g ingredient holders
            if isinstance(element,list): 
                
                for i in element: 

                    if chef.x== i[0] and chef.y==i[1]: 

                        self.used=True
                        position= [chef.x, chef.y]
                        type_station= key 
                        

        #If element is not a list that implies that there is only one station of that type
            else: 

                if chef.x==element[0] and chef.y==element[1]:

                    self.used=True
                    position= [chef.x, chef.y]
                    type_station= key
        
        return position and key
                    

            

        






    




        
