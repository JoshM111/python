# Create a Flower class, a Flower is made of a color and type that are supplied by you. Additional attributes of Flowers include been_picked, height, and num_petals. 
# num_petals should always begin at 0 for every new instance of Flower, been_picked starts as False, whereas height should begin at 1.

# Create the following methods:

# grow: num_petals increases for that particular Flower by 2, and height increases by 3
# stepped_on: height decreases for that particular Flower by 2 (A Flower should NEVER have a height less than 1)
# plucked: num_petals decreases for that particular Flower by 1 (A Flower should NEVER have a num_petals less than 0)
# picked: been_picked for that particular Flower becomes True
# planted: been_picked for that particular Flower becomes False
# say_info: When been_picked is true, say "I can't find where this flower is!", otherwise print something similar to the following on ONE line:
# "color: red, type: rose, # of petals: 4, height: 6"


class Flower:
    def __init__ (self, color, variety, num_petals, been_picked, height):
        self.color =  color
        self.variety = variety
        self.num_petals = 0
        self.been_picked = False
        self.height = 0
    def grow(self, amount, inches):
        self.num_petals += amount
        self.height += inches
        return self
    def stepped_on(self, amount):
        if self.height <= 1:
            return "Watch where you're stepping!"
        else:
            self.height = self.height- amount
        return self
    def plucked(self):
        self.num_petals = self.num_petals - 1
        if self.num_petals <= 0:
            return "Dont touch me!"
        return self
    def picked(self):
        if self.been_picked == True:
            return True
        return self
    def planted(self):
        self.been_picked = False
        return self
    def say_info(self):
        if self.been_picked == "True":
            print("I can't find where this flower is!") 
        else:
            print(f"Color: {self.color},Type: {self.variety},# of Petals: {self.num_petals},Height: {self.height}")
        return self

rose = Flower("red", "rose", 15, "True", 4)
print(rose.been_picked)
print(rose.height, rose.num_petals)

rose.say_info()

# I am having trouble with the picked and planted portion of the code