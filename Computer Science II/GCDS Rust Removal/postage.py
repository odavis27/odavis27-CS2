# postage class to store all info of inputed postage info
class postage:
    def __init__(self,length,thick, height):
        self.length = length
        self.thick = thick
        self.height = height
        self.type = None
        self.cost = 0
        #set_postage_type()

    def set_postage_type(self):
        # check if postage is any of the following:
        # check for regular post card

    #   regular post card
    #----------------------------------------------------------------------
        if self.length >= 3.5 and self.length <= 4.25 and self.height >= 3.5 and self.height <= 6 and self.thick >= 0.007 and self.thick <= 0.016:
            # postage is regular card
            self.type = 1
    #   large post card
    #----------------------------------------------------------------------
        elif self.length > 4.25 and self.length < 6 and self.height > 6 and self.height < 11.5 and self.thick >= 0.007 and self.thick <= 0.015:
            # postage is regular card
            self.type = 2
    #   envelope
    #----------------------------------------------------------------------
        elif self.length >= 3.5 and self.length <= 6.125 and self.height >= 5 and self.height <= 11.5 and self.thick >= 0.016 and self.thick <= 0.25:
            # postage is enevlope
            self.type=3
    #   Large Evelope
    #----------------------------------------------------------------------
        elif self.length > 6.125 and self.length < 24 and self.height >= 11 and self.height <= 18 and self.thick >= 0.25 and self.thick <= 0.5:
            # postage is large evelope
            self.type=4
    #   packages
    #======================================================================
        elif self.length + self.height*2 + self.thick*2 <= 84:
            self.type=5
        elif 84 < self.length + self.height*2 + self.thick*2 <= 130:
            self.type=6


    def get_zones(self,zip):
        if zip < 7000:
            return 1
        elif zip < 20000:
            return 2
        elif zip < 36000:
            return 3
        elif zip < 63000:
            return 4
        elif zip < 85000:
            return 5
        elif zip < 100000:
            return 6

    # get_cost functions as a bit of main
    def get_shipping_cost(self,zip_1,zip_2):
        if self.type != None:
            zone_costs = {1:0.03,2:0.03,3:0.04,4:0.05,5:0.25,6:0.035}
            start_costs = {1:0.2,2:0.37,3:0.37,4:0.6,5:2.95,6:3.95}

            # get distance via absolute value of zip 1 - zip 2
            # then, input distance into get zones function to get number of zones traveled
            traveled_zones = self.get_zones(abs(zip_1-zip_2))-1
            # input current postage type into both dictionaries to get the price factor
            # then multiply it by the number of zones traveled through
            cost = (zone_costs[self.type]*traveled_zones)+start_costs[self.type]


if __name__ == "__main__":
    new_postage_input = input('''
Please input the information for your package
    The order the must info must go in is
    - length
    - width
    - thickness
Package Information:
    ''')
    new_postage
    pass


