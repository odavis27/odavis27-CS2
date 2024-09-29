''' 
Oliver Davis
11/5/2023
Description:
   a program to get the cost of a package based on its dimensions and zip codes
Bugs:
    im not aware of any bugs currently
Constaints:
    Inserting a non numerical character or less than/more than the required number of inputs
Instructions:
    upon running the file user will be prompted to insert package information
    the package info must be all numerical and 5 inputs are required
    the order of inputs should go:
        - package length
        - package width 
        - package height
        - zip code 1
        - zip code 2
Log: 
 9/26/24 v.1
'''
class postage:
    """
    Class to storage all info and functions of the postage. Mostly 
    just exists because it looks better an help organize things
    Args:
        length (float): the packages length
        height (float): the packages height
        thick (float): the packages thick
    """
    def __init__(self,length, height, thick):
        self.length = length
        self.height = height
        self.thick = thick
        self.type = None
        self.cost = 0

    def set_postage_type(self):
        """
        sets self.type to the potage type based on a bunch of 
        restrictions the dimensions of the package must be within
        Args:
            none
        """
        # check if postage is any of the following types using size restriction given:

        # regular post card
        if self.length >= 3.5 and self.length <= 4.25 and self.height >= 3.5 and self.height <= 6 and self.thick >= 0.007 and self.thick <= 0.016:
            # postage is regular card
            self.type = 1
        # large post card
        elif self.length > 4.25 and self.length < 6 and self.height > 6 and self.height < 11.5 and self.thick >= 0.007 and self.thick <= 0.015:
            # postage is regular card
            self.type = 2
        # envelope
        elif self.length >= 3.5 and self.length <= 6.125 and self.height >= 5 and self.height <= 11.5 and self.thick >= 0.016 and self.thick <= 0.25:
            # postage is enevlope
            self.type=3
        # Large Evelope
        elif self.length > 6.125 and self.length < 24 and self.height >= 11 and self.height <= 18 and self.thick >= 0.25 and self.thick <= 0.5:
            # postage is large evelope
            self.type=4
        # Packages
        #=============
        elif self.length + self.height*2 + self.thick*2 <= 84:
            self.type=5
        elif 84 < self.length + self.height*2 + self.thick*2 <= 130:
            self.type=6


    def get_zones(self,zip):
        """
        calculates the cost of package with the type as well as zip codes
        Args:
            float: zip code needed to convert to shipping zone
        Returns:
            int: shipping zone argument "zip" is within
        """
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

    def set_shipping_cost(self,zip_1,zip_2):
        """
        calculates the cost of package with the type as well as zip codes
        Args:
            float: packages starting zip code (zip_1) 
            float: packages starting zip code (zip_1)
        Returns:
            none
        """
        if self.type != None:
            zone_costs = {1:0.03,2:0.03,3:0.04,4:0.05,5:0.25,6:0.35}
            start_costs = {1:0.2,2:0.37,3:0.37,4:0.6,5:2.95,6:3.95}

            # get distance via absolute value of zip 1 - zip 2
            # then, input distance into get zones function to get number of zones traveled
            traveled_zones = abs(self.get_zones(zip_1)-self.get_zones(zip_2))

            # input current postage type into both dictionaries to get the price factor
            # then multiply it by the number of zones traveled through. 
            cost = (zone_costs[self.type]*traveled_zones)+start_costs[self.type]
            # include only the first two float digits
            cost = format(cost, '.2f')
            # if the first letter in the cost is a zero, remove it
            self.cost = str(cost).lstrip("0")

# this function is probally not needed but it looks nicer than the same line over and over in the code
# all it does is print out a line
def seperate_line():
    # seperate line to make output look pretty
    print('---------------------------------------')  

def main():
    '''
        main function
    '''
    # make a usless counter
    useless_next_count = ''
    # while true to allow user to input multiple inputs in one run of the file
    while True:
        # prompt user for package info
        new_post_input = input(f"Input the information for your{useless_next_count} package:\n   ")
        #new_post_input = test1
        # excepting to prevent spitting errors at user if a non-digit character
        # for dimensions/zip code (or anything else I havent thought about)
        try:
            # convert all items in new_post_input into seperate floats stored in a list
            post_info = [float(i) for i in new_post_input.split(',')]
            # create a new postage class with inputed dimensions
            new_post = postage(post_info[0],post_info[1],post_info[2])
            # set the new postage's type
            new_post.set_postage_type()

            # if it is mailable
            if new_post.type != None:
                # get shipping cost
                new_post.set_shipping_cost(post_info[3],post_info[4])
                # print the cost with 2 decimal places
                print(f"Cost to mail: {new_post.cost}")
                seperate_line()
                # increase useless_next_count by one more next (comment out if you are boring)
                useless_next_count+=" next"
            else: 
                print("Package is unmailable")
                seperate_line()
        except ValueError:
            print("Inserted characters must be numerical")
            seperate_line()
        except IndexError:
            print("Must be five inputs")
            seperate_line()

if __name__ == "__main__":
    main()