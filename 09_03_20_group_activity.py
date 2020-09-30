numbers = [5, [7, 3, 12, 14], [8, 99, 60], 16, [9]]

#Print the following numbers using the above variable:

#1 - 16
print(numbers[3])
#2 - 12
print(numbers[1][2])
#3 - 9
print(numbers[4][0])

fido = {"can_roll_over": True, 
        "can_fetch": False, 
        "num_times_barked": 764, 
        "owners": ["Hal", "Lois"]}

#Print the following things using the above variable:

#4 - False
print(fido["can_fetch"])
#5 - "Lois"
print(fido["owners"][1])


superheroes = [
    {"name": "Wonder Woman", "power": "super strength"},
    {"name": "Flash", "power": "runs fast", "extra_field": [7, 8, 54]},
    {"name": "Aquaman", "power": "talks to aquatic creatures"},
    {"name": "Spiderman", "power": "shoots webs"}
]

#Print the following things using the above variable:

#6 - "Aquaman"
print(superheroes[2]["name"])

#7 - "super strength"
print(superheroes[0]["power"])

#8 - 54
print(superheroes[1]["extra_field"][2])

#9 - Write a for loop that prints all names in the above variable.
for name in range(len(superheroes)):
    print(superheroes[name]["name"])
# !OR! #- make sure to reference this!
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
for name in superheroes:
    print(name["name"])