class Toy:
    #methods go here
    def __init__ (self, name, toy_catchphrase): # methods are functions that go in classes
        print("__init__ has been called!")
        #toy attributes go here
        # self = "this" in JS= the one instance that has called this method
        self.name = name #creating key-value pair inside of the dictionary
        self.owner= "Andy" # can create attribute but not pass it below.
        self.catchphrase = toy_catchphrase
        #return self is assumed in the init function
        self.lover = None
    def say_catchphrase(self):
        print(self.catchphrase)
        return self
    def say_info(self):
        print("Hey my name is ", self.name)
        print("My owner's name is ", self.owner)
        return self
    def create_soulmate(self, soulmate):
        self.lover =  soulmate
        return self

woody = Toy("Woody", "Howdy Partner!") #individual -> instance
print(woody.name)
buzz = Toy("Buzz", "To Infinity and Beyond!") # individual -> instance
print(buzz.name)

woody.say_catchphrase().say_info()
buzz.say_catchphrase().say_info()

jessie= Toy("Jessie", "Yee-Haw!!")
woody. create_soulmate(jessie)
print(woody.lover.name)
jessie.create_soulmate(buzz)
print(jessie.lover.name) #this wouldnt be updated.
buzz.create_soulmate(woody)
print(buzz.lover.name)
print(buzz.lover.lover.lover.lover.lover.name)
# chaining methods together
