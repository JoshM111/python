# 1#
# With this concept of default parameters in mind, the goal of this assignment is to write a single function, randInt() that takes up to 2 arguments.
# If no arguments are provided, the function should return a random integer between 0 and 100.
# If only a max number is provided, the function should return a random integer between 0 and the max number.
# If only a min number is provided, the function should return a random integer between the min number and 100
# If both a min and max number are provided, the function should return a random integer between those 2 values.
# Here are a couple of important notes about using random.random() and rounding. 
# (Create this function without using random.randInt() -- we are trying to build that method ourselves for this assignment!)

# random.random() returns a random floating number between 0.000 and 1.000
# random.random() * 50 returns a random floating number between 0.000 and 50.000
# random.random() * 25 + 10 returns a random floating number between 10.000 and 35.000
# round(num) returns the rounded integer value of num

# Here's a little bit of code to get you started, with some test cases and expected outputs. 
# Test each function call one at a time and a few times each to make sure you're getting the correct range.

# import random
# def randInt(min="", max= ""):
#     num = random.random() * 50 + 25
#     return num

# print(randInt())
# print(randInt(max=50))
# print(randInt(min=50))
# print(randInt(min=50, max=500))

import random

def randint(min=0, max=100):
  possible_range = max - min
  return round(random.random() * possible_range + min)

print(randint())
print(randint(max=50))
print(randint(min=50))
print(randint(min=50, max=150))

'''
This is mostly just a math problem.
First, we start by getting the possible range of numbers.
The range will be used to multiply the number created by random, which is between 0 and 1.
Multiplying this number will give us a number that is no greater than the range, but no less than 0.
For instance, if we're given 20 and 70, the range is 50, so we'll first start by getting a number between 0 and 50.
If the minimum is greater than 0, we have to make sure the number cannot be less than the minimum, so we must add the minimum value to our calculated random number.
Since we've already accounted for the range, if we add 20 (our min from the example) to a number between 0 and 50, then mathematically it cannot be lower than 20 or higher than 70.
Then we just round to get an integer instead of a float.
'''